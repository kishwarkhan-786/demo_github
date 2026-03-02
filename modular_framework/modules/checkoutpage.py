import time

class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver

    def enter_firstname(self):
        self.driver.find_element('id', 'first-name').send_keys("Deep")
        time.sleep(1)

    def enter_lastname(self):
        self.driver.find_element('id', 'last-name').send_keys('Dhamecha')
        time.sleep(1)

    def enter_postal_code(self):
        self.driver.find_element('id', 'postal-code').send_keys('560003')
        time.sleep(1)

    def click_on_continue(self):
        self.driver.find_element('id', 'continue').click()
        time.sleep(2)

    def click_on_finish(self):
        self.driver.find_element('xpath', '//button[text()="Finish"]').click()
        time.sleep(2)

    def click_on_backhome(self):
        self.driver.find_element('xpath', '//button[text()="Back Home"]').click()
        time.sleep(2)


