# import time

# from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# class Locators:
#
#     reg_link = 'xpath', '//a[text()="Register"]'
#     gender_btn = 'id', 'gender-male'
#     firstname = 'id', 'FirstName'
#     lastname = 'id', 'LastName'
#     email = 'id', 'Email'
#     password = 'id', 'Password'
#     confirm_pwd = 'id', 'ConfirmPassword'
#
# loc = Locators()
#
#
# class DemoWebShop:
#
#     def click_on_reg(self):
#         # driver.find_element('xpath', '//a[text()="Register"]').click()
#         driver.find_element(*loc.reg_link).click()
#         ## driver.find_element(('xpath', '//a[text()="Register"]')).click()
#         ## driver.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(1)
#
#     def click_gender_btn(self):
#         # driver.find_element('id', 'gender-male').click()
#         driver.find_element(*loc.gender_btn).click()
#
#     def enter_fname(self):
#         # driver.find_element('id', 'FirstName').send_keys('Rohit')
#         driver.find_element(*loc.firstname).send_keys('Rohit')
#
#     def enter_lname(self):
#         # driver.find_element('id', 'LastName').send_keys('Shukla')
#         driver.find_element(*loc.lastname).send_keys('Shukla')
#
#     def enter_reg_email(self):
#         # driver.find_element('id', 'Email').send_keys('rohit@gmail.com')
#         driver.find_element(*loc.email).send_keys('rohit@gmail.com')
#
#     def enter_reg_pwd(self):
#         # driver.find_element('id', 'Password').send_keys('rohit@12345')
#         driver.find_element(*loc.password).send_keys('rohit@12345')
#
#     def enter_confirm_pwd(self):
#         # driver.find_element('id', 'ConfirmPassword').send_keys('rohit@12345')
#         driver.find_element(*loc.confirm_pwd).send_keys('rohit@12345')

##############################################################################################

import time

from selenium import webdriver
from method_driven.locators import Locators

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

loc = Locators()

class DemoWebShop:

    def click_on_reg(self):
        driver.find_element(*loc.reg_link).click()
        time.sleep(1)

    def click_gender_btn(self):
        driver.find_element(*loc.gender_btn).click()

    def enter_fname(self):
        driver.find_element(*loc.firstname).send_keys('Rohit')

    def enter_lname(self):
        driver.find_element(*loc.lastname).send_keys('Shukla')

    def enter_reg_email(self):
        driver.find_element(*loc.email).send_keys('rohit@gmail.com')

    def enter_reg_pwd(self):
        driver.find_element(*loc.password).send_keys('rohit@12345')

    def enter_confirm_pwd(self):
        driver.find_element(*loc.confirm_pwd).send_keys('rohit@12345')

demo = DemoWebShop()
demo.click_on_reg()
demo.click_gender_btn()
demo.enter_fname()
demo.enter_lname()
demo.enter_reg_email()
demo.enter_reg_pwd()
demo.enter_confirm_pwd()


















































