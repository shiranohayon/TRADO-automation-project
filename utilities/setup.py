import pytest
from selenium import webdriver
from pages.login_page import LoginPage
# from pages.cart_page import Cartpage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
# from pages.sign_up_page import Sign_Up_Page
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from utilities.db_utils import create_mongo_connection



class WebDriverSetup:

    @pytest.fixture()
    def setUp(self):
        chromedriver_path = "C:/chromedriver/chromedriver.exe"
        service = Service(executable_path=chromedriver_path)
        # options = Options()
        # options.headless = True
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(service=service,options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        self.driver.get("https://qa.trado.co.il/")
        self.login_page = LoginPage(self.driver)
        # self.cart_page = CartPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.welcome_popup()
        self.products_page = ProductsPage(self.driver)
        # self.registration_page = SignUpPage(self.driver)
        self.db = create_mongo_connection()
        yield self.driver
        self.driver.quit()











