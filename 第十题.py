# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:24:39 2018

@author: 安以陌
"""


ls=open('广东招生人数.txt',encoding='gbk').readlines()
schoolls=[]
for line in ls:
    schoolls.append(line.split(',')[0].split('(')[1])
    
for schoollid in schoolls:    
    f=open('学校.txt','a+',encoding='utf-8')
    f.write(str(schoollid)+','+"\n")

    
    
ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]
for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400',
'X-Requested-With':'XMLHttpRequest'}
f=open('海南招生人数.txt','a',encoding='utf-8')
for schoollid in schoolls:
    for kemu in [1,2]:
        try:
            req=r.Request(url,data='id={}&type={}&city=46&state=1'.format(schoollid,kemu).encode(),headers=headers)
            f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
            print('学校'+schoollid +'在海南招生人数')
            f.close()
        except Exception  as err:
            print('学校'+schoollid +'爬取错误')




import re
ms=open('XML高考派城市.txt',encoding='utf-8').readlines()
cities=[]
for line in ls:
    cities.append(re.findall(r"[0-9]\d*",line)[1])
for cityid in cities:
    f=open('所有城市id.txt','a+',encoding='utf-8')
    f.write(cityid+"\n")