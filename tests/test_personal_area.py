from selenium.webdriver.support.wait import WebDriverWait
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep
from utilities.db_utils import get_user_first_name, get_user_last_name, get_user_city, get_user_home_number
import allure

class Tests(WebDriverSetup):

    @allure.title("test_43_fill_shipping_details_personal_area")
    def test_43_fill_shipping_details_personal_area(self, setUp):
        self.login_page.login_process(self.db)
        self.personal_area_page.click_personal_area()
        self.personal_area_page.click_edit_btn()
        first_name = 'shira'
        last_name = 'ohayo'
        city = 'tel aviv'
        home_number = '81'
        phone = '0525918555'
        self.personal_area_page.fill_first_name_field(first_name)
        self.personal_area_page.fill_last_name_field(last_name)
        self.personal_area_page.fill_city_field(city)
        self.personal_area_page.fill_home_number_field(home_number)
        self.personal_area_page.click_edit_btn()
        sleep(4)
        assert first_name == get_user_first_name(self.db, phone)
        assert last_name == get_user_last_name(self.db, phone)
        # The city returns bug, empty on db and should fail
        assert city == get_user_city(self.db, phone)
        assert home_number == get_user_home_number(self.db, phone)

