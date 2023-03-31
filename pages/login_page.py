from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from utilities.db_utils import get_login_code
from pages.home_page import HomePage, HomeLocators
from time import sleep


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_phone_input(self, phone):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.login_phone_filed))).send_keys(phone)

    def click_login_user(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, LoginLocators.login_user_btn))).click()



    def get_logincode_from_db(self, db, phone):
        return get_login_code(db, phone)


    def login_process(self, db):
        phone = '0525918555'
        HomePage.click_connection(self)
        self.login_phone_input('0525918555')
        self.click_login_user()
        login_code = self.get_logincode_from_db(db, phone)
        self.fill_login_code_in_squares(login_code)
        self.click_login_user()
        sleep(2)

    def get_connection_btn(self):
       return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.connection_login_signup_btn))).is_displayed()

    def get_connection_btn_text(self):
       return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.connection_login_signup_btn))).text

    def click_connection_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.connection_login_signup_btn))).click()

    def click_close_connection_popup(self):
        self.driver.find_element(By.XPATH, LoginLocators.close_connection_popup).click()

    def get_personal_area(self):
       return WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, LoginLocators.personal_area_btn)))

    def get_login_popup(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, LoginLocators.login_popup)))

    def get_empty_phone_error_message(self):
        # error_div = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, LoginLocators.empty_phone_error_message)))
        error_div = self.driver.find_element(By.XPATH, LoginLocators.empty_phone_error_message)

        return error_div.text




    # def fill_login_code_in_squares(self, logincode):
    #     for i in range(5):
    #         element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located((By.CLASS_NAME, "input_" + str(i))))
    #         element.send_keys(logincode[i])

    def fill_login_code_in_squares(self, logincode):
        for i in range(5):
            div = i + 1
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[{div}]/span/input')))
            element.send_keys(logincode[i])


    def get_logout_btn(self):
        return self.driver.find_element(By.CLASS_NAME,LoginLocators.log_out_btn)






