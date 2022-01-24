import os

path_dir = r'C:/Users/chris/Desktop/label/annotations2'
file_list = os.listdir(path_dir)
#fileName = "annotations2/crop_000010.txt"


for i in file_list:
    fileName = 'annotations2/' + i
    f = open(fileName, 'r', encoding='UTF8')

    lines = f.readlines()

    for line in lines:
        print(line, end='')

    f.close()