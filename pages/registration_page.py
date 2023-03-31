from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_locators import SignUpLocators
from selenium.webdriver.common.keys import Keys
from utilities.db_utils import get_login_code
from time import sleep

class SignUpPage:

    def __init__(self, driver):
        self.driver = driver

    def click_sign_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.sign_up_btn))).click()

    def click_phone_field_signup(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.signup_phone_input))).click()
        sleep(2)

    def click_bnnumber_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.signup_bnnumber_input))).click()


    def sign_up_phone_input(self, phone):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.signup_phone_input))).send_keys(phone)
        sleep(2)


    def sign_up_bnnumber_input(self, bnnumber):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.signup_bnnumber_input))).send_keys(bnnumber)
        sleep(2)


    def click_terms_checkbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.agree_terms_checkbox))).click()
        sleep(3)


    def click_create_user_btn(self):
        sleep(2)
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.create_user_btn))).click()


    def get_login_code_from_db(self, db, phone):
        sleep(3)
        return get_login_code(db, phone)

    def click_signup_user(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, SignUpLocators.login_user_btn))).click()


    def get_invalid_phone_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, SignUpLocators.phone_error_message)))


    def input_square1(self, number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.square1))).send_keys(number)
    def input_square2(self, number):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, SignUpLocators.square2))).send_keys(number)
    def input_square3(self, number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.square3))).send_keys(number)
    def input_square4(self, number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.square4))).send_keys(number)

    def input_square5(self, number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SignUpLocators.square5))).send_keys(number)



    def fill_signup_code_in_squares(self, logincode):
        squares = [SignUpLocators.square1, SignUpLocators.square2, SignUpLocators.square3,
                   SignUpLocators.square4, SignUpLocators.square5]
        for i in range(len(logincode)):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, squares[i]))).send_keys(
                logincode[i])












