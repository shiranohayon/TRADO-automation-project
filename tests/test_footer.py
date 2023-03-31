from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep

class Tests(WebDriverSetup):

    def test_send_valid_message_contact_us(self, setUp):
        self.footer_page.click_contact_us_btn()
        self.footer_page.fill_firstname_contact_us('shiran')
        self.footer_page.fill_lastname_contact_us('ohayon')
        self.footer_page.fill_email_contact_us('aa11bb22ghkl@gmail.com')
        self.footer_page.fill_phone_contact_us('0573332145')
        self.footer_page.fill_content_refferal_contact_us('just a test')
        self.footer_page.click_send_message_contact_us()
        confirmation_msg = self.footer_page.get_confirmation_txt_contact_us()
        assert confirmation_msg.text == 'הפרטים נקלטו בהצלחה', f"Unexpected text: {confirmation_msg.text}"