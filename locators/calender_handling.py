import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.goibibo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath",'//span[@class="logSprite icClose"]').click()
time.sleep(5)
driver.find_element("xpath",'//span[text()="Departure"]').click()
time.sleep(5)


while True:
    month=driver.find_element('xpath','//div[@class="DayPicker-Caption"])')
    print(month.text)

    if month.text=='October 2026':
        driver.find_element('xpath','//p[text()="15"]').click()
        break
    else:
        driver.find_element("xpath",'//span[@aria-label="Next Month"]').click()