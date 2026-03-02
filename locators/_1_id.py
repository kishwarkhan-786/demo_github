import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
time.sleep(5)
driver.find_element("id","gender-male").send_keys("kishwar")
time.sleep(5)
driver.find_element("id","LastName").send_keys("khan")
time.sleep(5)
driver.find_element("id","Email").send_keys("kishwarkhan@gmail.com")
time.sleep(5)
driver.find_element("id","Password").send_keys()