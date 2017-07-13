# -*- coding:utf-8 -*-
from db import arcitle, keyword
def delete(strs):
     #  根据我们输入的关键词进行删除
    for i in keyword.find({'keyword': '%s' % strs}):
        arcitle.remove({'md5_sign': '%s' % i.get('md5_sign')})
        keyword.remove({'keyword': '%s' % strs})


if __name__ == '__main__':
    strs = raw_input('lalallalllalalla')
    delete(strs)
