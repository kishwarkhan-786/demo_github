'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://saucedemo.com/")
time.sleep(5)
driver.find_element("css selector",'input[placeholder="Username"]').send_keys("standard_user")
time.sleep(3)
driver.find_element("css selector",'input[placeholder="Password"]').send_keys("secret_sauce")
time.sleep(3)
driver.find_element("css selector",'input[placeholder="Username"]').click()
time.sleep(3)'''

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://chat.qspiders.com/")
time.sleep(5)
driver.find_element("css selector",'input[id="username"]').send_keys("9924356780")
time.sleep(3)
driver.find_element("css selector",'input[d="password"]').send_keys(qsp@12345)
time.sleep(3)
driver.find_element("css selector",'input[type="submit"]').click()
time.sleep(3)''
















