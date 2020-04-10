#encoding:utf-8
import urllib.request,urllib.error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
try:
    url = 'http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1585554557&di=52cd280e4e7a678410c3395f4f68366e&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Fbeilanpin2.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request,timeout=1)
    contents = response.read()
    file_name = 'image.png'
    with open(file_name,'wb') as file:
        file.write(contents)



except urllib.error.URLError as e:
    print(e.reason)




