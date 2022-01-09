import sqlite3

# Define connection and curson

con = sqlite3.connect('store_transaction.db')
cursor = con.cursor()


#Creat store table

cmd = '''CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)'''

cursor.execute(cmd)

cmd2 = '''CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))'''

cursor.execute(cmd2)

# add to stores
cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis, MN')")
cursor.execute("INSERT INTO stores VALUES (95, 'Chicago, IL')")
cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City, IA')")

#add to purchase
cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

# Get results
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

# update row
cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")

# Get results
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

# Delete
cursor.execute("DELETE FROM purchases WHERE purchase_id =54")

# Get results
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)
