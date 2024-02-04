import pytest
from modules.ui.page_objects.board_games_shop_page import BoardGamesShopPage

@pytest.mark.ui
def test_make_order():
    page = BoardGamesShopPage()

    page.open()
    page.search_by_board_game_name("Splendor")
    page.select_splendor_game()

    page.check_title("Настільна гра Розкіш українською | Купити карткову настільну гру Розкіш | Самовивіз і доставка | Ігромаг Україна купити за низькою ціною у Києві, Харкові, Дніпрі, Одесі, Львові, Запоріжжі, Україні | інтернет магазин Ігромаг (Igromag)")
    page.check_availibility("Є в магазині")
    page.click_buy_btn()

    page.click_order_btn()

    page.check_title("Ігромаг | Оформлення замовлення")
    page.check_order_price("1 399")

    page.close()

@pytest.mark.ui
def test_edit_order():
    page = BoardGamesShopPage()

    page.open()
    page.search_by_board_game_name("Splendor")
    page.select_splendor_game()

    page.check_title("Настільна гра Розкіш українською | Купити карткову настільну гру Розкіш | Самовивіз і доставка | Ігромаг Україна купити за низькою ціною у Києві, Харкові, Дніпрі, Одесі, Львові, Запоріжжі, Україні | інтернет магазин Ігромаг (Igromag)")
    page.click_buy_btn()

    page.click_plus_btn()
    page.check_qnt_items("2")
    page.click_order_btn()

    page.check_title("Ігромаг | Оформлення замовлення")
    page.check_order_price("2 798")

    page.close()