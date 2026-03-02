import time
import pytest

from selenium import webdriver

@pytest.fixture(scope='class', params=['chrome', 'firefox', 'edge'])
def setup(request):
    parameter = request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()

    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()

## driver --> webdriver.Chrome(opts)
## setup --> webdriver.Chrome(opts)


class TestRegister:

    def test_reg(self, setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender(self, setup):
        setup.find_element('id', 'gender-male').click()

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('Rohit')

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('Shukla')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('rohit@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('rohit@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('rohit@12345')


class Testlogin:

    def test_login(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('rohit@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('rohit@12345')

































































































