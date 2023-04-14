from selenium.webdriver.support.wait import WebDriverWait

from utilities.db_utils import is_product_in_db
from utilities.setup import WebDriverSetup
import allure

class Tests(WebDriverSetup):

    @allure.title("test_15_product_units_amount")
    def test_14_product_units_amount(self, setUp):
        self.products_page.click_product()
        barcode = self.products_page.get_barcode()
        # keep in barcode_from_page only the barcode, used replace method to remove title before
        barcode_from_page = barcode.replace("מק״ט יצרן: ", "")
        # get the amount of the product from db by barcode
        amount_from_db = self.products_page.get_units_amount_from_db(self.db, barcode_from_page)
        amount_from_page = self.products_page.get_units_amount()
        assert amount_from_db == amount_from_page


    def test_15_product_price(self, setUp):
        self.products_page.click_product()
        barcode = self.products_page.get_barcode()
        # keep in barcode_from_page only the barcode, used replace method to remove title before
        barcode_from_page = barcode.replace("מק״ט יצרן: ", "")
        # get the amount of the product from db by barcode
        get_price = self.products_page.get_product_price()
        price_from_db = self.products_page.get_product_price_from_db(self.db, barcode_from_page)
        price_from_page = float(get_price.split("/")[0])

        assert price_from_db == price_from_page


    def test_18_create_new_store(self, setUp):
        self.login_page.login_process(self.db)
        self.home_page.click_upload_product_btn()
        self.products_page.fill_bn_number_field('1234')
        self.products_page.fill_phone_field('1234567345')
        self.products_page.fill_website_url_field('https://qa.trado.co.il/')
        self.products_page.fill_street_field('street')
        self.products_page.fill_business_name_field('food company')
        self.products_page.fill_email_field('aa11bb22ghkl@gmail.com')
        self.products_page.fill_city_field('tel aviv')
        self.products_page.fill_building_field('8')
        self.products_page.click_add_product_btn()
        assert 1 == 1
       # Todo: fix assert

    def test_19_upload_new_product(self, setUp):
        self.login_page.login_process(self.db)
        self.home_page.click_upload_product_btn()
        barcode = "12335"
        self.products_page.fill_catalog_number_field(barcode)
        self.products_page.fill_product_name_field('pasta barilla')
        self.products_page.fill_price_of_product_field('20')
        self.products_page.click_add_product_btn()
        self.products_page.fill_quantity_in_carton_field('100')
        self.products_page.fill_stock_of_cartons_field('2000')
        self.products_page.fill_minimum_cartors_for_order_field('30')
        self.products_page.click_add_product_btn()
        self.products_page.fill_business_days_field('3')
        self.products_page.fill_remarks_field('no remarks')
        self.products_page.fill_your_phone_field('0745678942')
        self.products_page.click_add_product_btn()
        is_product_created = is_product_in_db(self.db, barcode)
        assert is_product_created == True
















