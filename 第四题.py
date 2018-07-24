# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request as r
city=input('请输入城市（英文）')
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json
data=json.loads(data)
print('第一天18点温度')
print('temp:'+str(data['list'][2]['main']['temp']))
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('description:'+data['list'][2]['weather'][0]['description'])
print('temp_min:'+str(data['list'][2]['main']['temp_min']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))
print('温馨提示：今天有雨记得带伞')
print('第二天18点温度')
print('pressure:'+str(data['list'][10]['main']['temp']))
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('description:'+data['list'][10]['weather'][0]['description'])
print('temp_min:'+str(data['list'][10]['main']['temp_min']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))
print('温馨提示：今天晴天可出门')
print('第三天18点温度')
print('pressure:'+str(data['list'][18]['main']['temp']))
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('description:'+data['list'][18]['weather'][0]['description'])
print('temp_min:'+str(data['list'][18]['main']['temp_min']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))
print('温馨提示：多云，可能会下雨')
print('第四天18点温度')
print('pressure:'+str(data['list'][26]['main']['temp']))
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('description:'+data['list'][26]['weather'][0]['description'])
print('temp_min:'+str(data['list'][26]['main']['temp_min']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))
print('温馨提示：可出门，祝你玩得开心')
print('第五天18点温度')
print('pressure:'+str(data['list'][34]['main']['temp']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('description:'+data['list'][34]['weather'][0]['description'])
print('temp_min:'+str(data['list'][34]['main']['temp_min']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))
print('温馨提示：晴天')
tempers=[data['list'][2]['main']['temp'],
       data['list'][10]['main']['temp'],
       data['list'][18]['main']['temp'],
       data['list'][26]['main']['temp'],
       data['list'][34]['main']['temp']]
print('打印温度折线图')
print('-'*int(tempers[0]))
print('-'*int(tempers[1]))
print('-'*int(tempers[2]))
print('-'*int(tempers[3]))
print('-'*int(tempers[4]))
print('温度排序')
print(sorted(tempers))