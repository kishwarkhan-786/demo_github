'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(5)
footer_elements=driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
for ele in footer_elements:
    print(ele.text)'''

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(5)
categories=driver.find_elements('xpath','//div[@class="block block-category-navigation"]//a')
for ele in categories:
    print(ele.text)'''

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.myntra.com/")
time.sleep(5)
popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]/a')
for ele in popular_searches:
    print(ele.text)'''

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("")
time.sleep(5)
all_checkboxes=driver.find_elements('xpath','//input[@name="download"]')
for checkbox in all_checkboxes:
    checkbox.click()
    time.sleep(5)'''
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.python.org/")
time.sleep(5)
all_links = driver.find_elements("tag name", "a")
for link in all_links:
    print(link.get_attribute("href"))

























































