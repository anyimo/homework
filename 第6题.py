# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:46:05 2018

@author: 安以陌
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
def shop(a):
    print('商品描述:'+data['mods']['itemlist']['data']['auctions'][a]['title'])
    print('价格:'+data['mods']['itemlist']['data']['auctions'][a]['view_price'])
    print('地区:'+data['mods']['itemlist']['data']['auctions'][a]['item_loc'])
    print('nick:'+data['mods']['itemlist']['data']['auctions'][a]['nick'])
    print('')
for i in range(0,36):
    shop(i)
    if (i+1)%4==0 :
            print('##############')
        
                
def price(b):
    return float(data['mods']['itemlist']['data']['auctions'][b]['view_price'])

lists=[]
for x in range (0,36):
    lists.append(price(x))

print('价格倒序')
sorted(lists,reverse=True)


def sale(c):
    return int(data['mods']['itemlist']['data']['auctions'][c]['view_sales'][:-3])
list=[]
for y in range(0,36):
    list.append(sale(y))
print('销量排序')
sorted(list,reverse=True)
