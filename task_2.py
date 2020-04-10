#encoding:utf-8
import os
import random,string
import pandas as pd
import numpy as np
import re
# Create files
def file_creating(stu_no, stu_name,class_path):
    file_name = class_path+stu_no+'_'+stu_name+'.py'
    f = open(file_name,'w')
    f.write('# 任务二\n')
    #f.close()
    return f

def task_explanation():
    text_1 = "本次任务旨在帮助同学回顾python基础语法，建议首先复习《python程序设计》课件1-4章。"+'\n'
    #text_2 = "在完成本次任务时，建议大家多思考，多检索，学会借助百度、python官方文档等工具查找方法，"+'\n'
    #text_3 = "同时结合自己的逻辑，完成任务。\n"
    text_4 = "注意：本任务的得分将按照任务提交时间的先后顺序与任务正确率结合来计算，\n"
    text_5 = "完成本次任务时，不得使用任何第三方软件，不能import任何第三方库"
    text_6 = "由于每位同学的题目都不相同，建议不要抄袭，一旦发现抄袭情况，本次任务判为0分'''\n"
    text = "'''\n" + text_1  + text_4 +text_5+text_6+'\n'
    return text

def content_writing(text,f):
    f.write(text)
    return f

def first_task():
    annotation = '# 第一题 '
    year = random.randint(1700,2019)
    month = random.randint(3, 12)
    day = random.randint(3, 29)
    contents = '请计算%d年%d月%d日是该年份的第几天，注意是否有闰年的情况'%(year,month,day)
    text = annotation+contents+'\n'*5
    return text

def second_task():
    annotation = '# 第二题 统计字符串string_1与字符串string_2中相同的字符并打印，区分大小写\n'
    num_1 = string.ascii_letters + string.digits
    string_1 = "".join(random.sample(num_1,18))
    num_2 = string.ascii_letters + string.digits
    string_2 = "".join(random.sample(num_2,18))
    content_1 = "string_1 = '%s'"%string_1
    content_2 = "string_2 = '%s'"%string_2
    text_1 = annotation + content_1+'\n'
    text_2 = text_1+content_2 +'\n'*5
    return text_2

def third_task():
    annotation = '# 第三题 给定如下文本\n'
    novel = open("./Harry Potter and The Sorcerer's Stone.txt",'r',encoding = 'gbk').readlines()
    content = list(map(lambda y: y.strip(), filter(lambda l: len(l.strip()) != 0, novel)))
    start =random.randint(0,len(content)-15)
    end = start + 10
    block = "'''" + "\n".join(content[start:end + 1]) + "'''"
    annotation1 = '# 1. 统计句子中对话的数量，注意对话使用""标点符号包含'+'\n'*5
    annotation2 = "# 2. 计算文本中所有句子的平均长度，句子以句号、叹号和问号分隔"+'\n'*5
    annotation3 = '# 3. 找出文本中长度最长的单词（字母最多）'+'\n'*5
    text = annotation + block + '\n' + annotation1+annotation2+annotation3
    return text

def fourth_task1():
    files = open('./inex_3.txt').read()
    annotation_0 = '#第四题\n'
    # 第一问
    img_regex = r'<.+src=.+'
    images = re.findall(img_regex, files)
    text_1 = "text_1 = '"+str(random.choice(images))+"'"+'\n'*5
    annotation_1 = '# 1.给定文本text_1，在文本的URL链接中文件名，包括文件类型后缀，例如：box.jpg。\n'
    # 第二问
    type_regex = r'<span><a href=.+'
    movie_types = re.findall(type_regex, files)
    text_2 = "text_2 = '"+str(random.choice(movie_types))+"'"+'\n'*5
    annotation_2 = '# 2.提取文本text_2中的电影类型\n'
    # 第三问
    other_regex = r'<a onclick.+\s.+\s</a>'
    other_results = re.findall(other_regex, files)
    text_3 = "'''\n"+str(random.choice(other_results))+"'''"+'\n'
    annotation_3 = '# 3.给定如下文本,提取文本中的电影名称以及电影链接\n'
    text = annotation_0 + annotation_1 + text_1 +annotation_2 + text_2 + annotation_3 + text_3 +'\n'*5
    return text

def fourth_task2():
    files = open('./inex_3.txt').read()
    annotation_0 = '#第四题\n'
#    annotation1 = '# 1. ' + '\n' * 5
    movie_regex = r'<table.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s.+\s'
    movies = re.findall(movie_regex, files)
    text_1 ="'''\n"+random.choice(movies)+"'''\n"
    annotation_1 = '# 给定如下文本：\n'
    q2 = "# 1.提取电影链接"+'\n'*5
    q3 = '# 2.提取电影名称'+'\n'*5
    q4 = '# 3.提取电影的其他信息，包括上映时间、主演等信息'+'\n'*5
    q5 = '# 4.提取电影评分'+'\n'*5
    text = annotation_0 + annotation_1+text_1 +q2+q3+q4+q5
    return text

if __name__ == '__main__':
    excelFiles = os.listdir('./classes/')
    for f in excelFiles:
        if f == '.DS_Store':
            continue
        else:
            df = pd.DataFrame(pd.read_excel('./classes/' + f))
            class_path = './classes/' + f[3:9] + '/'
            os.mkdir(class_path)
            stu_nos = list(df['学号'])
            stu_names = list(df['姓名'])
            for i in range(len(stu_nos)):
                # print(stu_nos[i])
                # print(stu_names[i])
                stu_no = stu_nos[i]
                stu_name = stu_names[i]
                # 创建文件
                file = file_creating(stu_no, stu_name, class_path)
                # 写入注释
                explanation = content_writing(task_explanation(), file)
                # 写入第一题
                file_task1 = content_writing(first_task(), explanation)
                # 写入第二题
                file_task2 = content_writing(second_task(), file_task1)
                # 写入第三题
                file_task3 = content_writing(third_task(), file_task2)
                # 写入第四题
                question = random.randint(0,1)
                if question==0:
                    file_task4 = content_writing(fourth_task1(),file_task3)
                else:
                    file_task4 = content_writing(fourth_task2(),file_task3)
                file_task4.close()
