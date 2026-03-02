'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://discord.com/")
time.sleep(5)
driver.find_element("link text","Nitro").click()
time.sleep(5)
driver.find_element("link text","Discover").click()
time.sleep(5)
driver.find_element("link text","Log In").click()
time.sleep(5)
driver.find_element("link text","Careers").click()
time.sleep(5)'''

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://digiyatrafoundation.com/")
time.sleep(5)
driver.find_element("link text","About").click()
time.sleep(5)
driver.find_element("link text","Privacy").click()
time.sleep(5)
driver.find_element("link text","FAQ's").click()
time.sleep(5)
driver.find_element("link text ","News").click()
time.sleep(5)'''
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
time.sleep(5)
driver.find_element("link text","Register").click()
time.sleep(5)
driver.find_element("link text","Log in").click()
time.sleep(5)








































