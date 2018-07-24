# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:52:38 2018

@author: 安以陌
"""

    

for i in range(0,100):
    try:
        s=44*i
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=0&p4ppushleft=1%2C48&style=grid&loc=%E6%97%A0%E9%94%A1&ajax=true&s={}'
        import urllib.request as r
        data=r.urlopen(url.format(s)).read().decode('utf-8','ignore')
        import json
        data=json.loads(data)
        def shop(a):
            return data['mods']['itemlist']['data']['auctions'][a]['title'];
        def price(b):
            return data['mods']['itemlist']['data']['auctions'][b]['view_price'];
        def loc(c):
            return data['mods']['itemlist']['data']['auctions'][c]['item_loc'];
        for x in range (0,44):   
            f=open('xihuan.txt','a',encoding='utf-8')
            f.write('商品描述:'+str(shop(x)+'商品价格:'+str(price(x))+'发货地:'+str(loc(x))))
            f.close
        f.write('\n')
        print('第'+str(i+1)+'页爬取成功')
    except Exception as err:
        print('爬取异常')
        
m=open('tmp.txt',encoding='utf-8')
data=m.read()
import json
data=json.loads(data) 
def shop(a):
    print('商品描述:'+data['mods']['itemlist']['data']['auctions'][a]['title'])
    print('价格:'+data['mods']['itemlist']['data']['auctions'][a]['view_price'])
    print('地区:'+data['mods']['itemlist']['data']['auctions'][a]['item_loc'])
    print('nick:'+data['mods']['itemlist']['data']['auctions'][a]['nick'])
for i in range (0,4):
    shop(i)
