import cv2

def img_resize(path):
    img = cv2.imread(path)
    if img.shape[0] <= 1000 and img.shape[1] <= 1000:
        return
    re = []
    if img.shape[0] > img.shape[1]:
        re = (int(1000 * (img.shape[1] / img.shape[0])), 1000)
    else:
        re = (1000, int(1000 * (img.shape[0] / img.shape[1])))
    resize_img = cv2.resize(img, re)

    cv2.imwrite('C:/Users/hyoseok/Desktop/work/child/sleeping/test.jpg',resize_img)

img_resize('C:/Users/hyoseok/Desktop/work/child/sleeping/img.jpg')