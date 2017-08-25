import requests,time, os ,random
from bs4 import BeautifulSoup
from http import cookiejar
headers = {
    "Host": "www.chsi.com.cn",
    "Referer": "http://www.chsi.com.cn/cet/",
    'User-Agent': 'ser-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36'
}
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='/home/yu/aadog/cet4cookies.txt')
name=input('姓名：')
number=input('除去座号的准考证号：')
startdog=input('起始座号：')
enddog=input('终止座号：')
dogtime=input('间隔时间：')
for intdog in range(startdog,enddog):
    if intdog<10:
        pigdog='0'+str(intdog)
    else:
        pigdog=str(intdog)
    zfc=number+pigdog
    utl='http://www.chsi.com.cn/cet/query?zkzh='+zfc+'&xm='+name
    r = session.get(utl, headers = headers )
    print (r.status_code)
    soup2 = BeautifulSoup(r.content, "html.parser")
    upsdog=soup2.find_all('div')
    dognumber=0
    for idogs in upsdog:
        dognumber=dognumber+1
        if dognumber==11:
            print(idogs.get_text())
        else:
            pass
    time.sleep(10)
    print(intdog)
    #print(upsdog)
