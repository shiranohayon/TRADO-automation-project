from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.footer_locators import FooterLocators
from time import sleep

class FooterPage:

    def __init__(self, driver):
        self.driver = driver

    def click_contact_us_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.contact_us_btn))).click()

    def fill_firstname_contact_us(self, firstname):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.footer_first_name_field))).send_keys(firstname)

    def fill_lastname_contact_us(self, lastname):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.footer_last_name_field))).send_keys(lastname)

    def fill_email_contact_us(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.footer_email_field))).send_keys(email)

    def fill_phone_contact_us(self, phone):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.footer_phone_field))).send_keys(phone)

    def fill_content_refferal_contact_us(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.content_refferal))).send_keys(text)

    def click_send_message_contact_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.send_message_btn))).click()

    def get_confirmation_txt_contact_us(self):
       return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.confirmation_txt_message)))

