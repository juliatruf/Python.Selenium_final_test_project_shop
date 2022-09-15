from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    url = 'https://www.onlinetrade.ru/'
    city = 'Ярославль'
    category = 'Компьютеры и периферия'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_change_city = "//a[@data-handlermode='cityselectnew']"
    select_city = "//a[text()='" + city + "']"
    select_no_city = "//a[@title='доставка по России']"
    menu = "//div[@class='header__menuLink__icon']"
    select_category = "//span[text()='Компьютеры и периферия']"
    current_breadcrumbs = "//span[@class='breadcrumbs__itemCurrent']"

    # Getters

    def get_select_change_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_change_city)))

    def get_select_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_city)))

    def get_select_no_city(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.select_no_city)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category)))

    def get_select_category_breadcrumbs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_breadcrumbs)))

    # Actions

    def click_select_change_city(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_select_change_city().click()
        print("Click change city ")

    def click_select_city(self):
        self.get_select_city().click()
        print("Click select city: ", self.city)

    def click_select_no_city(self):
        self.get_select_no_city().click()
        print("Click select: доставка по России")

    def click_menu(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_menu().click()
        print("Click menu Catalog")

    def click_select_category(self):
        self.get_select_category().click()
        print("Click select category: ", self.category)

    # Methods

    def select_location_city(self):
        self.get_current_url()
        self.click_select_change_city()
        self.scroll_page_to_element(self.get_select_city())
        self.click_select_city()
        self.get_screenshot()
        self.assert_word(self.get_select_change_city(), self.city)

    def select_location_no_city_from_list(self):
        self.get_current_url()
        self.click_select_change_city()
        self.scroll_page_to_element(self.get_select_no_city())
        self.click_select_no_city()
        self.get_screenshot()
        self.assert_word(self.get_select_change_city(), "Города России")

    def select_category_name(self):
        self.get_current_url()
        self.click_menu()
        self.click_select_category()
        self.assert_word(self.get_select_category_breadcrumbs(), self.category)
