from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Search_results_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_name_1 = "//div[@class='content__mainColumn content__itemsLoadingCover js__itemsLoadingCover']/div[2]/div[1]/div[2]/div[1]/a"
    product_price = "//div[@class='content__mainColumn content__itemsLoadingCover js__itemsLoadingCover']/div[2]/div[1]/div[3]/div[1]/span"
    buy_product_button = "//div[@class='content__mainColumn content__itemsLoadingCover js__itemsLoadingCover']/div[2]/div[1]/div[3]/div[3]/a"
    popup_buy_title = "//div[@id='popup_buy']/div[1]/div[1]/h3"
    popup_buy_continue_button = "//a[@class=' js__popup__close']"
    header_basket_button = "//a[contains(@class, 'js__header__basketLink')]"
    main_word_basket = "//h1"

    # Getters

    def get_product_name_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name_1)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_buy_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_button)))

    def get_popup_buy_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popup_buy_title)))

    def get_popup_buy_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popup_buy_continue_button)))

    def get_header_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header_basket_button)))

    def get_main_word_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_basket)))

    # Actions

    def click_buy_product_button(self):
        self.get_buy_product_button().click()
        print("Click buy button")

    def click_popup_buy_continue_button(self):
        self.get_popup_buy_continue_button().click()
        print("Click continue button")

    def click_header_basket_button(self):
        self.get_header_basket_button().click()
        print("Click header basket button")

    # Methods

    def add_product_to_cart(self):
        self.get_current_url()
        self.set_item_local_storage('item_name', self.get_product_name_1().text)
        self.set_item_local_storage('item_price', self.get_product_price().text)
        self.click_buy_product_button()
        self.assert_word(self.get_popup_buy_title(), 'Товар добавлен в корзину «Основная»')

    def continue_shopping(self):
        self.get_current_url()
        self.click_popup_buy_continue_button()
        self.assert_word(self.get_buy_product_button(), "Оформить")

    def go_to_basket(self):
        self.get_current_url()
        self.click_header_basket_button() # Переход на страницу регистрации/логина
        self.click_header_basket_button() # Повторно - для пропуска шага регистрации/логина
        self.assert_word(self.get_main_word_basket(), "Корзина")
