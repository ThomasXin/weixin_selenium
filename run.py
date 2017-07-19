# -*- coding:utf-8 -*-
import hashlib
from db import keyword, arcitle
from weixin import get_achieve

def take_md5(query):
    # 这里的MD5主要是作为两个表中相对应的标记
    get_md5 = hashlib.md5()
    get_md5.update(query)
    md5 = get_md5.hexdigest()
    # 这里要以MD5弄一个去重，如果MD5相等就不保存(不知道各大搜索引擎是如何去重的，好好思考一下)
    s = set()  # 根据set的特性我们进行去重
    for items in keyword.find({}, {'md5_sign':1}):
        s.add(items['md5_sign'])
    # 这个是数据库中已存在的md5的数量
    db_uum = len(s)
    # 添加
    s.add(md5)
    # 添加之后的数量
    add_num = len(s)
    # 如果数量增加了表明与原来的MD5值不相等，我们再进行保存
    if add_num > db_uum:
        # 保存关键字
        keyword.insert_one({'keyword': query, 'md5_sign': md5})
        # 调用weixin.py里的方法
        get_achieve(query, md5)
        # for items in arcitle.find({'md5_sign':'%s'% md5}):
        #     print(items)
        num = 0
        for items in arcitle.find({'md5_sign': '%s' % md5}):
            num += 1
        if num < 1:
            keyword.remove({'md5_sign': '%s' % md5})


