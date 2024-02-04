import pytest
from modules.common.database import Database

@pytest.mark.database
def test_user_insert():
    db = Database()
    user_id = 25
    db.insert_user(user_id, "Wolfeschlegelsteinhausenbergerdörff", "Taumatawhakatangihangakoauauotamateaturipukakapiki-maungahoronukupokaiwhenuakitanatahu Str. 1", "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch", "0244", "New Zeland")
    user = db.get_user_by_id(user_id)

    assert user[0][0] == user_id
    assert user[0][1] == "Wolfeschlegelsteinhausenbergerdörff"
    assert user[0][2] == "Taumatawhakatangihangakoauauotamateaturipukakapiki-maungahoronukupokaiwhenuakitanatahu Str. 1"
    assert user[0][3] == "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
    assert user[0][4] == "0244"
    assert user[0][5] == "New Zeland"

@pytest.mark.database
def test_product_negative_quantity_update():
    db = Database()
    product_id = 2
    db.update_product_quantity_by_id(product_id, -100)
    quantity = db.select_product_quantity_by_id(product_id)

    assert quantity[0][0] == -100

@pytest.mark.database
def test_product_float_quantity_update():
    db = Database()
    product_id = 2
    db.update_product_quantity_by_id(product_id, 100.314)
    quantity = db.select_product_quantity_by_id(product_id)

    assert quantity[0][0] == 100.314

@pytest.mark.database
def test_user_delete():
    db = Database()
    user_id = 30
    db.insert_user(user_id, "Tarzan", "Rainforest", "Congo Basin", "123", "Cameroon")
    db.delete_user_by_id(user_id)
    user = db.get_user_by_id(user_id)

    assert len(user) == 0

@pytest.mark.database
def test_filter_orders_by_order_date_and_product_name():
    db = Database()
    product_id = 14
    user_id1 = 26
    user_id2 = 27
    order_id1 = 333
    order_id2 = 334
    db.insert_product(product_id, "apple", "Golden bio", 100)
    db.insert_user(user_id1, "Steve Rogers", "569 Leaman Place", "New York", "11211", "USA")
    db.insert_user(user_id2, "Bruce Banner", "Rocinha Street 29", "Rocinha Favela", "22451", "Brazil")
    db.insert_order(order_id1, user_id1, product_id, "2024-01-14 12:30:00")
    db.insert_order(order_id2, user_id2, product_id, "2024-01-14 12:30:00")
    orders = db.select_orders_by_order_date_and_product_name("2024-01-14 12:30:00", "apple")
    
    assert len(orders) == 2
    assert orders[0][0] == order_id1
    assert orders[0][1] == "2024-01-14 12:30:00"
    assert orders[0][2] == "apple"
    assert orders[1][0] == order_id2
    assert orders[1][1] == "2024-01-14 12:30:00"
    assert orders[1][2] == "apple"

    db.delete_order_by_id(order_id1)
    db.delete_order_by_id(order_id2)