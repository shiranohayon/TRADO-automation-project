from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage
from time import sleep
import allure


class Tests(WebDriverSetup):

    @allure.title("test_35_valid_log_in")
    def test_35_valid_log_in(self, setUp):
        self.login_page.login_process(self.db)
        personal_area_btn = self.login_page.get_personal_area()
        assert personal_area_btn.text == 'אזור אישי', f"Unexpected text: {personal_area_btn.text}"

    def test_36_invalid_log_in(self, setUp):
        self.login_page.invalid_login_process()
        personal_area_btn = self.login_page.get_personal_area()
        assert personal_area_btn.text != 'אזור אישי', f"Unexpected text: {personal_area_btn.text}"


    def test_37_log_in_without_details(self, setUp):
       self.home_page.click_connection()
       self.login_page.click_login_user()
       phone_field_error_msg = self.login_page.get_empty_phone_error_message()
       assert phone_field_error_msg == 'נא למלא שדה זה', f"Unexpected text: {phone_field_error_msg}"


    def test_38_log_out(self, setUp):
        self.login_page.login_process(self.db)
        logout_btn = self.login_page.get_logout_btn()
        logout_btn.click()
        assert self.login_page.get_connection_btn_text() == 'התחברות'

    def test_39_close_log_in_popup(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.click_close_connection_popup()
        is_login_popup_displayed = self.login_page.get_login_popup()
        assert is_login_popup_displayed == True

    def test_40_facebook_icon_visibility(self, setUp):
       self.home_page.click_connection()
       is_facebook_logo_displayed = self.login_page.get_facebook_logo()
       assert is_facebook_logo_displayed == True

    def test_41_google_icon_visibility(self, setUp):
        self.home_page.click_connection()
        is_google_logo_displayed = self.login_page.get_google_logo()
        assert is_google_logo_displayed == True

    def test_42_twitter_icon_visibility(self, setUp):
        self.home_page.click_connection()
        is_twitter_logo_displayed = self.login_page.get_twitter_logo()
        assert is_twitter_logo_displayed == True










