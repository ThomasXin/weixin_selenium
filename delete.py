# -*- coding:utf-8 -*-
from db import arcitle, keyword
def delete(strs):
     #  根据我们输入的关键词进行删除
    for i in keyword.find({'keyword': '%s' % strs}):
        arcitle.remove({'md5_sign': '%s' % i.get('md5_sign')})
        keyword.remove({'keyword': '%s' % strs})
    print('已经移除---%s---相关信息' % strs)

if __name__ == '__main__':
    strs = raw_input('请输入要删除的关键词')
    delete(strs)
