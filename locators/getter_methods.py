'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.myntra.com/")
time.sleep(5)
home = driver.find_element('xpath', '//a[@data-group="home"]')
print(home.text)'''

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.temu.com/")
time.sleep(5)