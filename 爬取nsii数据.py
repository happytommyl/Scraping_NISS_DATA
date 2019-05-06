from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4  import BeautifulSoup
import requests
import pandas as pd
import os
import time
import math


#设定爬虫网址
name = input("查询关键字：")
url = "http://nsii.org.cn/2017/query.php?name=" + name

# 设置查询页数
count = int(input("设置查询页数："))

# 导入浏览器驱动
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

# 切换表格界面
python_button = driver.find_element_by_id("btnTable")
python_button.click()

# 循环点击加载更多
try:
    for i in range(count): # 调整加载次数，约为总条目/10
        try: 
            button_loadmore = driver.find_element_by_id("btnLoadMore")
            button_loadmore.click()
            time.sleep(0.05)
            print(i)
        except:
            break

finally:

    # 导出数据
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find_all("table")
    
    # 保存数据
    file_handle = open('.\\result\\' + name  + '.html',mode='w',encoding='utf-8')
    
    table_text = (str(table))
    file_handle.write(table_text)

    file_handle.close()
