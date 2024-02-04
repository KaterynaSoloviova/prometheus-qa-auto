import time

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class BoardGamesShopPage(BasePage):
    URL = "https://desktopgames.com.ua/ua/"

    SEARCH_INPUT_ID = "autocomplete"
    SEARCH_BTN_CLASS = "search_btn"
    SPLENDOR_LINK_XPATH = "//a[@href='https://desktopgames.com.ua/ua/splendor-ua.html']"
    AVAILIBILITY_LABEL_XPATH = "//span[@id='in_stock_show']/a"
    ORDER_PRICE_LABEL_CLASS = "sum_display"
    INCREASE_ORDER_QNT_BTN_CLASS = "up"
    ITEM_QNT_ELEM_CLASS = "cart_quan"
    

    def __init__(self) -> None:
        super().__init__()

    def open(self):
        self.driver.get(BoardGamesShopPage.URL)

    def search_by_board_game_name(self, board_game_name):
        search_item_elem = self.driver.find_element(By.ID, BoardGamesShopPage.SEARCH_INPUT_ID)
        search_item_elem.send_keys(board_game_name)

        search_btn_elem = self.driver.find_element(By.CLASS_NAME, BoardGamesShopPage.SEARCH_BTN_CLASS)
        search_btn_elem.click()
        time.sleep(1)

    def select_splendor_game(self):
        link_elem = self.driver.find_element(By.XPATH, BoardGamesShopPage.SPLENDOR_LINK_XPATH)
        link_elem.click()

    def check_title(self, expected_title):
        print(self.driver.title)
        assert self.driver.title == expected_title


    def click_buy_btn(self):
        buy_btn_elem = self.driver.find_element(By.LINK_TEXT, "Купити")
        buy_btn_elem.click()
        time.sleep(1)

    def click_order_btn(self):
        place_order_btn_elem = self.driver.find_element(By.LINK_TEXT, "Оформити замовлення")
        place_order_btn_elem.click()
        time.sleep(1)

    def check_availibility(self, expected_text):
        availibility_label_elem = self.driver.find_element(By.XPATH, BoardGamesShopPage.AVAILIBILITY_LABEL_XPATH)
        print(availibility_label_elem.text)
        assert availibility_label_elem.text == expected_text
   
    def check_order_price(self, expected_price):
        price_label_elem = self.driver.find_element(By.CLASS_NAME, BoardGamesShopPage.ORDER_PRICE_LABEL_CLASS)
        print(price_label_elem.text)
        assert price_label_elem.text == expected_price

    def click_plus_btn(self):
        increase_order_qnt_btn_elem = self.driver.find_element(By.CLASS_NAME, BoardGamesShopPage.INCREASE_ORDER_QNT_BTN_CLASS)
        increase_order_qnt_btn_elem.click()
        time.sleep(1)

    def check_qnt_items(self, expected_qtn):
        item_qnt_elem = self.driver.find_element(By.CLASS_NAME, BoardGamesShopPage.ITEM_QNT_ELEM_CLASS)
        value = item_qnt_elem.get_attribute("value")
        print(value)
        assert value == expected_qtn