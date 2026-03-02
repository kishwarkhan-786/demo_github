import time

from selenium import webdriver
from reading_excel import excel_data

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

data = excel_data("login")

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element('xpath', '//a[text()="Log in"]').click()
time.sleep(1)
driver.find_element('id', 'Email').send_keys(data['email_id'])
driver.find_element('id', 'Password').send_keys(data['password'])




