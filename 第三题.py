# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:17:07 2018

@author: 安以陌
"""

import urllib.request as r
import json
data = r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=suzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
data = json.loads(data)
temp = data['main']['temp']
description = data['main'][0]['description']
pressure = data['main']['pressure']
print('suzhou: ' + str(temp) + '°C' + description + ' ' + str(pressure))