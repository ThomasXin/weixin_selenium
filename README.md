﻿# weixin_selenium
* 此小爬虫是爬取微信公众号内的素材管理/新建分享图文中的文章。
* login.py 是你第一次登录微信公众号时需要用到的，目的是为了拿到cookies.txt里的cookies。
* weixin.py就是我们要做的内容，
* query.py 根据关键词进行查找。知道了article库中有什么类型数据  
* db.py 是与数据库相关的
* 小爬虫用到的库的版本及系统
	0.win764位
	1.Python 2.7.13
	2.selenium (3.4.3)
	3.pymongo (3.4.0)
	4.数据库位Mongodb
* 第一次用selenium，感觉还不错，用到的驱动是谷歌驱动下载链接在这里 链接：http://pan.baidu.com/s/1qYWahI0 密码：d5pl。 直接放在python根目录下如：D:\python2.7/chromedriver.exe
* 第一次会用模拟登陆和selenium，还需要多多练习啊
