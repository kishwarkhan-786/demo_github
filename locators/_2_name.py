###EG1
'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element("name","username").send_keys("kishwarjaafarkhan@gamil.com")
time.sleep(5)
driver.find_element("name","password").send_keys("aicte@786")
time.sleep(5)'''

##EG2

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(5)
driver.find_element("name","emailOrPhone").send_keys("kishwarjaafarkhan@gmail.com")
time.sleep(5)
driver.find_element("name","password").send_keys("aicte@786")
time.sleep(5)
driver.find_element("name","fullName").send_keys("kishwar khan")
time.sleep(5)
driver.find_element("name","username").send_keys("kishwarkhan34")
time.sleep(5)'''
##EG3
'''
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get(r"C:\Users\abc\PycharmProjects\selenium_training\files\css_selector.html")
time.sleep(5)
driver.find_element("name","fname").send_keys("kishwar")
time.sleep(5)
driver.find_element("name","fname").send_keys("khan")
time.sleep(5)'''

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.instagram.com/")
time.sleep(2)


















































