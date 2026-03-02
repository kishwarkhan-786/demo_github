import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
from openpyxl import Workbook
Workbook=Workbook()
worksheet=Workbook.active
worksheet.title="login_info"
worksheet["A1"]="username"
worksheet["B1"]="password"
worksheet["A2"]="standard_user"
worksheet["B2"]="secret_sauce"

driver.get("https://www.saucedemo.com/")
time.sleep(3)
driver.find_element('id','user-name').send_keys("standard_user")
time.sleep(3)
driver.find_element('id','password').send_keys("secret_sauce")
time.sleep(3)
driver.find_element('id','login-button').click()
time.sleep(4)
Workbook.save("A15_candidates.xlsx")
Workbook.save(r'C:\Users\abc\PycharmProjects\selenium_training\files\A15.xlsx')

try:
    success_msg=driver.find_element('id','login-button').click()
    print("login SUCCESSFUL")
except:
    print("login FAILED")
    driver.quit()