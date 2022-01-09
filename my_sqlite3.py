import sqlite3
from os import listdir, mkdir
from output_and_log import output

def check_for_db(file_name='chores.db'):
    folder_itmes = listdir('./')
    if 'db' not in folder_itmes:
        output('Creating ./db folder', 'info')
        mkdir('./db')

    folder_itmes = listdir('./db')
    if file_name in folder_itmes:
        return True
    else:
        return False


def create_db(file_name='chores.db'):
    # Creates a database if one doesn't exist.
    if check_for_db(file_name) is False:
        output(f'Creating sqlite3 database {file_name}.', 'info')
        connection = sqlite3.connect(f'./db/{file_name}')
        output(f'Sqlite3 database {file_name} created.', 'info')
        return True
    else:
        output(f'Failed to create Sqlite3 database ./db/{file_name}. File already exists.', 'error')
        return False


def connect_db(file_name='chores.db'):
    # Connects to and existing DB and returns the cursor
    # If the DB doesn't exist it returns "False"
    if check_for_db(file_name) is False:
        output('Failed to find ./db folder while trying to connect to the sqlite3 database. The folder ./db should be in the program root directory.', 'error')
        return False
    else:
        if check_for_db(file_name):
            connection = sqlite3.connect(f'./db/{file_name}')
            cursor1 = connection.cursor()
            return cursor1
        else:
            output(f'Trying to connect to sqlite3 database file ./db/{file_name} failed. Create the DB first.', 'error')
            return False


def create_tables(file_name='chores.db', tbl_name='', sql_cmd=''):
    cursor = connect_db(file_name)
    if cursor is False:
        return False
    else:
        # Get list of tables and check if it already exists
        output(f'Attempting to create table {tbl_name}.', 'info')
        sql1_cmd = f"SELECT name FROM sqlite_master WHERE type='table';"
        tbls = cursor.execute(sql1_cmd)
        tbls_list = []
        for x in tbls.fetchall():
            tbls_list.append(x[0])

        # If table exists fail with error and return False
        if tbl_name in tbls_list:
            output(f'Table creation failed. Table "{tbl_name}" already exists in "{file_name}" database.\n\tUse update table syntax to change table, or delete table and re-create it.', 'error')
            return False
        else:
            # Attempt to creat table
            try:
                cursor.execute(sql_cmd)
            except sqlite3.OperationalError as e:
                output(f'Error trying to creat table in {file_name}.\n\tAttempted command: {sql_cmd}\n\tError message: {e}', 'error')
                return False
            output(f'Table {tbl_name} created', 'info')
            return True


def check_for_user(user, cursor):
    cursor.execute(f'''SELECT user_name FROM users WHERE user_name="{user}"''')
    user1 = cursor.fetchone()  # retrieve the first row

    # If database in new and blank return False (name not already used)
    if user1==None:
        return False
    else:
        return True


def check_for_chore(chore, cursor):
    cursor.execute(f'''SELECT chore FROM chores WHERE chore="{chore}"''')
    chore1 = cursor.fetchone()  # retrieve the first row

    # If database in new and blank return False (name not already used)
    if chore1 == None:
        return False
    else:
        return True


def check_for_sub_chore(sub_chore, cursor):
    # Check if sub_chore is blank.
    if sub_chore == '':
        return True

    cursor.execute(f'''SELECT chore FROM chores WHERE chore="{sub_chore}"''')
    chore1 = cursor.fetchone()  # retrieve the first row

    # If database in new and blank return False (name not already used)
    if chore1 == None:
        output(f"Trying to assigne a sub_chore to a chore that doesn't exist. {sub_chore}", "info")
        return False

    # Not allowing nested chores. A chore with a sub_chore can't be a sub_chore
    cursor.execute(f'''SELECT sub_chore FROM chores WHERE chore="{sub_chore}"''')
    chore1 = cursor.fetchone()  # retrieve the first row

    if chore1[0] == '':
        return True
    else:
        print(chore1)
        output(f'Trying to assign a sub_chore to a chore that already has a sub_chore. {sub_chore=}')
        return False


def add_users(db_file='chores.db', user='', password='', admin=-1):
    cursor = connect_db(file_name=db_file)

    if user == '':
        output('Trying to create user with blank user name.', 'info')
        return False
    if (admin < 0) or (admin > 5):
        output(f'Trying to create user but admin is out of bounds. <0 or >5. {admin=}.', 'error')

    if check_for_user(user, cursor) is True:
        output(f'Trying to create a user that already exists. {user=}.', 'info')
        return False

    # add to users
    cursor.execute('''INSERT INTO users(user_name, password, is_admin)
                      VALUES(?,?,?)''', (user, password, admin))
    cursor.execute('commit')
    return True


def add_chore(db_file='chores.db', chore='', description='', sub_chore=''):
    cursor = connect_db(file_name=db_file)

    if chore == '':
        output('Trying to create chore with blank chore.', 'info')
        return False

    if description == '':
        output('Trying to create chore with blank description.', 'info')
        return False

    if check_for_chore(chore, cursor) is True:
        output(f'Trying to create a chore that already exists. {chore=}.', 'info')
        return False

    if check_for_sub_chore(sub_chore, cursor) is False:
        # Message in function
        return False

    # add to chores
    cursor.execute('''INSERT INTO chores(chore, description, sub_chore)
                          VALUES(?,?,?)''', (chore, description, sub_chore))

    cursor.execute('commit')
    return True


def add_assignment(db_file='chores.db', user='', chore='', days='', start_date='', end_date=''):
    cursor = connect_db(file_name=db_file)

    if user == '' or chore == '' or days == '' or start_date == '' or end_date == '':
        output(f'At least one key value blank to add assignment. {user=}, {chore=}, {days=}, {start_date=}, {end_date=}', 'info')
        return False

    if check_for_chore(chore, cursor) is False:
        output(f"Trying to make assignment with a chore that doesn't exist. {chore=}.", 'info')
        return False

    if check_for_user(user, cursor) is False:
        output(f"Trying to make assignment with a user that doesn't exist. {user=}.", 'info')
        return False

    # add assignment
    cursor.execute('''INSERT INTO assignment(user_name, chore, days, start_date, end_date)
                          VALUES(?,?,?,?,?)''', (user, chore, days, start_date, end_date))

    cursor.execute('commit')
    return True

