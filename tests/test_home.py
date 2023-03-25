from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from time import sleep

class Tests(WebDriverSetup):

    def test_1_welcome_to_popup_with_category(self, setUp):
        welcome_popup = self.home_page.get_welcome_popup()
        print("welcome_popup before")
        print(welcome_popup)
        self.home_page.click_restaurant_option()
        self.home_page.click_save_btn()
        sleep(2)
        print("welcome_popup after")
        print(welcome_popup)
        # Todo: check how to know if welcome_popup is not displayed anymore
        assert welcome_popup.is_displayed() == False







    def test_3_valid_text_sales_btn(self, setUp):
        sales_btn = self.home_page.txt_sales_btn()
        assert sales_btn.text == 'מבצעים', f"Unexpected text: {sales_btn.text}"


    def test_4_valid_text_drinks_btn(self, setUp):
        drinks_btn = self.home_page.txt_drinks_btn()
        assert drinks_btn.text == 'משקאות', f"Unexpected text: {drinks_btn.text}"


    def test_5_click_drinks_btn(self, setUp):
        self.home_page.click_drinks_btn()
        # Check if the current URL is correct
        assert self.driver.current_url == "https://qa.trado.co.il/?sectionName=%D7%9E%D7%A9%D7%A7%D7%90%D7%95%D7%AA"



    def test_7_search_invalid_keyword(self, setUp):
        sleep(2)
        self.home_page.search_bar_keyword('aaaa')
        sleep(2)
        results_search_bar = self.home_page.no_results_search_bar()
        sleep(2)
        # Todo: check if the results window should appear and when
        assert self.home_page.no_results_search_bar()



    def test_change_to_us_language(self, setUp):
        self.home_page.click_change_to_us_language()
        login_btn = self.home_page.check_login_btn()
        assert login_btn.text == 'Login', f"Unexpected text: {login_btn.text}"



    def test_9_top_logo_redirects_home_page_from_product(self, setUp):
        self.products_page.click_product()
        self.home_page.click_top_logo()
        assert self.driver.current_url == 'https://qa.trado.co.il/'


    # def test_10_promotional_banner_image_transition(self, setUp):
    #     first_img = self.home_page.view_first_banner_image()
    #     # get image source attribute
    #     first_image_src = first_img.get_attribute('src')
    #     second_img = self.home_page.view_second_banner_image()
    #     second_image_src = second_img.get_attribute('src')
    #     # check if the external and inner image sources are equal
    #     assert first_image_src != second_image_src

    def test_10_promotional_banner_image_transition(self, setUp):
        # Todo read the todo in get_current_img_src()
        first_img_src = self.home_page.get_current_img_src()
        sleep(5)
        second_img_src = self.home_page.get_current_img_src()
        print("first_img_src")
        print(first_img_src)
        print("second_img_src")
        print(second_img_src)
        assert first_img_src != second_img_src



    def test_11_blue_line_under_drinks_button(self, setUp):
        self.home_page.click_drinks_btn()
        drinks_btn_class = self.home_page.drinks_btn_blue_line().get_attribute('class')
        assert drinks_btn_class == "verticalMenu_active"

    def test_12_redirect_to_product_page(self, setUp):
        self.products_page.click_product()
        assert self.driver.current_url == 'https://qa.trado.co.il/product/60341'

    def test_13_product_title(self, setUp):
        external_title = self.home_page.external_txt_product_btn()
        # Get the external text of the product button element
        external_title_text = external_title.text
        self.products_page.click_product()
        # Get the inner text of the product button element
        inner_title = self.products_page.inner_txt_product_btn()
        inner_title_text = inner_title.text
        # Check if the external and inner titles are equal
        assert external_title_text == inner_title_text
        print(external_title_text, '\n', inner_title_text)


    def test_14_product_image(self, setUp):
        external_image = self.home_page.external_product_image()
        #get image source attribute
        external_image_src = external_image.get_attribute('src')
        external_image.click()
        inner_image = self.product_page.inner_product_image()
        inner_image_src = inner_image.get_attribute('src')
        # check if the external and inner image sources are equal
        assert external_image_src == inner_image_src










