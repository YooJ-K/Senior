import os
dir = 'C:/Users/hyoseok/Desktop/work/child/img_aug_files/c/'

file_list = os.listdir(dir)

for file in file_list:
    file_path = dir + file

    f1 = open(file_path, 'r', encoding='UTF8')
    new_file_name = ''
    for line in f1:
        if 'filename' in line:
            new_file_name = line.split('<')[1].split('>')[1].split('.')[1]
            break
    f1.close()

    new_file_path = dir + new_file_name + '.xml'
    os.rename(file_path, new_file_path)