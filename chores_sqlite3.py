import sqlite3
from os import listdir

def create_db(file_name='chores.db'):
    # Creates a database if one doesn't exist.
    # If the DB does exist it returns "None"
    folder_itmes = listdir('./')
    if file_name in folder_itmes:
        return None
    else:
        connection = sqlite3.connect(file_name)
        return True



def connect_db(file_name='chores.db'):
    # Connects to and existing DB and returns the cursor
    # If the DB doesn't exist it returns "None"
    folder_itmes = listdir('./')
    if file_name in folder_itmes:
        connection = sqlite3.connect(file_name)
        cursor1 = connection.cursor()
        return cursor1
    else:
        return None


#Creat base table
def create_tables():
    cursor = connect_db()
    cmd = '''CREATE TABLE IF NOT EXISTS
    users(user_name MESSAGE_TEXT PRIMARY KEY, password TEXT, is_admin INTEGER)'''

    cursor.execute(cmd)

    cmd = '''CREATE TABLE IF NOT EXISTS
    chores(chore MESSAGE_TEXT PRIMARY KEY, description MESSAGE_TEXT, sub_chore MESSAGE_TEXT)'''

    cursor.execute(cmd)


    cmd = '''CREATE TABLE IF NOT EXISTS
    assignment(user_name MESSAGE_TEXT, chore MESSAGE_TEXT, days MESSAGE_TEXT, start_date DATE,end_date DATE,
    FOREIGN KEY(user_name) REFERENCES users(user_name),
    FOREIGN KEY(chore) REFERENCES chores(chore))'''

    cursor.execute(cmd)

    return cursor

def add_users():
    cursor = create_tables()
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
    cursor.execute('commit')


if __name__ == '__main__':
    add_users()