import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import Main_page
from pages.category_computers_page import Category_computers_page
from pages.subcategory_computers_manipulators_page import Subcategory_computers_manipulators_page
from pages.keyboards_page import Keyboards_page
from pages.search_results_page import Search_results_page
from pages.basket_page import Basket_page
from pages.checkout_page import Checkout_page

def test_select_category(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\jtrufanova\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test")

    mp = Main_page(driver)
    mp.select_category_name()

    computers = Category_computers_page(driver)
    computers.select_subcategory_manipulators()

    manipulators = Subcategory_computers_manipulators_page(driver)
    manipulators.select_manipulators_keyboards()

    keyboards = Keyboards_page(driver)
    keyboards.select_product_keyboard_multi_filters()

    srp = Search_results_page(driver)
    srp.add_product_to_cart()
    srp.continue_shopping()
    srp.go_to_basket()

    bp = Basket_page(driver)
    bp.check_product_name()
    bp.check_product_price()
    bp.check_total_sum_basket()
    bp.check_default_total_purchase()
    bp.checkout_basket()

    cp = Checkout_page(driver)
    cp.check_checkout_total_purchase()

    print("Finish Test")
    driver.execute_script("window.localStorage.clear();")
    time.sleep(5)
    driver.quit()
