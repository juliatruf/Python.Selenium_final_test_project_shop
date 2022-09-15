from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Subcategory_computers_manipulators_page(Base):

    #subcategory = 'Манипуляторы и устройства ввода'
    #sub_2_category = 'Клавиатуры'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sub_2_category_keyboards = "//span[text()='Клавиатуры ']"
    current_breadcrumbs = "//span[@class='breadcrumbs__itemCurrent']"

    # Getters

    def get_select_manipulators_keyboards(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sub_2_category_keyboards)))

    def get_select_sub_2_category_breadcrumbs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_breadcrumbs)))

    # Actions

    def click_select_manipulators_keyboards(self):
        self.get_select_manipulators_keyboards().click()
        print("Click select sub-subcategory")

    # Methods

    def select_manipulators_keyboards(self):
        self.get_current_url()
        self.click_select_manipulators_keyboards()
        self.assert_word(self.get_select_sub_2_category_breadcrumbs(), 'Клавиатуры')
        self.assert_url('https://www.onlinetrade.ru/catalogue/klaviatury-c28/')
