# -*- coding:utf-8 -*-
import hashlib
import time
from db import keyword, ceshi
from weixin1 import get_achieve

def take_md5():
    # 这个模块主要的作用就是我们直接从数据库中拿出待查的数据，我认为用队列可能会好一些，争取下次再改吧
    while True:
        query = ceshi.find({}, {'name':1})
        for items in query:
            print(items.get('name'))
            # 这里的MD5主要是作为两个表的标记
            get_md5 = hashlib.md5()
            get_md5.update(items.get('name'))
            md5 = get_md5.hexdigest()
            # # 这里要以MD5弄一个去重，如果MD5相等就不保存(不知道各大搜索引擎是如何去重的，好好思考一下)
            # s = set()  # 根据set的特性我们进行去重
            # for items in keyword.find({}, {'md5_sign':1}):
            #     s.add(items['md5_sign'])
            # # 这个是数据库中已存在的md5的数量
            # db_uum = len(s)
            # # 添加
            # s.add(md5)
            # # 添加之后的数量
            # add_num = len(s)
            # # 如果数量增加了表明与原来的MD5值不相等，我们再进行保存
            # if add_num > db_uum:
            #     # 保存关键字
            #     keyword.insert_one({'keyword': query, 'md5_sign': md5})
            #     # 调用weixin.py里的方法
            get_achieve(items.get('name'), md5)
if __name__ == '__main__':
    take_md5()