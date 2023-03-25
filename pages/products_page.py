from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.products_locators import ProductsLocators
from time import sleep
from utilities.db_utils import get_specific_document

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver


    def click_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.product_btn))).click()
        sleep(2)

    def inner_txt_product_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.inner_product_title)))

    def get_units_amount(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.units_amount))).text

    # db is the connection object to mongo
    def get_units_amount_from_db(self, db, barcode):
        # get the whole product from db by barcode
        product = get_specific_document(db, "products", "barcode", barcode)
        units = product.get("units")
        amount = units.get("amount")
        return amount

    def get_barcode(self):
        barcode = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.barcode))).text
        print(barcode)
        return barcode