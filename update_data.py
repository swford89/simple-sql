from sqlalchemy.exc import NoSuchTableError
import sqlalchemy

from db_setup import database_create

def update_data():
    """for updating an EXISTING record in our database"""

    # initialize the table
    while True:
        try:
            table_name = input('Enter the name of the table which contains your record: ')
            specific_table = sqlalchemy.Table(table_name, metadata, autoload=True, autoload_with=engine)
            break
        except NoSuchTableError:
            print('''
            Your table either does not exist or is not spelled correctly. Try again.
            ''')

    # define update data
    print(f'Column titles: {specific_table.columns.keys()}')
    update_column = input('Enter your update column: ')

    for column in specific_table.columns:
        while True:
            try:
                if update_column == column.name and isinstance(column.type, type(sqlalchemy.String())):
                    update_value = input('Enter your updated string value: ')
                elif update_column == column.name and isinstance(column.type, type(sqlalchemy.Integer())):
                    update_value = int(input('Enter your updated integer value: '))
                elif update_column == column.name and isinstance(column.type, type(sqlalchemy.Float())):
                    update_value = float(input('Enter your updated float value: '))
                elif update_column == column.name and isinstance(column.type, type(sqlalchemy.Boolean())):
                    update_value = bool(input('Enter your updated boolean value: '))
            except ValueError:
                print('Looks like an invalid datatype was entered. Try again.')
            else:
                break
    update_dict = {update_column: update_value}

    # define where filter
    print(f'Column titles: {specific_table.columns.keys()}')
    where_column = input('Enter your where column: ')

    for column in specific_table.columns:
        while True:
            try:
                if column.name == where_column and isinstance(column.type, type(sqlalchemy.String())):
                    where_value = input('Enter your where-filter string value: ')
                elif column.name == where_column and isinstance(column.type, type(sqlalchemy.Integer())):
                    where_value = int(input('Enter your where-filter integer value: '))
                elif column.name == where_column and isinstance(column.type, type(sqlalchemy.Float())):
                    where_value = float(input('Enter your where-filter float value: '))
                elif column.name == where_column and isinstance(column.type, type(sqlalchemy.Boolean())):
                    where_value = bool(input('Enter your where-filter boolean value: '))
            except ValueError:
                    print('Looks like an invalid datatype was entered. Try again.')
            else:
                break

    update_query = sqlalchemy.update(specific_table).values(**update_dict).where(
        specific_table.columns[where_column] == where_value)
    result_proxy = connection.execute(update_query)
    print('''
    Update Complete.
    ''')
    return

engine, connection, metadata = database_create()