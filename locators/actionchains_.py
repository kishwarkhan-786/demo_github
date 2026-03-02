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
# ac_obj = ActionChains(driver)
# driver.get("https://www.myntra.com/")
# time.sleep(3)
# men = driver.find_element('xpath', '(//a[text()="Men"])[1]')
# ac_obj.move_to_element(men).perform()
# time.sleep(2)
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
# kids = driver.find_element('xpath', '(//a[text()="Kids"])[1]')
# ac_obj.move_to_element(kids).perform()
# time.sleep(2)
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac_obj.move_to_element(home).perform()
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
# ac_obj = ActionChains(driver)
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(3)
# ele1=driver.find_element('xpath','//button[text()="Copy Text"]')
# ac_obj.double_click(ele1).perform()
# time.sleep(4)
#
# ele2 = driver.find_element('xpath', '//label[text()="Name:"]')
# ac_obj.double_click(ele2).perform()
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(3)
# ac_obj.context_click().perform()
# time.sleep(3)
# ele=driver.find_element('xpath','//h2[text()="Dynamic Button"]')
# ac_obj.context_click(ele).perform()
# time.sleep(4)




import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

# ele = driver.find_element('xpath', '//a[text()=" ONLINE SHOPPING "]')
# ac_obj.scroll_to_element(ele).perform()
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.HOME).perform()

# ele = driver.find_element('xpath', '//a[text()=" ONLINE SHOPPING "]')
# driver.execute_script("arguments[0].scrollIntoView();", ele)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(4)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(3)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(3)
#


driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)

ele=driver.find_element("xpath", '//h2[text()="Scrolling DropDown"]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(4)
slider=driver.find_element('xpath','//div[@id="slider-range"]')
ac_obj.click_and_hold(slider).move_by_offset(100, 0).release().perform()
time.sleep(2)
ac_obj.click_and_hold(slider).move_by_offset(-100, 0).release().perform()
time.sleep(2)
























