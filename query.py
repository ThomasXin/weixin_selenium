# -*- coding:utf-8 -*-
import hashlib
import Queue
from run import take_md5
from db import arcitle, keyword

def query(strs):
    #  根据我们输入的关键词进行查找，必须匹配，待解决的问题就是要实现模糊查询
    for i in keyword.find({'keyword': '%s' % strs}):
        # 根据得到的标志我们要进行在控制台打印输出我们查出来的内容
        for j in arcitle.find({'md5_sign': '%s' % i.get('md5_sign')}):
            print(j.get('url'), "%s" % j.get('title'))
        return 1

def reason_keyword():
    # for items in keyword.find():
    #     print(items.get('keyword'))
    strs = raw_input('请客官翻牌选秀啦：\n')
    if query(strs):
        print('就这些了！！！客官不要生气')
    else:
        q = Queue.Queue()
        q.put(strs)
        while not q.empty():
            s = q.get()
            take_md5(s)

if __name__ == '__main__':
    reason_keyword()


