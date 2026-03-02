import time

class HomePage:
    def __init__(self,driver):
        self.driver=driver


    def click_on_pro1(self):
        self.driver.find_element('xpath', '//div[text()="Sauce Labs Backpack"]/../../..//button[text()="Add to cart"]').click()
        time.sleep(2)

    def click_on_cart_icon(self):
        self.driver.find_element('xpath', '//div[@id="shopping_cart_container"]').click()
        time.sleep(2)

    def click_on_pro2(self):
        self.driver.find_element('xpath', '//div[text()="Sauce Labs Bike Light"]/../../..//button[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(2)

    def click_on_menu_btn(self):
        self.driver.find_element('id', 'react-burger-menu-btn').click()
        time.sleep(2)

    def click_on_logout(self):
        self.driver.find_element('id', 'logout_sidebar_link').click()
