

# def test_login():
#     raise Exception()
# def test_signup():
#     print("signup executing")
# def test_logout():
#     print("logout executing")
# def test_add(a,b):
#     print(a+b)
# test_add(1,2)
#
# def test_login():
#     print("good morning")
# def test_login():
#     print("good evening")
# class TestSample:
#     def __init__(self):
#         pass
#     def test_login(self):
#         print("login executing")
#     def test_signup(self):
#         print("signup executing")
#     def test_logout(self):
#         print("logout executing")

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

class TestRegister:

    def test_reg(self):
        driver.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender(self):
        driver.find_element('id', 'gender-male').click()

    def test_fname(self):
        driver.find_element('id', 'FirstName').send_keys('Rohit')

    def test_lname(self):
        driver.find_element('id', 'LastName').send_keys('Shukla')

    def test_reg_email(self):
        driver.find_element('id', 'Email').send_keys('rohit@gmail.com')

    def test_reg_pwd(self):
        driver.find_element('id', 'Password').send_keys('rohit@12345')

    def test_confirm_pwd(self):
        driver.find_element('id', 'ConfirmPassword').send_keys('rohit@12345')

class Testlogin:

    def test_login(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self):
        driver.find_element('id', 'Email').send_keys('rohit@gmail.com')

    def test_login_pwd(self):
        driver.find_element('id', 'Password').send_keys('rohit@12345')



