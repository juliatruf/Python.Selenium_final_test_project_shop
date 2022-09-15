from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Category_computers_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    subcategory_manipulators = "//span[text()='Манипуляторы и устройства ввода ']"
    current_breadcrumbs = "//span[@class='breadcrumbs__itemCurrent']"

    # Getters

    def get_select_subcategory_manipulators(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subcategory_manipulators)))

    def get_select_subcategory_breadcrumbs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_breadcrumbs)))

    # Actions

    def click_select_subcategory_manipulators(self):
        self.get_select_subcategory_manipulators().click()
        print("Click select subcategory ")

    # Methods

    def select_subcategory_manipulators(self):
        self.get_current_url()
        self.click_select_subcategory_manipulators()
        self.assert_word(self.get_select_subcategory_breadcrumbs(), 'Манипуляторы и устройства ввода')
