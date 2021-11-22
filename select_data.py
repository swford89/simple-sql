from pprint import pprint

import sqlalchemy
from sqlalchemy.exc import NoSuchTableError

from db_setup import database_create

def select_data():
    """for reading data from the database"""
    
    while True:
        try:
            table_name = input('Enter the name of the table you would like to read from: ')
            specific_table = sqlalchemy.Table(table_name, metadata, autoload=True, autoload_with=engine)
            break
        except NoSuchTableError:
            print('''
            Your table either does not exist or is not spelled correctly. Try again.
            ''')

    query = sqlalchemy.select([specific_table])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    pprint(result_set)
    return

engine, connection, metadata = database_create()