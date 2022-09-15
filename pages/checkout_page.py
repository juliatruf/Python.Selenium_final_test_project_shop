from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    total_purchase_checkout = "//div[contains(@class, 'multicart__summStep2Message')]/div[3]/ul/li"

    # Getters

    def get_total_purchase_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_purchase_checkout)))

    # Methods

    def check_checkout_total_purchase(self):
        self.get_current_url()
        self.get_screenshot()
        step_1_total_purchase = self.get_item_local_storage('basket_total_purchase')
        step_2_total_purchase = self.get_price_integer(self.get_total_purchase_checkout())
        self.assert_success_test(str(step_2_total_purchase), step_1_total_purchase, "Checkout Total Purchase GOOD")
