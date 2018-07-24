# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:16:25 2018

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
shop(0)
shop(1)
shop(2)
shop(3)
print('#########################')
shop(4)
shop(5)
shop(6)
shop(7)
print('#########################')      
shop(8)
shop(9)
shop(10)
shop(11)
print('#########################') 
shop(12)
shop(13)
shop(14)
shop(15)
print('#########################')
      
def price(b):
    return float(data['mods']['itemlist']['data']['auctions'][b]['view_price'])

lists=[price(0),price(1),price(2),price(3),price(4),price(5),price(6),price(7),price(8),
       price(9),price(10),price(11),price(12),price(13),price(14),price(15),price(16),price(17),
       price(18),price(19),price(20),price(21),price(22),price(23),price(24),price(25),price(26),
       price(27),price(28),price(29),price(30),price(31),price(32),price(33),price(34),price(35)]
print('价格倒序')
sorted(lists,reverse=True)


def sale(c):
    return int(data['mods']['itemlist']['data']['auctions'][c]['view_sales'][:-3])
list=[sale(0),sale(1),sale(2),sale(3),sale(4),sale(5),sale(6),sale(7),sale(8),
       sale(9),sale(10),sale(11),sale(12),sale(13),sale(14),sale(15),sale(16),sale(17),
       sale(18),sale(19),sale(20),sale(21),sale(22),sale(23),sale(24),sale(25),sale(26),
       sale(27),sale(28),sale(29),sale(30),sale(31),sale(32),sale(33),sale(34),sale(35)]
print('销量排序')
sorted(list,reverse=True)




