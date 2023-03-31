from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep
from utilities.db_utils import is_user_in_db


class Tests(WebDriverSetup):

    def test_34_valid_sign_up(self, setUp):
        phone = '0577944554'
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input(phone)
        self.registration_page.click_bnnumber_field()
        self.registration_page.sign_up_bnnumber_input('1234')
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
        login_code = self.registration_page.get_login_code_from_db(self.db, phone)
        self.registration_page.fill_signup_code_in_squares(login_code)
        self.registration_page.click_signup_user()
        is_user_created = is_user_in_db(self.db, phone)
        assert is_user_created == True


    def test_signup_with_invalid_phone(self, setUp):
        phone = '0577'
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input(phone)
        self.registration_page.click_bnnumber_field()
        self.registration_page.sign_up_bnnumber_input('1234')
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
        phone_error_message = self.registration_page.get_invalid_phone_error_message()
        assert phone_error_message.text == 'מס׳ טלפון לא תקין', \
            f"Unexpected text: {phone_error_message.text}"


    def test_sign_up_with_invalid_bnnumber_over_9_char(self, setUp):
        phone = '0577467001'
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input(phone)
        self.registration_page.click_bnnumber_field()
        self.registration_page.sign_up_bnnumber_input('12345678910')
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
       # Todo: ask israel what is the ifyun and which assert i need










    def test_sign_up_with_exists_user(self, setUp):
        phone = '0525918555'
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input(phone)
        self.registration_page.click_bnnumber_field()
        self.registration_page.sign_up_bnnumber_input('1234')
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
        login_code = self.registration_page.get_login_code_from_db(self.db, phone)
        self.registration_page.fill_signup_code_in_squares(login_code)
        self.registration_page.click_signup_user()
        is_user_created = is_user_in_db(self.db, phone)
    # Todo: assert user not created more than once and assert error message

    # assert "Phone number already exists" in error_msg
    #
    # users = get_users_by_phone_number(self.db, phone)
    # assert len(users) == 1

    def test_sign_up_without_details(self, setUp):
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
        phone_field_error_msg = self.login_page.get_empty_phone_error_message()
        assert phone_field_error_msg == 'נא למלא שדה זה', f"Unexpected text: {phone_field_error_msg}"


    def test_invalid_sign_up_without_terms_checkbox(self,setUp):
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input('0525918555')
        self.registration_page.click_bnnumber_field()
        self.registration_page.sign_up_bnnumber_input('1234')
        self.registration_page.click_create_user_btn()
        # Todo: change assert that checking the text error or on db user not created


