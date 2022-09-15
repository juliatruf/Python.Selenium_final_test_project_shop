from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    product_name_basket = "//*[@id='tabs_cart']/form/table/tbody[2]/tr/td[3]/div[2]/a"
    product_price_basket = "//*[@id='tabs_cart']/form/table/tbody[2]/tr/td[5]/div/b"
    product_count_basket = "//input[@class='input__text js__itemIDCount']"
    sum_price_basket = "//*[@id='cartResultPrice__ID']/div[1]"
    total_sum_basket = "//*[@id='tabs_cart']/div[1]/div[3]/div[1]/b"
    default_shipment_price = "//tbody[@id='js__productpage_deliveryPoint']/tr/td[4]/b"
    default_total_purchase = "//div[@id='basket_paymenttypes__ID']/div/table/tbody/tr[1]/td[3]"
    submit_button = "//input[@name='submit']"
    #default_shipment_radio_button = "//tbody[@id='js__productpage_deliveryPoint']/tr[1]/td[1]/label"
    #default_payment_radio_button = "//div[@id='basket_paymenttypes__ID']/div/table/tbody/tr[1]/td[1]/label"
    main_word = "//h1"

    # Getters

    def get_product_name_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name_basket)))

    def get_product_price_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price_basket)))

    def get_product_count_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_count_basket)))

    def get_sum_price_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_price_basket)))

    def get_total_sum_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_sum_basket)))

    def get_default_shipment_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.default_shipment_price)))


    def get_default_total_purchase(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.default_total_purchase)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # def get_default_shipment_radio_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.default_shipment_radio_button)))
    # def get_default_payment_radio_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.default_payment_radio_button)))

    # Actions

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")

    # Methods

    def check_product_name(self):
        self.get_current_url()
        item_name_card = self.get_item_local_storage('item_name')
        self.assert_success_test(self.get_product_name_basket().text, item_name_card, "Basket Product Name GOOD")

    def check_product_price(self):
        item_price_card = self.get_item_local_storage('item_price')
        self.assert_success_test(self.get_product_price_basket().text, item_price_card, "Basket Product Price GOOD")

    def check_total_sum_basket(self):
        self.assert_success_test(self.get_product_price_basket().text, self.get_total_sum_basket().text,
                                 "Basket Total Sum GOOD")

    def check_default_total_purchase(self):
        shipment_price = self.get_price_integer(self.get_default_shipment_price())
        total_sum = self.get_price_integer(self.get_total_sum_basket())
        total_purchase = shipment_price + total_sum
        current_total_purchase = self.get_price_integer(self.get_default_total_purchase())
        self.assert_success_test(current_total_purchase, total_purchase, "Basket Total Purchase GOOD")

    def checkout_basket(self):
        self.get_screenshot()
        self.set_item_local_storage('basket_total_purchase', self.get_price_integer(self.get_default_total_purchase()))
        self.click_submit_button()
        self.assert_word(self.get_main_word(), "Оформление заказа")
