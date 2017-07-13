# -*- coding:utf-8 -*-
import hashlib
from db import arcitle, keyword
def query(strs):
    #  根据我们输入的关键词进行查找，必须匹配，待解决的问题就是要实现模糊查询
    for i in keyword.find({'keyword': '%s' % strs}):
        # 根据得到的标志我们要进行在控制台打印输出我们查出来的内容
        for j in arcitle.find({'md5_sign': '%s' % i.get('md5_sign')}):
            print(j.get('url'), "%s" % j.get('title'))
        return 1
def reason_star_end():
     try:
        # 这是要输入我们关键词的起始和结束的序号，如果是非数字就会结束
        start = raw_input('请输入起始位置：\n')
        end = raw_input('请输入结束位置：\n')
        # 打印输出关键字
        for items in keyword.find().skip(int(start)).limit(int(end)):
            print(items.get('keyword'))
        strs = raw_input('请客官翻牌选秀啦：\n')
        if query(strs):
            print('就这些了！！！客官不要生气')
        else:
            print('抱歉客官，您的需求我们解决不了的啦')
     except ValueError:
            print('请输入数字')
def reason_keyword():
    for items in keyword.find():
        print(items.get('keyword'))
    strs = raw_input('请客官翻牌选秀啦：\n')
    if query(strs):
        print('就这些了！！！客官不要生气')
    else:
        print('抱歉客官，您的需求我们目前没有的啦，正在给您找！')
if __name__ == '__main__':
    input_ = raw_input("请选择要查找的方式：Enter是默认，0是有范围的查询")
    if input_<>'0':
        reason_keyword()
    else:
        reason_star_end()



