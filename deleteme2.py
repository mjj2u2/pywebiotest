import sqlite3

# Define connection and curson

con = sqlite3.connect('store_transaction.db')
cursor = con.cursor()


#Creat store table

cmd = '''CREATE TABLE IF NOT EXISTS
users(user_name MESSAGE_TEXT PRIMARY KEY, password TEXT, is_admin INTEGER)'''

cursor.execute(cmd)

cmd2 = '''CREATE TABLE IF NOT EXISTS
chores(chore MESSAGE_TEXT PRIMARY KEY, description MESSAGE_TEXT, sub_chore MESSAGE_TEXT)'''

cursor.execute(cmd2)


cmd3 = '''CREATE TABLE IF NOT EXISTS
assignment(user_name MESSAGE_TEXT, chore MESSAGE_TEXT, days MESSAGE_TEXT, start_date DATE,end_date DATE,
FOREIGN KEY(user_name) REFERENCES users(user_name),
FOREIGN KEY(chore) REFERENCES choress(chore))'''

cursor.execute(cmd3)

# add to users
cursor.execute("INSERT INTO users VALUES ('Mike', 'password', 1)")
cursor.execute("INSERT INTO users VALUES ('Timothy', 'password', 0)")
cursor.execute("INSERT INTO users VALUES ('Megan', 'password', 0)")

#add to chores
cursor.execute("""INSERT INTO chores VALUES ('Bathroom', 'Scrub the bathroom, sweep the floor. Wash the mirror, and clean the floor','Mirror,Floor,Toilet')""")
cursor.execute("""INSERT INTO chores VALUES ('Front room', 'Clean up the couches and floor and table.','')""")
cursor.execute("""INSERT INTO chores VALUES ('Mirror', 'Wash the mirror and lean no streaks.','')""")
cursor.execute("""INSERT INTO chores VALUES ('Floor', 'Sweep the floor, mop the floor.','')""")
cursor.execute("""INSERT INTO chores VALUES ('Toilet', 'Scrub the toilet inside and out.','')""")


# Get results
cursor.execute("SELECT * FROM users")

results = cursor.fetchall()
print(results)

# Get results
cursor.execute("SELECT * FROM chores")

results = cursor.fetchall()
print(results)

for x in results:
    if x[2] != '':
        my_list = x[2].split(',')
        for y in my_list:
            for z in results:
                if y in z[0]:
                    print(z)


