#coding:utf8
__author__ = 'liyatao'
#python selenium模拟登录知乎 ,将chromedriver.exe文件放到C:\Python27\Scripts 目录下，这样下面填的时候就不用填绝对地址，因为已经在环境变量中
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('chromedriver.exe') #chromedriver.exe的地址，因为添加到了环境变量，所以不用填绝对地址
driver.get("https://www.zhihu.com/signup")

login=driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span').click()

username=driver.find_element_by_name('username')
username.clear()
username.send_keys('xxx') #xxx为用户名

password=driver.find_element_by_name('password')
password.send_keys('xxx')  #xxx为密码

driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button').click()

# driver.close()
