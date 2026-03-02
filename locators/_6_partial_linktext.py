'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
time.sleep(5)
driver.find_element("partial link text","Books").click()
time.sleep(5)
driver.find_element("partial link text","Computers").click()
time.sleep(5)'''

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://kushal.com/")
time.sleep(5)
driver.find_element("partial link text","")















