'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get('C:/Users/abc/Desktop/python%20selenium%20notes/css_selector.html')
time.sleep(5)
driver.find_element('tag name','input').send_keys("kishwar")
time.sleep(5)
driver.find_element('tag name','input').send_keys("khan")
time.sleep(5)'''

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(5)
driver.find_element("tag name","input").send_keys("kishwar")
time.sleep(5)
driver.find_element("tag name","input").send_keys("khan")
time.sleep(5)






