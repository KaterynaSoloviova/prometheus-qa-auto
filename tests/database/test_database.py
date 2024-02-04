import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"

@pytest.mark.database
def test_product_quantity_update():
    db = Database()
    product_id = 1
    quantity = 25
    db.update_product_quantity_by_id(product_id, quantity)
    water_quantity = db.select_product_quantity_by_id(product_id)

    assert water_quantity[0][0] == quantity

@pytest.mark.database
def test_product_insert():
    db = Database()
    product_id = 4
    quantity = 30
    db.insert_product(product_id, "печиво", "солодке", quantity)
    water_quantity = db.select_product_quantity_by_id(product_id)

    assert water_quantity[0][0] == quantity

@pytest.mark.database
def test_product_delete():
    db = Database()
    product_id = 99
    quantity = 999
    db.insert_product(product_id, "тестові", "дані", quantity)
    db.delete_product_by_id(product_id)
    quantity = db.select_product_quantity_by_id(product_id)

    assert len(quantity) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
    print(orders)