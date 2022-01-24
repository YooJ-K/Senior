import os
import cv2

location= r"C:/Users/hyoseok/Desktop/work/child/hangul_xml/"
file_list = os.listdir(location)

print(file_list)

count = 0



    '''

    
    if files.split('.')[-1] == 'jpg':
        img_path = location + files
        new_img_path = location + 'error_file_' + str(count) + '.jpg'
        os.rename(img_path, new_img_path)
        count +=1

    fileName = files.split('_')
    tmpFileName = fileName[1].split('.')
    fileName[1] = tmpFileName[0]
    fileName = 'foreign_kindergarten_' + fileName[2]
  

    new_img_path = location + fileName
    os.rename(img_path, new_img_path)
    
    fileName = files.split('_')
    tmpFileName = fileName[2].split('.')
    fileName[2] = tmpFileName[0]
    fileName = "_".join(fileName)
        
        '''