from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep
import allure

class Tests(WebDriverSetup):

    @allure.title("test_27_add_single_product_to_cart")
    def test_27_add_single_product_to_cart(self, setUp):
        self.home_page.click_product()
        product_name_in_page = self.products_page.get_product_name()
        self.products_page.click_plus_product_quantity()
        product_name_in_cart = self.cart_page.get_product_name()
        assert product_name_in_page == product_name_in_cart

    def test_28_product_price_from_main_page_to_cart(self, setUp):
        self.home_page.click_product()
        product_price_in_page = self.products_page.get_price_of_product_on_page()
        self.products_page.click_plus_product_quantity()
        product_price_in_cart = self.cart_page.get_price_of_product_on_cart()
        assert product_price_in_page == product_price_in_cart

