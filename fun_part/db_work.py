import sqlite3

class Db:
    def __init__(self):
        self.conn = sqlite3.connect("/home/dci-student/Desktop/Ola/Database/08-23Database/Data08.31/Warehouse2/Warehouse2/db/products.db")
        self.cursor = self.conn.cursor()

    def add_entry(self, values):
        self.cursor.execute(f"INSERT INTO products VALUES {values}")
        self.conn.commit()     
            
    def delete_entry(self, condition):
        self.cursor.execute(f"DELETE FROM products WHERE id={condition}")
        self.conn.commit() 
    
    def modify_entry(self, id, entry):
        title = entry[1]
        category = entry[2]
        price = entry[3]
        description = entry[4]
        date_added = entry[5]

        set_values = f"title = ?, category = ?, price = ?, description = ?, date_added = ?"
        condition = f"id = {id}"

        self.cursor.execute(f"UPDATE products SET {set_values} WHERE {condition}", (title, category, price, description, date_added))
        self.conn.commit()
    
    def view_entries(self, condition=None):
        query = f"SELECT * FROM products"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        entries = self.cursor.fetchall()
        return entries
    
    def get_entry(self, table, id):
        query = f"SELECT * FROM {table} WHERE id = {id}"
        self.cursor.execute(query)
        entry = self.cursor.fetchone()
        return entry
    
# db = Db() 
# for row in db.view_entries("products"):
#     print(row)