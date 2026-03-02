'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
time.sleep(5)
ele1=driver.find_element('xpath','(//a[contains(text(), "Books")])[1]')
print(ele1.is_displayed())
ele2=driver.find_element('xpath','(//a[contains(text(), "Books")])[2]')
print(ele2.is_displayed())'''

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
time.sleep(5)
ele1=driver.find_element("xpath",'//input[@id="gender-male"]')
ele2=driver.find_element('xpath','//input[@id="gender-female"]')
ele1.click()
print(ele1.is_selected())
print(ele2.is_selected())'''

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(5)
