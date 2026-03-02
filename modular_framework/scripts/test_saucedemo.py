from modular_framework.modules.loginpage import LoginPage
from modular_framework.modules.homepage import HomePage
from modular_framework.modules.cartpage import CartPage
from modular_framework.modules.checkoutpage import CheckoutPage

def test_case1(setup):
    lp = LoginPage(setup)
    hp = HomePage(setup)
    cp = CartPage(setup)
    cop = CheckoutPage(setup)

    lp.enter_username()
    lp.enter_password()
    lp.click_on_login_btn()
    hp.click_on_pro1()
    hp.click_on_cart_icon()
    cp.validate_product1()
    cp.click_on_continue_shopping()
    hp.click_on_pro2()
    hp.click_on_cart_icon()
    cp.validate_product2()
    cp.click_on_checkout()
    cop.enter_firstname()
    cop.enter_lastname()
    cop.enter_postal_code()
    cop.click_on_continue()
    cop.click_on_finish()
    cop.click_on_backhome()
    hp.click_on_menu_btn()
    hp.click_on_logout()

