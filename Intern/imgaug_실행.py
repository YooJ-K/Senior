import imgaug as ia
from imgaug import augmenters as iaa
from files import *
from os import listdir
import cv2
import numpy as np
import xml.etree.ElementTree as ET
from pascal_voc_writer import Writer
import random

#코드가 조금..많이.. 더럽습니다. ㅜㅜ

# 오류 파일 경로
xml_path = 'C:/Users/hyoseok/Desktop/work/child/hangul_xml/'
img_path = 'C:/Users/hyoseok/Desktop/work/child/hangul/'
new_img_save_path = 'C:/Users/hyoseok/Desktop/work/child/img_aug_files/img_aug_for_hangul/'
new_img_xml_save_path = 'C:/Users/hyoseok/Desktop/work/child/img_aug_files/img_aug_for_hangul_xml/'

def read_anntation(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    bounding_box_list = []

    file_name = root.find('filename').text
    for obj in root.iter('object'):

        object_label = obj.find("name").text
        for box in obj.findall("bndbox"):
            x_min = int(box.find("xmin").text)
            y_min = int(box.find("ymin").text)
            x_max = int(box.find("xmax").text)
            y_max = int(box.find("ymax").text)

        bounding_box = [object_label, x_min, y_min, x_max, y_max]
        bounding_box_list.append(bounding_box)

    return bounding_box_list, file_name

def read_train_dataset(dir):
    images = []
    annotations = []

    for file in listdir(dir):
        if 'ini' in file:
            print(file)
            continue
        #if 'jpg' in file.lower() or 'png' in file.lower():
        images.append(cv2.imread(dir + file))
        annotation_file = file.replace(file.split('.')[-1], 'xml')
        bounding_box_list, file_name = read_anntation(xml_path + annotation_file)
        annotations.append((bounding_box_list, annotation_file, file_name))

        #processedData.append(file)
    images = np.array(images)

    return images, annotations

ia.seed(1)

dir = img_path
images, annotations = read_train_dataset(dir)

for idx in range(len(images)):

    image = images[idx]
    boxes = annotations[idx][0]

    ia_bounding_boxes = []
    for box in boxes:
        ia_bounding_boxes.append(ia.BoundingBox(x1=box[1], y1=box[2], x2=box[3], y2=box[4]))

    bbs = ia.BoundingBoxesOnImage(ia_bounding_boxes, shape=image.shape)
    seq = []
    for k in range(10): 

        size = (random.random() * 0.8 + 0.36) * 1000 # 사진의 긴 변 길이 1000으로 맞춰주기 위함
        size = int(size)

        seq.append(iaa.Sequential([
            
            iaa.Affine( # rotate의 각도를 지정해줌
                rotate=[0, 90, 180, 270]
            ),
            iaa.Resize({"longer-side": size, "shorter-side": "keep-aspect-ratio"}), 
            iaa.Fliplr(0.5),
            iaa.Flipud(0.5),
            iaa.ChangeColorTemperature([4000, 4500, 5000, 10000, 20000, 30000]), # range 로 하려면 () 내부에, 랜덤으로 고르려면 [] 내부에
            iaa.LogContrast(gain=(0.6, 1.0)) # 이미지가 밝기로 조정할려고 하니, 안되어서 '대비'로 조정함
        ]))
            

    for k in range(10):

        seq_det = seq[k].to_deterministic()

        image_aug = seq_det.augment_images([image])[0]
        bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
        
        for i in range(len(bbs.bounding_boxes)):
            before = bbs.bounding_boxes[i]
            after = bbs_aug.bounding_boxes[i]

            w, h, c = bbs_aug.shape
            
            if bbs_aug.bounding_boxes[i].x1 < 0:
                bbs_aug.bounding_boxes[i].x1 = 0
            if bbs_aug.bounding_boxes[i].y1 < 0:
                bbs_aug.bounding_boxes[i].y1 = 0
            if bbs_aug.bounding_boxes[i].x2 > h:
                bbs_aug.bounding_boxes[i].x2 = h
            if bbs_aug.bounding_boxes[i].y2 > w:
                bbs_aug.bounding_boxes[i].y2 = w

        image_before = bbs.draw_on_image(image, size=20)
        image_after = bbs_aug.draw_on_image(image_aug, size=0)

        name = annotations[idx][2].split('.')

        image_save_name = new_img_save_path + name[0] + '_' + str(k) + '.jpg' # 임의로 jpg 파일로 설정해 둔 것이니, 수정해도 괜찮습니다.
        cv2.imwrite(image_save_name, image_after)
        #print(annotations[idx][2], name, image_save_name) # box 확인 위함
        h,w = np.shape(image_aug)[0:2]
        voc_writer = Writer(image_save_name, w, h)

        for i in range(len(bbs_aug.bounding_boxes)):
            bb_box = bbs_aug.bounding_boxes[i]
            voc_writer.addObject(boxes[i][0], int(bb_box.x1), int(bb_box.y1), int(bb_box.x2), int(bb_box.y2))

        fName = annotations[idx][1].split('.')[0]

        voc_writer.save(new_img_xml_save_path + fName + '_' + str(k) + '.xml')
