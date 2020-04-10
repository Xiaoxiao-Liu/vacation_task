#encoding:utf-8
import os
#import urllib.request
from urllib import request
import urllib.parse
import urllib.error
import ssl
import pandas as pd
import socket
import http.cookiejar
import random

# Create files
def file_creating(stu_no, stu_name,class_path):
    file_name = class_path+stu_no+'_'+stu_name+'.py'
    f = open(file_name,'w')
    f.write('# 任务三\n')
    #f.close()
    return f

def task_explanation():
    text_1 = "在完成本次任务中，不可使用urllib外的爬虫库"+'\n'
    text_2 = "在完成本次任务时，建议大家多思考，多检索，学会借助百度、python官方文档等工具查找方法，"+'\n'
    text_3 = "同时结合自己的逻辑，完成任务。\n"
    text_4 = "注意：本任务的得分将按照任务提交时间的先后顺序与任务正确率结合来计算，\n"
    #text_5 = "完成本次任务时，不得使用任何第三方软件，不能import任何第三方库"
    text_6 = "由于每位同学的题目都不相同，建议不要抄袭，一旦发现抄袭情况，本次任务判为0分'''\n"
    text = "'''\n" + text_1 + text_2+ text_3 + text_4 +text_6+'\n'
    return text


def content_writing(text,f):
    f.write(text)
    return f

def first_task(url):
    headers = ''
    annotation = '# 第一题 '
    url  = url
    contents = '给定如下url地址：%s，请使用此地址向服务器发送请求，并获取网页源码信息。'%(url)
    notes = '# 注意：如果无法请求成功，请自行修改，或尝试捕获异常，并用自己的话解释异常原因。'
    exceptions = '#第二题 以上方法是否请求成功，如未请求到结果，请解释异常原因：'
    headers = '''user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
        ] # 以上是你可以使用的user agent'''
    text = annotation+contents+'\n' +notes +'\n' +headers+'\n'*5+exceptions
    return text

def get_url():
    df = pd.DataFrame(pd.read_excel('websites.xlsx'))
    websites = list(df['网址'])
    random.shuffle(websites)
    print(websites)
    #url = random.choice(websites)
    return websites


def visit_website(url):

    url = urllib.parse.quote(url, ':/=&?')
    ssl._create_default_https_context = ssl._create_unverified_context
    socket.setdefaulttimeout(30.0)
    #url = 'https://book.douban.com/'
    website = url.split('//')[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
               'Host': website}
    try:
        response = request.Request(url=url,headers=headers)
        page = request.urlopen(response,timeout=1)
        #print(page.read().decode('utf-8'))
        #print(response.read().decode('utf-8')) #response.read()获取响应内容
    except urllib.error.URLError as e:
        user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
        ]
        for ua in user_agents:
            try:
                response = request.Request(url=url, headers=headers)
                page = request.urlopen(response, timeout=1)
                print('this ua work:',ua)
            except:
                print("header is no use:")
        print("There is something wrong:",url)
        print(e)

def get_cookie():
    ssl._create_default_https_context = ssl._create_unverified_context
    filename = 'cookie.txt'
    url = 'https://www.baidu.com'
    cookie = http.cookiejar.MozillaCookieJar()
    # print(cookie)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    cookie.save(filename, ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':

    excelFiles = os.listdir('./classes/')
    for f in excelFiles:
        if f == '.DS_Store':
            continue
        else:
            websites = get_url()
            df = pd.DataFrame(pd.read_excel('./classes/' + f))
            class_path = './classes/' + f[3:9] + '/'
            os.mkdir(class_path)
            stu_nos = list(df['学号'])
            stu_names = list(df['姓名'])
            for i in range(len(stu_nos)):
                url = websites[i]
                # print(stu_nos[i])
                # print(stu_names[i])
                stu_no = stu_nos[i]
                stu_name = stu_names[i]
                # 创建文件
                file = file_creating(stu_no, stu_name, class_path)
                # 写入注释
                explanation = content_writing(task_explanation(), file)
                # 写入第一题
                file_task1 = content_writing(first_task(url), explanation)
                







