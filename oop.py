#encoding:utf-8

from urllib import request
import urllib.error
url = 'http://www.baidu.com/'
website = url.split('//')[1]
#print(website)
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
        headers = {'User-Agent': ua,
                   'Host':website
                       }
        response1 = request.urlopen(url,timeout=2)
        print('ok')
        print(response1.read().decode('gbk'))
    except urllib.error.URLError as e:
        print(e)

#print(response1.read().decode('utf-8'))
import http.cookiejar
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
filename = 'cookie.txt'
#url = 'https://www.baidu.com'
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
#print(cookie)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response2 = opener.open('https://www.baidu.com')
#response2 = urllib.request.urlopen("http://www.baidu.com")
print(response2.read().decode('utf-8'))
