import pytest
from modules.ui.page_objects.nova_poshta_page import NovaPoshtaPage

@pytest.mark.ui
def test_check_valid_shipmet_number_search():
    page = NovaPoshtaPage()

    page.open()
    page.search_by_shipment_number("59001084870951")

    page.click_dialog_btn()

    page.check_shipment_status("Отримано")
    page.check_detailed_shipment_info()

    page.close()

@pytest.mark.ui
def test_check_invalid_shipmet_number_search():
    page = NovaPoshtaPage()

    page.open()
    page.search_by_shipment_number("12345678901")

    page.check_error_message_content("Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609")

    page.close()
