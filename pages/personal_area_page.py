from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.personal_area_locators import PersonalAreaLocators
from utilities.db_utils import get_login_code
from time import sleep


class PersonalAreaPage:

    def __init__(self, driver):
        self.driver = driver


    def click_personal_area(self):
        sleep(2)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, PersonalAreaLocators.personal_area_btn))).click()

    def click_edit_btn(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, PersonalAreaLocators.edit_btn))).click()
        sleep(2)


    def fill_first_name_field(self, name):
       element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, PersonalAreaLocators.first_name_field)))
       element.clear()
       element.send_keys(name)

    def fill_last_name_field(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, PersonalAreaLocators.last_name_field)))
        element.clear()
        element.send_keys(name)

    def fill_city_field(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, PersonalAreaLocators.city_field)))
        element.clear()
        element.send_keys(name)

    def fill_home_number_field(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, PersonalAreaLocators.home_number_field)))
        element.clear()
        element.send_keys(name)

