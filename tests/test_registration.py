from selenium.webdriver.support.wait import WebDriverWait
from utilities.setup import WebDriverSetup
from utilities.db_utils import is_user_in_db, count_users_by_phone_number
import allure

class Tests(WebDriverSetup):

    @allure.title("test_29_valid_sign_up")
    def test_29_valid_sign_up(self, setUp):
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


    def test_31_signup_with_invalid_phone(self, setUp):
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
        is_user_created = is_user_in_db(self.db, phone)
        assert phone_error_message.text == 'מס׳ טלפון לא תקין' and is_user_created == False


    def test_32_sign_up_with_invalid_bnnumber_over_9_char(self, setUp):
        phone = '0577467001'
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input(phone)
        self.registration_page.click_bnnumber_field()
        bnnumber = '1234567891067957'
        self.registration_page.sign_up_bnnumber_input(bnnumber)
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
        assert len(bnnumber) <= 9


    def test_33_sign_up_with_exists_user(self, setUp):
        phone = '0525918555'
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input(phone)
        self.registration_page.click_bnnumber_field()
        self.registration_page.sign_up_bnnumber_input('1234')
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
        exist_user_error_msg_text = self.registration_page.error_message_exist_user()
        count_users = count_users_by_phone_number(self.db, phone)
        assert count_users == 1 and exist_user_error_msg_text == 'שדה צריך להיות ייחודיי'

    def test_34_sign_up_without_details(self, setUp):
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_terms_checkbox()
        self.registration_page.click_create_user_btn()
        phone_field_error_msg = self.login_page.get_empty_phone_error_message()
        assert phone_field_error_msg == 'נא למלא שדה זה', f"Unexpected text: {phone_field_error_msg}"


    def test_30_invalid_sign_up_without_terms_checkbox(self,setUp):
        phone = '0573391825'
        self.home_page.click_connection()
        self.registration_page.click_sign_up()
        self.registration_page.click_phone_field_signup()
        self.registration_page.sign_up_phone_input(phone)
        self.registration_page.click_bnnumber_field()
        self.registration_page.sign_up_bnnumber_input('1234456')
        self.registration_page.click_create_user_btn()
        terms_error_message = self.registration_page.get_approve_policy_error_message()
        is_user_created = is_user_in_db(self.db, phone)
        assert terms_error_message.text == 'Please Approve Our Policy' and is_user_created == False



