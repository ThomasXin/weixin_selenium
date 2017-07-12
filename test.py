# -*- coding:utf-8 -*-
from db import arcitle, keyword

for i in keyword.find({}, {'keyword': '/1/i', 'md5_sign': 1}):
    # print(i['md5_sign'], i['keyword'])
    for j in arcitle.find({'md5_sign' :str(i['md5_sign'])}):
        print(j)
        pass