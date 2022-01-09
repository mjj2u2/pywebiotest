import my_sqlite3 as db
from output_and_log import output


# todo Make DB path based on db name. This is for multiple instances
def setup_new_db(db_name):

    """output(f'Creating new Slite3 database with name {db_name}.', 'info')
    if db.create_db(db_name) is False:
        return False

    output('Creating Tables', 'info')
    if db.create_tables(file_name=db_name, tbl_name='users', sql_cmd='''CREATE TABLE IF NOT EXISTS
        users(user_name MESSAGE_TEXT PRIMARY KEY, password TEXT, is_admin INTEGER)''') \
            is False:
        return False

    if db.create_tables(file_name=db_name, tbl_name='chores', sql_cmd='''CREATE TABLE IF NOT EXISTS
    chores(chore MESSAGE_TEXT PRIMARY KEY, description MESSAGE_TEXT, sub_chore MESSAGE_TEXT)''') \
            is False:
        return False

    if db.create_tables(file_name=db_name, tbl_name='assignment', sql_cmd='''CREATE TABLE IF NOT EXISTS
        assignment(user_name MESSAGE_TEXT, chore MESSAGE_TEXT, days MESSAGE_TEXT, start_date DATE,end_date DATE,
        FOREIGN KEY(user_name) REFERENCES users(user_name),
        FOREIGN KEY(chore) REFERENCES chores(chore))''') \
            is False:
        return False

    output('Tables created successfully', 'info')
    output(f'New database {db_name} created and tables configured correctly.', 'info')
    return True

    while True:

        name = input('What name do you want to put in? ')
        pas = input(f'What password do you want for {name}? ')
        admn = input(f'What level of admin do you want for {name}? ')
        print('inserting user')

        db.add_users(db_file=db_name, user=name, password=pas, admin=int(admn))
    """

    while True:

        user = input('What user do you want? ')
        chore = input('What chore do you want? ')
        days = input(f'What days do you want? ')
        start_date = input(f'What start_date? ')
        end_date = input(f'What end_date?')
        print('inserting assignment')

        db.add_assignment(db_file=db_name, user=user, chore=chore, days=days, start_date=start_date, end_date=end_date)


if __name__ == "__main__":
    if setup_new_db('sam2.db') is True:
        print('Created DB')
    else:
        print('DB creation failed. Please check logs.')
