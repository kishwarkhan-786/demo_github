import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\abc\PycharmProjects\selenium_training\files\demo.html')
time.sleep(2)

listbox = driver.find_element('xpath', '//select[@id="standard_cars"]')
select_obj = Select(listbox)


select_obj.select_by_index(6)
time.sleep(2)
select_obj.select_by_index(3)
time.sleep(2)
select_obj.select_by_index(9)
time.sleep(2)
select_obj.select_by_index(2)
time.sleep(3)
select_obj.select_by_index(20)
time.sleep(10)

# select_obj.select_by_value("bmw")
# time.sleep(2)
# select_obj.select_by_value("lr")
# time.sleep(2)
# select_obj.select_by_value("toy")
# time.sleep(2)
# select_obj.select_by_value("Audi")









