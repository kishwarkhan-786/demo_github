import time


class CartPage:
    def __init__(self,driver):
        self.driver=driver

    def validate_product1(self):
        assert self.driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]').is_displayed()

    def click_on_continue_shopping(self):
        self.driver.find_element('xpath', '//button[@id="continue-shopping"]').click()
        time.sleep(2)

    def validate_product2(self):
        assert self.driver.find_element('xpath', '//div[text()="Sauce Labs Bike Light"]').is_displayed()
        time.sleep(1)

    def click_on_checkout(self):
        self.driver.find_element('id', 'checkout').click()
        time.sleep(2)

