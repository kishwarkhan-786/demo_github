# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# ac.send_keys(Keys.END).perform()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(3)
# def handling_windows():
#     return driver.window_handles
#
# parent_window = handling_windows()[0]
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)     ## driver.switch_to.window(child_window)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys('Google pixel')
#         time.sleep(2)
#
# driver.switch_to.window(parent_window)
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="YouTube"]').click()
# time.sleep(2)
#
# for handle_ in handling_windows():
#     driver.switch_to.window(handle_)
#     if 'youtube' in driver.current_url:
#         driver.find_element('xpath', '//input[@name="search_query"]').send_keys('python selenium')
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(2)
parent_handle = driver.current_window_handle        ##

home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
ac.move_to_element(home).perform()          ## hovering to home
time.sleep(2)
driver.find_element('xpath', '//a[text()="Festive Decor"]').click()
time.sleep(2)
driver.find_element('xpath', '//h4[@class="product-product"]').click()      ## opens in a new tab
time.sleep(2)











































