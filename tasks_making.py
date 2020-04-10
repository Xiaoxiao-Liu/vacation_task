#encoding:utf-8
import os
import random,string
import pandas as pd
import numpy as np
# Create files
def file_creating(stu_no, stu_name,class_path):
    file_name = class_path+stu_no+'_'+stu_name+'.py'
    f = open(file_name,'w')
    f.write('# 任务一\n')
    #f.close()
    return f

def task_explanation():
    text_1 = "本次任务旨在帮助同学回顾python基础语法，建议首先复习《python程序设计》课件。"+'\n'
    text_2 = "在完成本次任务时，建议大家多思考，多检索，学会借助百度、python官方文档等工具查找方法，"+'\n'
    text_3 = "同时结合自己的逻辑，完成任务。\n"
    text_4 = "本任务的得分将按照任务提交时间的先后顺序与任务正确率结合来计算，\n"
    text_5 = "由于每位同学的题目都不相同，建议不要抄袭，一旦发现抄袭情况，本次任务判为0分'''\n"
    text = "'''\n" + text_1 + text_2 + text_3 + text_4 +text_5
    return text

def content_writing(text,f):
    f.write(text)
    return f

def first_task():
    annotation = '# 第一题 '
    gap = random.randint(1,10)
    ranges = random.randint(100,1000)
    contents = '求'+str(ranges)+'以内所有'+str(gap)+'的倍数的和'
    text = annotation+contents+'\n'*5
    return text

def second_task():
    annotation = '# 第二题 统计字符串strings中，字母和数字的个数\n'
    num = string.ascii_letters + string.digits
    strings = "".join(random.sample(num,18))
    contents = "strings = '%s'"%strings
    text = annotation + contents+'\n'*5
    return text

def third_task():
    annotation = '# 第三题 给定如下文本\n'
    novel = open("./Harry Potter and The Sorcerer's Stone.txt",'r',encoding = 'gbk').readlines()
    content = list(map(lambda y: y.strip(), filter(lambda l: len(l.strip()) != 0, novel)))
    start =random.randint(0,len(content)-15)
    end = start + 10
    block = "'''" + "\n".join(content[start:end + 1]) + "'''"
    annotation1 = '# 1. 计算文本中的单词数量'+'\n'*5
    annotation2 = "# 2. 计算文本中的句子数量（句子以'.'分隔'）"+'\n'*5
    annotation3 = '# 3. 找出文本中所有专有名词（专有名词：该单词的首字母大写，且该单词不是一个句子的第一个单词）'+'\n'*5
    text = annotation + block + '\n' + annotation1+annotation2+annotation3
    return text

def fourth_task():
    annotation = '# 第四题 打开文件"index.txt"，并读取文本\n'
    annotation1 = '# 1. 计算index的文本中，有多少个url地址（url也可以称作网址，通常在html语言中用href标记）' + '\n' * 5
    annotation2_1 = "# 2. 找出文本中包含的书名，以及书名所对应的书的介绍，将书名与对应的介绍保存在字典中\n"
    annotation2_2 = "# 比如书名为：小王子，对应的介绍为：小王子是一个超凡脱俗的仙童，他住在...\n"
    annotation2_3 = "# 保存在字典后为：{'小王子':'小王子是一个超凡脱俗的仙童，他住在...'}\n"
    annotation2_4 = "# 提示：书名在文本中使用了title标签，书的介绍中都包括了书名"
    annotation2 = annotation2_1 + annotation2_2 + annotation2_3 + annotation2_4 + '\n' * 5
    text = annotation + annotation1 + annotation2
    return text

#os.system('python ./1.py')

if __name__ == '__main__':
    excelFiles = os.listdir('./classes/')

    for f in excelFiles:
        df = pd.DataFrame(pd.read_excel('./classes/' + f))
        class_path = './classes/'+f[3:9]+'/'
        os.mkdir(class_path)
        stu_nos = list(df['学号'])
        stu_names = list(df['姓名'])
        for i in range(len(stu_nos)):
            #print(stu_nos[i])
            #print(stu_names[i])
            stu_no = stu_nos[i]
            stu_name = stu_names[i]
            # 创建文件
            file = file_creating(stu_no,stu_name,class_path)
            # 写入注释
            explanation = content_writing(task_explanation(),file)
            # 写入第一题
            file_task1 = content_writing(first_task(),explanation)
            # 写入第二题
            file_task2 = content_writing(second_task(),file_task1)
            # 写入第三题
            file_task3 = content_writing(third_task(),file_task2)
            # 写入第四题
            file_task4 = content_writing(fourth_task(),file_task3)
            file_task4.close()
            try:
                return_msg = os.popen("python " + class_path)
                print(return_msg.read())
            except:
                print(class_path)

