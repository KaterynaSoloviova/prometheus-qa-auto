import time

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class NovaPoshtaPage(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk/"
    SHIPMENT_INPUT_ID = "en"
    SEARCH_BTN_ID = "np-number-input-desktop-btn-search-en"
    OK_BTN_XPATH = "//*[@id='chat']/div[2]/button"
    SHIPMENT_STATUS_XPATH = '//*[@id="np-chat-messages-area-show-all-messages"]/div/div[2]/div/div[1]/section[1]/div/div[2]/span'
    DETAILED_INFO_LINK_XPATH = '//*[@id="np-chat-messages-area-show-all-messages"]/div/div[2]/div/div[1]/section[2]/div[1]/span'
    ERROR_MASSAGE_XPATH = '//*[@id="np-number-input-desktop-message-error-message"]/span'

    def __init__(self) -> None:
        super().__init__()

    def open(self):
        self.driver.get(NovaPoshtaPage.URL)

    def search_by_shipment_number(self, shipment_number):
        shipment_number_elem = self.driver.find_element(By.ID, NovaPoshtaPage.SHIPMENT_INPUT_ID)
        shipment_number_elem.send_keys(shipment_number)

        search_btn_elem = self.driver.find_element(By.ID, NovaPoshtaPage.SEARCH_BTN_ID)
        search_btn_elem.click()
        time.sleep(3)

    def click_dialog_btn(self):
        ok_btn_elem = self.driver.find_element(By.XPATH, NovaPoshtaPage.OK_BTN_XPATH)
        ok_btn_elem.click()

    def check_shipment_status(self, expected_status):
        status_elem = self.driver.find_element(By.XPATH, NovaPoshtaPage.SHIPMENT_STATUS_XPATH)
        assert status_elem.text == expected_status

    def check_detailed_shipment_info(self):
        detailed_info_elem = self.driver.find_element(By.XPATH, NovaPoshtaPage.DETAILED_INFO_LINK_XPATH)
        detailed_info_elem.click()
        
    def check_error_message_content(self, expected_message):
        message_elem = self.driver.find_element(By.XPATH, NovaPoshtaPage.ERROR_MASSAGE_XPATH)
        assert message_elem.text == expected_message