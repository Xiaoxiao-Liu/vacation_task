import http.cookiejar,urllib.request,urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
login_url = 'https://tieba.baidu.com/#'
cookie = http.cookiejar.MozillaCookieJar()
test_url = 'https://tieba.baidu.com/p/5856834725'
url = 'https://tieba.baidu.com'
user = '451095587@qq.com'
pwd = 'Liuxiaoxiao'
values = {
    'userName':'smile1020笑',
    'password':'Liuxiaoxiao',
}
#douban:Liuxiaoxiao5678
postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
headers = {'User-Agent':user_agent, 'Connection':'keep-alive'}

cookie_file = 'cookie.txt'
cookie_aff = http.cookiejar.MozillaCookieJar(cookie_file)
handler = urllib.request.HTTPCookieProcessor(cookie_aff)
opener = urllib.request.build_opener(handler)
request = urllib.request.Request(login_url, postdata, headers)
try:
    response = opener.open(request)
    response = urllib.request.urlopen(request, timeout=1)
    #print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard=True, ignore_expires=True)

for item in cookie_aff:
    print('Name ='+ item.name)
    print('Value ='+ item.value)
#使用cookie登陆get_url
get_request = urllib.request.Request(test_url,headers=headers)
get_response = opener.open(get_request)
print(get_response.read().decode())