import sqlite3

connection = sqlite3.connect('dostavka.db')
sql = connection.cursor()


sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, '
            'pr_photo TEXT);')


class Data:
    def __init__(self):
        self.connection = sqlite3.connect('dostavka.db')
        self.sql = self.connection.cursor()

    def add_product(self, pr_name, pr_photo):
        self.sql.execute('INSERT INTO products '
                        '(pr_name,pr_photo) VALUES (?,?);',
                        (pr_name, pr_photo))

        # Зафиксировать
        self.connection.commit()

    def show_all_products(self):
        all_products = self.sql.execute('SELECT pr_name FROM products;').fetchall()

        return [i[0] for i in all_products]

    def get_current_product(self, product_name):
        current_product = self.sql.execute('SELECT pr_name, pr_photo '
                                           'FROM products WHERE pr_name=?;', (product_name,)).fetchone()
        return current_product