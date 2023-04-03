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
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.inner_product_title)))

    def inner_product_image(self):
        img_element = self.driver.find_element(By.CSS_SELECTOR, "div.fullProduct_image img")
        src = img_element.get_attribute("src")
        return src


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
        return barcode

    def get_product_price(self):
        price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.product_price))).text
        return price


    def get_product_price_from_db(self, db, barcode):
        # get the whole product from db by barcode
        product = get_specific_document(db, "products", "barcode", barcode)
        price = product.get("price")
        return price



    def fill_bn_number_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.bnnumber_field).send_keys(text)
    def fill_phone_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.phone_field).send_keys(text)
    def fill_website_url_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.website_url_field).send_keys(text)
    def fill_street_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.street_field).send_keys(text)
    def fill_business_name_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.business_name_field).send_keys(text)
    def fill_email_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.email_field).send_keys(text)
    def fill_city_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.city_field).send_keys(text)
    def fill_building_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.building_field).send_keys(text)


    def click_add_product_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.add_product_btn).click()
        sleep(3)

    def fill_catalog_number_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.catalog_number_field).send_keys(text)
    def fill_product_name_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.product_name_field).send_keys(text)
    def fill_price_of_product_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.product_price_field).send_keys(text)
    def fill_quantity_in_carton_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.quantity_in_carton_field).send_keys(text)
    def fill_stock_of_cartons_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.stock_of_cartons_field).send_keys(text)
    def fill_minimum_cartors_for_order_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.minimum_cartors_for_order_field).send_keys(text)
    def fill_business_days_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.shipping_popup_business_days).send_keys(text)
    def fill_remarks_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.shipping_popup_remarks).send_keys(text)
    def fill_your_phone_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.shipping_popup_your_phone).send_keys(text)
    def click_plus_product_quantity(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.product_quantity_btn))).click()
    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.product_name))).text

    def get_price_of_product_on_page(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.page_product_price))).text
        element = element.replace("₪", "")
        return element