import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get(r'C:\Users\abc\PycharmProjects\selenium_training\files\loading.html')
time.sleep(20)
driver.find_element('xpath', '//input[@name="fname"]').send_keys('Meghana')
time.sle
driver.find_element('xpath', '//input[@name="lname"]').send_keys('M')

