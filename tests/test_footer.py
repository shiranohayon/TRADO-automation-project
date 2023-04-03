from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep
import allure

class Tests(WebDriverSetup):

    @allure.title("test_21_send_valid_message_contact_us")
    def test_21_send_valid_message_contact_us(self, setUp):
        self.footer_page.click_contact_us_btn()
        self.footer_page.fill_firstname_contact_us('shiran')
        self.footer_page.fill_lastname_contact_us('ohayon')
        self.footer_page.fill_email_contact_us('aa11bb22ghkl@gmail.com')
        self.footer_page.fill_phone_contact_us('0573332145')
        self.footer_page.fill_content_refferal_contact_us('just a test')
        self.footer_page.click_send_message_contact_us()
        confirmation_msg = self.footer_page.get_confirmation_txt_contact_us()
        assert confirmation_msg.text == 'הפרטים נקלטו בהצלחה', f"Unexpected text: {confirmation_msg.text}"


    def test_22_limit_of_100_chars_contact_us(self, setUp):
        self.footer_page.click_contact_us_btn()
        self.footer_page.fill_firstname_contact_us('shiran')
        self.footer_page.fill_lastname_contact_us('ohayon')
        self.footer_page.fill_email_contact_us('aa11bb22ghkl@gmail.com')
        self.footer_page.fill_phone_contact_us('0573332145')
        # Try to enter invalid message more than 100 chars
        random_101_letters_string = self.footer_page.forloop_invalid_content_refferal()
        self.footer_page.fill_content_refferal_contact_us(random_101_letters_string)
        output_text_content_refferal = self.footer_page.get_text_content_refferal_contact_us()
        assert len(output_text_content_refferal) == 100


    def test_24_nevigation_to_facebook_stay_in_touch(self, setUp):
        self.footer_page.click_facebook_link()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == ('https://www.facebook.com/')

    def test_25_nevigation_to_instagram_stay_in_touch(self, setUp):
        self.footer_page.click_instagram_link()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == ('https://www.instagram.com/')

    def test_26_nevigation_to_twitter_stay_in_touch(self, setUp):
        self.footer_page.click_twitter_link()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == ('https://twitter.com/?lang=he')