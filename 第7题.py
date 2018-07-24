# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:41:20 2018

@author: 安以陌
"""

import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json
data=json.loads(data)

def judge():
    for i in range(2,36,8):
        print('pressure:'+str(data['list'][i]['main']['pressure']))
        print('description:'+data['list'][i]['weather'][0]['description'])
        print('temp_min:'+str(data['list'][i]['main']['temp_min']))
        print('temp_max:'+str(data['list'][i]['main']['temp_max']))
        if data['list'][i]['main']['temp']>27:
            print('天气炎热，注意防暑')
        elif data['list'][i]['main']['temp']>25:
            print('注意防晒')
        elif data['list'][i]['main']['temp']>20:
            print('可出门')
judge()  


def sale():
    for i in range(0,36):
        print('商品描述:'+data['mods']['itemlist']['data']['auctions'][i]['title'])
        print('价格:'+data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        print('地区:'+data['mods']['itemlist']['data']['auctions'][i]['item_loc'])
        print('nick:'+data['mods']['itemlist']['data']['auctions'][i]['nick'])
        if int(data['mods']['itemlist']['data']['auctions'][i]['view_sales'][:-3])>5000:
            print('销量很好')
        elif int(data['mods']['itemlist']['data']['auctions'][i]['view_sales'][:-3])>2000:
            print('销量还行')
        elif int(data['mods']['itemlist']['data']['auctions'][i]['view_sales'][:-3])>100:
            print('销量很差')
sale()        