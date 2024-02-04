import sqlite3

class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/katerynasoloviova/Work/prometheus-qa-auto' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        query = "SELECT sqlite_version();"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}';"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_quantity_by_id(self, product_id, quantity):
        query = f"UPDATE products SET quantity = {quantity} WHERE id = {product_id};"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_quantity_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id};"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, quantity):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {quantity});"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id};"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record   

    def insert_user(self, customer_id, name, address, city, postal_code, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({customer_id}, '{name}', '{address}', '{city}', '{postal_code}', '{country}');"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_user_by_id(self, customer_id):
        query = f"DELETE FROM customers WHERE id = {customer_id};"
        self.cursor.execute(query)
        self.connection.commit()

    def get_user_by_id(self, customer_id):
        query = f"SELECT id, name, address, city, postalCode, country FROM customers WHERE id = {customer_id};"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def select_orders_by_order_date_and_product_name(self, order_date, product_name):
        query = f"SELECT orders.id, orders.order_date, products.name \
                FROM orders \
                LEFT JOIN products ON orders.product_id = products.id \
                WHERE products.name = '{product_name}' and orders.order_date = '{order_date}';"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record   

    def insert_order(self, order_id, customer_id, product_id, order_date):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
            VALUES ({order_id}, {customer_id}, {product_id}, '{order_date}');"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_order_by_id(self, order_id):
        query = f"DELETE FROM orders WHERE id = {order_id};"
        self.cursor.execute(query)
        self.connection.commit()     


   