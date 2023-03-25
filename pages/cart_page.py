from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_locators import Buttons_home
from time import sleep

class CartPage:

    def __init__(self, driver):
        self.driver = driver