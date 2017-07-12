# -*- coding:utf-8 -*-
import time
import json
from selenium import webdriver

driver = webdriver.Chrome()  # 谷歌浏览器(谷歌驱动放在python根目录下)
#  需要爬取的目标登录页面
driver.get('https://mp.weixin.qq.com/')
#  获取到用户名输入框并设置为焦点
driver.find_element_by_xpath('//*[@id="account"]').clear()
#  在用户名输入框输入账号
driver.find_element_by_xpath('//*[@id="account"]').send_keys('username')
time.sleep(2)
# 以下两条同上
driver.find_element_by_xpath('//*[@id="pwd"]').clear()
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('password')
time.sleep(2)
#  选择记住账号
driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/label').click()
time.sleep(2)
#  点击登录
driver.find_element_by_xpath('//*[@id="loginBt"]').click()
time.sleep(15)
# 获取登录后的cookies(我们要的就是这个，下次直接带上，不用登录)
cookies = driver.get_cookies()

cookie = {}
for items in cookies:
    cookie[items.get('name')] = items.get('value')
with open('cookies.txt', 'w') as file:
    file.write(json.dumps(cookie))  # 写入转成字符串的字典
driver.close()