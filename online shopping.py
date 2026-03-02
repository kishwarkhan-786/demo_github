

import time
from selenium import webdriver
opts=webdriver.EdgeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Edge(opts)
driver.get("https://www.myntra.com")
time.sleep(10)
driver.maximize_window()
time.sleep(10)
driver.minimize_window()
time.sleep(15)
driver.back()
time.sleep(15)
driver.forward()
time.sleep(15)
driver.refresh()





