#encoding:utf-8
import os
class_path = './classes/J18012/'
file_list = os.listdir(class_path)
for file in file_list:
    cmd = class_path+file
    print(cmd)
    try:
        os.system("python " + cmd)
    except:
        print(file)


