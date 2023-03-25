from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep

class Tests(WebDriverSetup):

    def test_1_check_product_units_amount(self, setUp):
        self.products_page.click_product()
        barcode = self.products_page.get_barcode()

        # keep in barcode_from_page only the barcode without before
        barcode_from_page = barcode.replace("מק״ט יצרן: ", "")

        # get the amount of the product from db by barcode
        amount_from_db = self.products_page.get_units_amount_from_db(self.db, barcode_from_page)
        amount_from_page = self.products_page.get_units_amount()
        assert amount_from_db == amount_from_page


