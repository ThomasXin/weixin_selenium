# -*- coding:utf-8 -*-
import pymongo


client = pymongo.MongoClient('localhost', 27017)
arcitle_list = client['arcitle_list']
keyword = arcitle_list['keyword']
arcitle = arcitle_list['arcitle']