from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Keyboards_page(Base):

    availability_value = 'в наличии'
    producer_name = 'MICROSOFT'
    price_lower_border = 30
    item_type = 'мембранная'
    connection_type = 'беспроводная'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    availability = "//span[contains(text(), '" + availability_value + "')]"
    expand_producers_list = "//*[@id='columnBlock__producersFilterIDfilter__ID']/div[2]/div/a"
    producer = "//*[@id='mCSB_1_container']/ul/li[21]"  #Microsoft
    expand_price = "//div[@data-spoiledContent='price_active']"
    slider_left = "//div[@id='js__ot_priceRange']/span[1]"
    type = "//span[contains(text(), '" + item_type + "')]"
    connection = '//span[contains(text(), "беспроводная")]'
    show_filter_result = "//a[text()='показать']"
    search_result = "//div[@class='content__mainColumn content__itemsLoadingCover js__itemsLoadingCover']/div[2]/div[1]/div[2]/div[1]/a"

    # Getters

    def get_availability(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.availability)))

    def get_expand_producers_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.expand_producers_list)))

    def get_producer(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.producer)))

    def get_expand_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.expand_price)))

    def get_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_left)))

    def get_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type)))

    def get_connection(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.connection)))


    def get_show_filter_result(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_filter_result)))

    def get_search_result(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_result)))

    # Actions

    def click_availability(self):
        self.get_availability().click()
        print("Click availability: " + self.availability_value)

    def click_expand_producers_list(self):
        self.get_expand_producers_list().click()
        print("Click expand producers list")

    def click_producer(self):
        self.get_producer().click()
        print("Click producer: " + self.producer_name)

    def click_expand_price(self):
        self.get_expand_price().click()
        print("Click expand price")

    def click_type(self):
        self.get_type().click()
        print("Click type: " + self.item_type)

    def click_connection(self):
        self.get_connection().click()
        print("Click type: " + self.connection_type)

    def click_show_filter_result(self):
        self.get_show_filter_result().click()
        print("Click show result")


    # Methods

    def select_product_keyboard_multi_filters(self):
        self.get_current_url()
        self.click_availability()
        self.click_expand_producers_list()
        self.scroll_page_to_element(self.get_producer())
        self.click_producer()
        self.click_type()
        self.click_connection()
        self.click_expand_price()
        self.move_slider(self.get_slider_left(), self.price_lower_border, 0)
        self.click_show_filter_result()
        self.assert_word(self.get_search_result(), "Клавиатура Microsoft Bluetooth Keyboard Black (QSZ-00011)")
