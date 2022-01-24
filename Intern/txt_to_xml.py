import os

path_dir = r'C:/Users/chris/Desktop/label/annotations2'
file_list = os.listdir(path_dir)

for i in file_list:
    fileName = 'annotations2/' + i
    f1 = open(fileName, 'r', encoding='UTF8')

    text = f1.readlines()

    f1.close()

    '''fileName = "annotations2/person_199.txt"

    f1 = open(fileName, 'r', encoding='UTF8')
    text = f1.readlines()

    f1.close()'''

    #text = list(input() for _ in range(6))

    text[5] = text[5].split(':')[1].strip()
    objectNum = int(text[5].split()[0])

    #text2 = list(input() for _ in range(6 + objectNum * 7))
    #text += text2

    text[2] = text[2].split('"')
    text[2] = text[2][1].split('/')
    text[2][2] = text[2][2].split('.')
    fileName = text[2][2][0]

    openfileName = "xml2/" + fileName + ".xml"
    f = open(openfileName, 'w', encoding='UTF-8')

    width, height, depth = text[3].split(':')[1].strip().split('x')
    width = width.strip()
    height = height.strip()
    depth = depth.strip()

    database = text[4].split('"')[1]

    f.write("<annotation>\n\
        <folder>pos</folder>\n\
        <filename>" + fileName +".png</filename>\n\
        <path>Train/pos/" + fileName + ".png</path>\n\
        \n\
        <source>\n\
            <database>" + database + "</database>\n\
        </source>\n\n\
        <size>\n\
            <width>" + width.strip() + "</width>\n\
            <height>" + height.strip() + "</height>\n\
            <depth>" + depth.strip() + "</depth>\n\
        </size>\n\
        \n\
        <segmented>0</segmented> \n \n")

    for i in range(objectNum):
        objectName = text[12 + i * 7].split('"')[1]
        bounding = text[12 + i*7 + 5].split(':')[1].strip()
        bounding = bounding.replace(')', '').replace('-', ',').replace('(', '').split(',')

        f.write("    <object>\n\
            <name>" + objectName + "</name>\n\
            <pose>Unspecified</pose>\n\
            <truncated>0</truncated>\n\
            <difficult>0</difficult>\n\
            <bndbox>\n\
                <xmin>" + bounding[0].strip() + "</xmin>\n\
                <ymin>" + bounding[1].strip() + "</ymin>\n\
                <xmax>" + bounding[2].strip() + "</xmax>\n\
                <ymax>" + bounding[3].strip() + "</ymax>\n\
            </bndbox>\n\
        </object>\n\n")

    f.write("</annotation>")

    f.close()