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
    f.write('# 任务四\n')
    #f.close()
    return f


def task_explanation():
    text_1 = "本次任务旨在练习正则表达式，因此不可以使用其他检索方式进行关键词匹配"+'\n'
    text_2 = "在完成本次任务时，建议大家多对照正则表达式表格进行练习，认真思考，"+'\n'
    text_3 = "结合自己的逻辑，完成任务。\n"
    text_4 = "注意：本任务的得分将按照任务提交时间的先后顺序与任务正确率结合来计算，\n"
    #text_5 = "完成本次任务时，不得使用任何第三方软件，不能import任何第三方库"
    text_6 = "由于每位同学的题目都不相同，建议不要抄袭，一旦发现抄袭情况，本次任务判为0分'''\n"
    text = "'''\n" + text_1 + text_2+ text_3 + text_4 +text_6+'\n'
    return text


def content_writing(text,f):
    f.write(text)
    return f


def questions_generation(df,quiz,i):
    annotation = '# 第{}题\n'.format(i)
    #print(annotation)
    question = '#要求：{}\n'.format(list(df.iloc[quiz:quiz+1]['question'])[0])
    #print(question)
    text = '#文本：{}'.format(list(df.iloc[quiz:quiz+1]['text'])[0])

    contents = annotation+question+text+'\n'*5
    return contents



def first_task():
    df = pd.DataFrame(pd.read_excel('regex_quiz.xlsx'))
    quiz_nos = random.sample(range(len(df['question'])),5)
    #print(type(quiz_nos[0]))
    i=0
    contents = ''
    for quiz in quiz_nos:
        i+=1
        contents += questions_generation(df, quiz,i)
    #print(contents)

    return contents


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
                stu_no = stu_nos[i]
                stu_name = stu_names[i]
                # 创建文件
                file = file_creating(stu_no, stu_name, class_path)
                # 写入注释
                explanation = content_writing(task_explanation(), file)
                # 写入第一题
                file_task1 = content_writing(first_task(), explanation)


