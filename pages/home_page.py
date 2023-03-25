from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_locators import HomeLocators
from selenium.webdriver.common.keys import Keys
from time import sleep

class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def get_welcome_popup(self):
       return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.welcome_to_popup)))

    def wait_welcome_popup_disappear(self):
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located((By.XPATH, HomeLocators.welcome_to_popup)))

    def get_welcome_popup(self):
        welcome_popup = self.driver.find_element(By.XPATH, HomeLocators.welcome_to_popup)
        return welcome_popup

    def is_welcome_popup_displayed(self):
        # return self.get_welcome_popup().is_displayed()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, HomeLocators.welcome_to_popup)))


    def click_restaurant_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.popup_restaurant_option))).click()
        sleep(2)

    def get_save_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.popup_save_btn)))

    def click_save_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.popup_save_btn))).click()

    def txt_sales_btn(self):
        view_sales = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.sales_btn)))
        return view_sales

    def txt_drinks_btn(self):
        view_drinks = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.drinks_btn)))
        return view_drinks

    def click_drinks_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.drinks_btn))).click()


    def click_change_to_us_language(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.change_language_us_btn))).click()
        sleep(3)

    def check_login_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.login_btn)))


    def click_top_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.top_logo_btn))).click()
        sleep(2)

    def view_first_banner_image(self):
        self.driver.find_element((By.XPATH, HomeLocators.promotional_banner_first_image))
        sleep(7)

    def view_second_banner_image(self):
        self.driver.find_element((By.XPATH, HomeLocators.promotional_banner_second_image))
        sleep(7)

    def get_banner(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.banner)))

    def get_current_img_src(self):
        sleep(3)
        # Todo: check why it doesnt find the element by classname
        current = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "slide selected")))
        a = current.find_element(By.TAG_NAME, 'a')
        image = a.find_element(By.TAG_NAME, 'img')
        src = image.get_attribute('src')
        return src


    def drinks_btn_blue_line(self):
       return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.drinks_btn)))

    def external_txt_product_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.external_product_title)))
        sleep(3)





    def get_search_bar_text_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.search_bar_text_field)))

    def search_bar_keyword(self, keyword):
        search_bar_text_field = self.get_search_bar_text_field()
        search_bar_text_field.click()
        search_bar_text_field.send_keys(keyword)





    def no_results_search_bar(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(By.XPATH, HomeLocators.zero_results_error_search))



    def welcome_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.welcome_to_popup)))
        self.click_restaurant_option()
        self.click_save_btn()













