# -*- coding:utf-8 -*-
from db import arcitle, keyword

def query(strs):
    """这是一个待解决的问题"""
    for i in keyword.find({}, { 'title': strs}):
        print(i)
        # for j in arcitle.find({'md5_sign': str(i['md5_sign'])}):
        #     print(j)
        #     pass
if __name__ == '__main__':
    strs = raw_input('请输入要查询的内容：\n')
    query(strs)