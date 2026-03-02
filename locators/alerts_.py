import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/" )
time.sleep(5)
driver.find_element('xpath','//button[text()="Simple Alert"]').click()
time.sleep(5)
alert_obj=driver.swich_to_.alerts