import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import Main_page


@pytest.mark.run(order=2)
def test_select_location_city_from_list(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\jtrufanova\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test")

    mp = Main_page(driver)
    mp.select_location_city()

    print("Finish Test")
    time.sleep(3)
    driver.quit()


@pytest.mark.run(order=1)
def test_select_location_no_city_from_list(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\jtrufanova\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test")

    mp = Main_page(driver)
    mp.select_location_no_city_from_list()

    print("Finish Test")
    time.sleep(3)
    driver.quit()
