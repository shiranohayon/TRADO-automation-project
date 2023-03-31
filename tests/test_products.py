from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep

class Tests(WebDriverSetup):

    def test_15_product_units_amount(self, setUp):
        self.products_page.click_product()
        barcode = self.products_page.get_barcode()
        # keep in barcode_from_page only the barcode, used replace method to remove title before
        barcode_from_page = barcode.replace("מק״ט יצרן: ", "")
        # get the amount of the product from db by barcode
        amount_from_db = self.products_page.get_units_amount_from_db(self.db, barcode_from_page)
        amount_from_page = self.products_page.get_units_amount()
        assert amount_from_db == amount_from_page



    def test_16_product_price(self, setUp):
        self.products_page.click_product()
        barcode = self.products_page.get_barcode()
        # keep in barcode_from_page only the barcode, used replace method to remove title before
        barcode_from_page = barcode.replace("מק״ט יצרן: ", "")
        # get the amount of the product from db by barcode
        get_price = self.products_page.get_product_price()
        price_from_db = self.products_page.get_product_price_from_db(self.db, barcode_from_page)
        price_from_page = float(get_price.split("/")[0])

        assert price_from_db == price_from_page









