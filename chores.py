import csv
from pywebio import start_server, pin
import pywebio.output as o
import pywebio.input as i
import pywebio.session as s
import functools as f
from datetime import datetime, timedelta
import pandas as pd



def get_df(file):
    df = pd.read_csv(file)
    return df


def put_df(file, df):
    df.to_csv(file)



def check_form(data):
    if len(data['name']) == '':
        return ('name', 'Please enter your name.')
    if data['password'] == '':
        return ('password', 'Please enter your password.')

    df_users = get_df(logins_file)
    user = df_users[(df_users['Name'] == data['name']) & (df_users['Password'] == data['password'])]
    if len(user.index) > 0:
        return
    else:
        return ('password', 'Failed to login. Check name and password and try again.')


def login():
    o.put_markdown("# Welcome to Johnson's Chores")
    data = i.input_group("Please Login:", [
        i.input('Name', name='name', type='text'),
        i.input('Password', name='password', type='password')
    ], validate=check_form)

    return data['name']


def complete_chores(choice, f_user):
    if choice == 'Complain':
        o.put_text('No')
        return

    reader = csv.reader(open('assignments.csv'))
    rows = list(reader)

    new_list = []

    for x in rows:
        if x[0] == f_user:
            today = str(datetime.now().weekday())
            if today in x[2]:
                new_list.append({'label': x[1], 'value': x[1], 'selected': False})


    check = i.checkbox(label='Check the chore(s) you have completed and hit "Submit".', options=new_list)

    for x in check:
        for y in rows:
            if x in y[1]:
                if y[4] <= datetime.date(datetime.now()) + timedelta(days=1):
                    y[3] = datetime(2000, 1, 1)
                    y[4] = datetime(2000, 1, 2)
                elif y[3] == datetime.date(datetime.now()):
                    y[3] = datetime.date(datetime.now() + timedelta(days=1))


def list_chores(f_user):
    df_assign = pd.read_csv('assignments.csv', parse_dates=['Start_Date', 'End_Date'])
    o.put_markdown(f'## Here are your chores for today, {f_user}:')

    df_assign = df_assign.apply(lambda df_line: df_line[['Chore']] if((df_line['Name'] == f_user) & (df_line['Start_Date'] == pd.Timestamp(datetime.date(datetime.now())))) else None, axis=1)
    df_assign.dropna(inplace=True)
    chore_list = df_assign['Chore'].to_list()

    for x in chore_list:
        o.put_markdown(f'#### {x}')

def main():
    user = login()
    o.clear()
    o.put_markdown(f'# Welcome {user}!')
    list_chores(user)

    o.put_buttons(['Mark Chore Complete', 'Complain'], onclick=f.partial(complete_chores, f_user=user))
    # Now tests
    s.hold()


if __name__ == '__main__':
    assignment_file = 'assignments.csv'
    chores_file = 'chores.csv'
    logins_file = 'logins.csv'

    start_server(main, debug=True, ipaddress='10.0.0.20', port=8000, cdn=False)
