from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_locators import HomeLocators
from locators.cart_locators import CartLocators
from time import sleep

class CartPage:

    def __init__(self, driver):
        self.driver = driver


    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, CartLocators.product_name_in_cart))).text

    def get_price_of_product_on_cart(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, CartLocators.price_of_product_on_cart))).text
        element = element.replace("₪", "")
        return element
