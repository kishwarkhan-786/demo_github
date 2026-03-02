'''import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/register")
time.sleep(2)
driver.find_element("class name","ico-register").click()
time.sleep(2)
driver.find_element("class name","ico-login").click()
time.sleep(2)
driver.find_element("class name","cart-label").click()
time.sleep(2)'''

'''import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:/Users/abc/Desktop/python%20selenium%20notes/css_selector.html')
time.sleep(2)
driver.find_element("class name","first_row").send_keys("kishwar")
time.sleep(2)
driver.find_element("class name","second_row").send_keys("khan")
time.sleep(2)
driver.find_element("class name","third_row").send_keys("uzair)")
time.sleep(2)'''

'''import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:/Users/abc/Desktop/python%20selenium%20notes/css_selector.html')
time.sleep(2)
driver.find_element("class name","first_row").send_keys("kishwar")
time.sleep(2)
driver.find_element("class name","first_row").send_keys("khan")
time.sleep(2)'''

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)
driver.find_element('class name','inputtext._58mg._5dba._2ph-').send_keys("kishwar")
time.sleep(2)
















