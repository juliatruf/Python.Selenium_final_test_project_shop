import datetime
import time
import re

from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\jtrufanova\\PycharmProjects\\finalProject\\screen\\' + name_screenshot)

    """Method scroll to an element"""

    def scroll_page_to_element(self, element):
        time.sleep(3)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        time.sleep(3)
        print("scrolled")

    """Method move slider"""

    def move_slider(self, slider, X, Y):
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(X, Y).release().perform()
        print("Price is changed")
        time.sleep(3)

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word: " + value_word)

    """Method assert success test"""

    def assert_success_test(self, current_value, intended_value, description):
        assert current_value == intended_value
        print("Success test: " + description)

    """Method get price integer"""

    def get_price_integer(self, value_string):
        price_string = value_string.text.replace(' ', '')
        price_integer = int(re.search(r'\d+', price_string).group(0))
        print("Price: ", price_integer)
        return price_integer

    """Method set item to local storage"""

    def set_item_local_storage(self, key, value):
        return self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    """Method get item from local storage"""

    def get_item_local_storage(self, key):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)
