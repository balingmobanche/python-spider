from scrapy import cmdline
from selenium import webdriver

from time import sleep

# cmdline.execute("scrapy crawl quotes".split())
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome(executable_path="D:\chromdriver\chromedriver.exe")
#2.通过浏览器向服务器发送URL请求
browser.get("https://www.weibo.com")
sleep(10)
browser.find_element_by_css_selector("#loginname").send_keys(
            "1329727778@qq.com")
browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys(
            "201201011853@3")
sleep(20)
browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
sleep(30)
browser.close()






