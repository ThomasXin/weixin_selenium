# -*- coding:utf-8 -*-

import requests
import json
import re
import random
import time
import hashlib
from db import keyword, arcitle
# 将cookies从文件中读取出来
with open('cookies.txt', 'r') as file:
    cookie = file.read()
cookies = json.loads(cookie)
url = 'https://mp.weixin.qq.com/'
response = requests.get(url, cookies=cookies)
token = re.findall(r'token=(\d+)', str(response.url))[0]
def get_achieve(query, md5):

    data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'url': query,
        'begin': '0',
        'count': '3'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.7 Safari/537.36',
        'Referer':'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&share=1&type=10&lang=zh_CN&token=295055052',
        'Host': 'mp.weixin.qq.com'
     }
    search_url = 'https://mp.weixin.qq.com/cgi-bin/operate_appmsg?sub=check_appmsg_copyright_stat'
    search_response = requests.post(search_url, cookies=cookies, data=data, headers=headers)

    max_num = search_response.json().get('total')  # 获取总条数
    num = int(int(max_num/3))  # 获取总页数
    begin = 0
    while num + 1 > 0:
        data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'url': query,
        'begin': '{}'.format(str(begin)),
        'count': '3'
    }
        search_response = requests.post(search_url, cookies=cookies, data=data, headers=headers)

        content = search_response.json().get('list')
        for items in content:
            print items.get('title'), items.get('url')
            arcitle.insert_one({'title': items.get('title'), 'url': items.get('url'), 'md5_sign': md5})
        num -= 1
        begin = int(begin)
        begin += 3
        time.sleep(5)

