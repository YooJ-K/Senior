######################
# img aug 사용시 자주 사용하는 것들 모음

import os

file_dir = input("File Directory(include : /) : ")
file_dir = file_dir.replace("\\", "/") + "/" # 일부 프로그램에서 경로 오류가 있을 수 있음.
file_list = os.listdir(file_dir)

def del_file_name(want_to_del):
    # 파일 이름의 일부를 지우는 함수
    for file in file_list:
        file_path = file_dir + file
        file_name = file.split(want_to_del)
        file_name = ''.join(file_name)
        new_file_path = file_dir + file_name
        os.rename(file_path, new_file_path)

def change_xml_file_name_to_new_file_name_inside_of_the_file():
    # xml 파일 내부에 존재한 <filename>어쩌구</filename>으로 바꿔주는 함수 어쩌구.xml
    for file in file_list:
        file_path = file_dir + file

        f1 = open(file_path, 'r', encoding='UTF8')
        new_file_name = ''
        for line in f1:
            if 'filename' in line:
                new_file_name = line.split('<')[1].split('>')[1].split('.')[0]
                break
        f1.close()

        new_file_path = file_dir + new_file_name + '.xml'
        os.rename(file_path, new_file_path)

def change_filename_in_xml_file_to_xml_file_name(img_dir):

    for file in file_list:
        file_path = file_dir + file
        tmp_file = file_dir + 'tmp_' + file

        f1 = open(file_path, 'r', encoding='UTF8')
        f2 = open(tmp_file, 'w', encoding='UTF8')

        img_list = os.listdir(img_dir)
        img_format = ''

        for name in img_list:
            if name.startswith(file.split('.')[0]):
                img_format = name.split('.')[1]
                break

        file_name = ''
        for line in f1:
            if 'filename' in line:      
                file_name = file.split('.')[0] + '.' + img_format    
                f2.write('	<filename>' + file_name + '</filename>')
            elif 'path' in line:
                f2.write('  <path>' + img_dir + file_name + '</path>')
            else:
                f2.write(line)
            f2.write('\n')

        f1.close()
        f2.close()

        os.remove(file_path)
        os.rename(tmp_file, file_path)

def change_img_and_xml_file_name(file_name, new_file_name):

    file_path = file_dir + file_name
    new_file_path = file_dir + new_file_name + '.xml'
    img_path = ''

    f1 = open(file_path, 'r', encoding='UTF8')

    for line in f1:
        if 'path' in line:
            img_path = line.split('<')[1].split('>')[1]
            break
    
    new_img_path = img_dir = img_path.split('.')[0].split('/')[:-1]
    print(new_img_path)
    new_img_path.append(new_file_name + '.' + img_path.split('.')[1])
    
    new_img_path = '/'.join(new_img_path)
    img_dir = img_dir[:-1]
    img_dir = '/'.join(img_dir) + '/'
    print(img_dir)

    f1.close()

    os.rename(img_path, new_img_path)
    os.rename(file_path, new_file_path)

    file_list = os.listdir(file_dir)
    
def delete_img_to_half():
    file_list = os.listdir(file_dir)
    for i in range(len(file_list)):
        if i % 2 == 0:
            os.remove(file_dir + file_list[i])
    file_list = os.listdir(file_dir)

def change_img_name():
    want_to_change_file_name = input('name for change : ')
    for file in file_list:
        numbering = file.split('_')[-1]
        newName = want_to_change_file_name + '_' + numbering
        os.rename(file_dir + file, file_dir + newName)

def add_file_format():
    for file in file_list:
        new_name = file_dir + file + '.jpg'
        os.rename(file_dir + file, new_name)

if __name__ == '__main__':
    while True:
        print('########## 원하는 메뉴를 선택하세요. ##########')
        print('1. Delete Part Of File Name')
        print('2. Change .xml file name to new name inside of the .xml file')
        print('3. xml 파일 내부의 이름과 경로를 바꾸기')
        print('4. xml 파일 및 이미지 파일 한번에 이름 바꾸기 (4 이후에 3 무조건 해주기.)')
        print('5. 이미지 반만 삭제하기')
        print('6. 이미지 파일명 디렉토리 내의 모든 파일 한번에 바꾸기 (일련번호 _ 뒤에 존재해야)')
        print('7. 파일 포맷 명 추가하기 제일 뒤에')
        print('0. exit')

        menu = int(input('Menu Number : '))

        if menu == 1:
            print('####################################################################################')
            print('                            Delete Part Of File Name')
            print('####################################################################################')

            want_to_del = input('what do you want to delete in file name? (If you pressed the wrong menu, please press 0.) : ')
            if want_to_del == '0':
                continue
            del_file_name(want_to_del)

            file_list = os.listdir(file_dir)

            print('------ This operation has been completed.')
            print()
        elif menu == 0:
            print('Thank you for your trying. - 김유진')
            break
        elif menu == 2:
            print('####################################################################################')
            print('          Change .xml file name to new name inside of the .xml file')
            print('####################################################################################')

            change_xml_file_name_to_new_file_name_inside_of_the_file()
            file_list = os.listdir(file_dir)

            print('------ This operation has been completed.')
            print()
        elif menu == 3:
            print('####################################################################################')
            print('           Change file name and path inside of the .xml file to new name')
            print('####################################################################################')
            img_dir = input('Please Put Image Directory : ')
            img_dir = img_dir.replace("\\", "/") + "/"

            change_filename_in_xml_file_to_xml_file_name(img_dir)

            print('------ This operation has been completed.')
            print()
        elif menu == 4:
            want_to_change_file_name = input('want to change file name : ')
            
            if want_to_change_file_name == '0':
                continue
            if 'xml' not in want_to_change_file_name:
                want_to_change_file_name += '.xml'
            
            change_img_and_xml_file_name(want_to_change_file_name, input('new name : '))

            print('------ This operation has been completed.')
            print()
        elif menu == 5:
            delete_img_to_half()
            print('------ This operation has been completed.')
            print()
        elif menu == 6:
            change_img_name()
            print('------ This operation has been completed.')
            print()
        elif menu == 7:
            add_file_format()
            print('------ This operation has been completed.')
            print()
        else:
            print('Wrong Menu! ReSelect!')
        
        file_list = os.listdir(file_dir)