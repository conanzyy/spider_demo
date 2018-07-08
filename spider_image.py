#coding:utf-8
import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import re
import time
import http.cookiejar


total = '123' + \
        '456' + \
        '789'

print ('total:%s' % total)

# url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1527833312292_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3"
url = "https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&tab=album"


#第一种网页下载方法
html1 = urllib.request.urlopen(url).read()
soup1 = BeautifulSoup(html1, 'html.parser',from_encoding="utf-8")
print ("长度1:%d" % len(html1))

#第二种网页下载方法
request = urllib.request.Request(url)
request.add_header("user-agent","Mozilla/5.0") #用户代理，伪装为一个浏览器
html2 = urllib.request.urlopen(url).read()
soup2 = BeautifulSoup(html2, 'html.parser',from_encoding="utf-8")
print ("长度2:%d" % len(html2))

#第三种网页下载方法
cj = http.cookiejar.CookieJar()  #创建一个cookie的容器cj
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器;自定义一个opener,并将opener跟CookieJar对象绑定
urllib.request.install_opener(opener)#安装opener,此后调用urlopen()时都会使用安装过的opener对象
html3 = urllib.request.urlopen(url).read()
soup3 = BeautifulSoup(html3, 'html.parser',from_encoding="utf-8")
print ("长度3:%d" % len(html3))

# print(soup.prettify())

# 用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句
links = soup1.find('div',class_ = "imgpage")
links1 = soup1.find_all('img',src = re.compile(r'https://imgsa.baidu.com/forum/'))
links2 = soup2.find_all('img',src = re.compile(r'https://imgsa.baidu.com/forum/'))
links3 = soup3.find_all('img',src = re.compile(r'https://imgsa.baidu.com/forum/'))

# 设置保存图片的路径，否则会保存到程序当前路径
path = r'/Users/MRsYang/Desktop/image/'

fout = open('output_image.html', 'w')
fout.write("<html>")
fout.write("<body>")
fout.write("<table border='1' word-break:break-all cellspacing='0' cellpadding='0' style='table-layout:fixed; width:100%;height:100%'>")
fout.write("<tr>")
fout.write("<th>url</th>")
 # fout.write("<th>标题</th>")
fout.write("<th>图片</th>")
fout.write("</tr>")

for link in links1:
    img_url = link.attrs['src']
    # 保存链接并命名，time.time()返回当前时间戳防止命名冲突
    # urllib.urlretrieve(img_url, path + '%s.jpg' % time.time())  # 使用request.urlretrieve直接将所有远程链接数据下载到本地
    print ("img_url:%s"%img_url)

    fout.write("<tr>")
    fout.write("<td style='width:30%%; WORD-WRAP: break-word; word-break:break-all'>%s</td>" % img_url)
    # fout.write("<td style='width:10%%; WORD-WRAP: break-word; word-break:break-all'>%s</td>" % data['title'].encode("utf-8"))
    fout.write("<td style='width:70%%;'><img src='%s'></td>" % img_url)
    fout.write("</tr>")

fout.write("</table>")
fout.write("</body>")
fout.write("</html>")
fout.close()


