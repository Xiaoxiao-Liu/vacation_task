#encoding:utf-8
import random
import pandas as pd
import os
import re

text = open("./data.txt",'r',encoding = 'utf-8').read()
#content = list(map(lambda y: y.strip(), filter(lambda l: len(l.strip()) != 0, novel)))
#start =random.randint(0,len(content)-15)
#end = start + 10
#block = "'''" + "\n".join(content[start:end + 1]) + "'''"
print(text)
# 　匹配邮箱地址
regex_mail = r'\s*[\w]+@[\w]+.[\w]+'
mail = re.findall(regex_mail,text)
print(mail)
# 匹配手机号
regex_phone = r'[\d]{11}|0[\d]{2,3}-+[\d-]{4,8}'
phone = re.findall(regex_phone,text)
print(phone)
