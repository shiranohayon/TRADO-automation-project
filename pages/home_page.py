from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_locators import HomeLocators
from selenium.webdriver.common.keys import Keys
from time import sleep
from utilities.db_utils import get_random_product

class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def get_welcome_popup(self):
        welcome_popup = self.driver.find_element(By.XPATH, HomeLocators.welcome_to_popup).is_displayed()
        return welcome_popup

    def wait_welcome_popup_disappear(self):
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located((By.XPATH, HomeLocators.welcome_to_popup)))


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
        current = self.driver.find_element(By.CSS_SELECTOR, ".slide.selected")
        a = current.find_element(By.TAG_NAME, 'a')
        image = a.find_element(By.TAG_NAME, 'img')
        src = image.get_attribute('src')
        return src


    def drinks_btn_blue_line(self):
       return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.drinks_btn)))

    def external_txt_product_btn(self):
        sleep(4)
        link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/product/56586']")
        # Find the <div> element with class "productDesc_name" inside the <a> element
        div = link.find_element(By.CSS_SELECTOR, "div.productDesc_name")
        return div


    # def external_product_image(self):




    def click_search_bar_text_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, HomeLocators.search_bar_text_field))).click()

    def search_bar_keyword(self, input):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, HomeLocators.search_bar_text_field))).send_keys(input)



    def no_results_search_bar(self):
        return self.driver.find_element(By.XPATH, HomeLocators.zero_results_error_search).is_displayed()



    def welcome_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.welcome_to_popup)))
        self.click_restaurant_option()
        self.click_save_btn()



    def sort_product_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.sort_btn))).click()
        sleep(2)

    def sort_high_to_low_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.sort_high_to_low))).click()
        sleep(2)

    def sort_low_to_high_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.sort_low_to_high))).click()
        sleep(2)


    def txt_of_importants(self):
      return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.footer_importants_text)))

    def click_connection(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.connection_login_signup_btn))).click()

    def get_product_name_to_search(self, db):
        product = get_random_product(db)
        return product.get("name")

    def is_result_window_displayed(self):
        results = self.driver.find_element(By.CLASS_NAME, "mainSearch_results")
        return results.is_displayed()

    def get_all_products_prices(self):
        prices = []
        prices_list = self.driver.find_elements(By.CSS_SELECTOR, ".productPrice_price")
        for product_price in prices_list:
            price = product_price.text
            price = price.replace("₪", "")
            price = float(price)
            prices.append(price)
        return prices

    def is_sorted_high_to_low(self, lst):
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:
                return False
        return True

    def is_sorted_low_to_high(self, lst):
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                return False
        return True








