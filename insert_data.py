from pprint import pprint

from sqlalchemy.exc import NoSuchTableError
import sqlalchemy

from db_setup import database_create

def insert_data():
    """for inserting a NEW record into our database"""

    field_list = []
    column_title_list = []
    column_field_dict = {}

    # initialize the necessary table
    while True:
        try:
            table_title = input('Enter the name of the table you would like to add data to: ')
            specific_table = sqlalchemy.Table(table_title, metadata, autoload=True, autoload_with=engine)
            break
        except NoSuchTableError:
            print('''
            Your table either does not exist or is not spelled correctly. Try again.
            ''')

    # print column titles and class object type to promt user to choose datatype this column requires 
    for column in specific_table.columns:
        print(f'''
        Full column: {column}
        Column title: {column.name}
        Column datatype: {column.type}
        ''')

        # get field values the user wants to enter in
        while True:
            try:
                if isinstance(column.type, type(sqlalchemy.String())): 
                    field_value = input(f'Enter a string value for column {column.name.upper()}: ')
                    field_list.append(field_value)
                    column_title_list.append(column.name)
                    break
                elif isinstance(column.type, type(sqlalchemy.Integer())):
                    field_value = int(input(f'Enter an integer value for column {column.name.upper()}: '))
                    field_list.append(field_value)
                    column_title_list.append(column.name)
                    break
                elif isinstance(column.type, type(sqlalchemy.Float())):
                    field_value = float(input(f'Enter the float value for column {column.name.upper()}: '))
                    field_list.append(field_value)
                    column_title_list.append(column.name)
                    break
                elif isinstance(column.type, type(sqlalchemy.Boolean())):
                    field_value = bool(input(f'Enter a boolean value for column {column.name.upper()}'))
                    field_list.append(field_value)
                    column_title_list.append(column.name)
                    break
            except ValueError:
                print('Looks like you entered in an invalid datatype. Try again.')

    for index, title in enumerate(column_title_list):
            column_field_dict[title] = field_list[index]

    pprint(f'Dictionary of column titles and values to insert: {column_field_dict}')                

    insert_query = sqlalchemy.insert(specific_table).values(**column_field_dict)
    result_proxy = connection.execute(insert_query)
    print('''
    Insert Complete.
    ''')
    return

engine, connection, metadata = database_create()