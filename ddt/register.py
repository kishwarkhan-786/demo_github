import time

from selenium import webdriver
from ddt.reading_excel import excel_data

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

data = excel_data('reg')
## {'firstname': 'Deep', 'lastname': 'Damecha', 'email_id': 'deep@gmail.com', 'password': 'deep@12345', 'confirm_pwd': 'deep@12345'}


driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(1)
driver.find_element('id', 'gender-male').click()
driver.find_element('id', 'FirstName').send_keys(data['firstname'])
driver.find_element('id', 'LastName').send_keys(data['lastname'])
driver.find_element('id', 'Email').send_keys(data['email_id'])
driver.find_element('id', 'Password').send_keys(data['password'])
driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])

