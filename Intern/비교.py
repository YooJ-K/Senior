import os

file_path = 'C:/Users/hyoseok/Desktop/work/child/sleeping/'
aug_file_path = 'C:/Users/hyoseok/Desktop/work/child/img_aug_files/img_aug_for_sleeping/'

file_list = os.listdir(file_path)
aug_file_list = os.listdir(aug_file_path)
tmp = []

for file in aug_file_list:
    tmp_fileName = file.split('_')
    tmp.append('_'.join(tmp_fileName[:-1]))

aug_file_list = list(set(tmp))
count = 0
for file in file_list:
    file_tmp = file.split('.')[:-1]
    file_tmp = '.'.join(file_tmp)
    if file_tmp not in aug_file_list:
        print(file)
        count +=1

print(count)