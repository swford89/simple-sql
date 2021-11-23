from pprint import pprint

import sqlalchemy

from table_creation import create_table

def table_column_datatype():
    """get title for table and columns; get datatype for columns"""

    # initialize list for titles, datatypes
    column_titles_list = []
    column_datatype_list = []

    # define the table
    table_title = input('Enter a title for your table: ')
    while True:
        try:
            column_amount = int(input(f'Enter the number of columns table {table_title.upper()} needs: '))
            break
        except ValueError:
            print('''
            Please enter a number for the amount of columns this table needs.
            ''')

    # get the title of the columns
    for num in range(1, column_amount + 1):
        column_title = input(f'Enter a title for Column #{num} in table {table_title.upper()}: ')
        column_titles_list.append(column_title)

    # specify the datatype of the columns
    for column in column_titles_list:
        # print datatype menu
        for num, datatype in datatype_dict.items():
            print(f'{num}. {datatype}')

        while True:
            try:
                column_datatype = int(input(f'Enter the number corresponding to the datatype that column {column.upper()} requires: '))
                # confirm user entered correct value      
                if column_datatype in datatype_dict.keys():
                    print(f'''
                    Confirmed: Column title = {column.upper()} 
                    Confirmed: Datatype = {datatype_dict[column_datatype]}
                    ''')
                    # add the datetype to the list
                    column_object = datatype_dict[column_datatype]
                    column_datatype_list.append(column_object)
                    break
            except ValueError:
                print('''
                Please enter a number corresponding to your desired datatype.
                ''')
            except KeyError:
                print('''
                Please enter a valid number from the Datatype Menu
                ''')
    while True:
        print(f'Column titles: {column_titles_list}')
        primary_key = input('Enter the title of the column you would like to set as the primary key: ')
        if primary_key in column_titles_list:
            break

    # create dictionary to use for table creation
    table_data_dict = {
        'table_title': table_title,
        'column_titles': column_titles_list,
        'column_datatypes': column_datatype_list,
        'primary_key': primary_key
    }
    
    return table_data_dict

datatype_dict = {
    1: sqlalchemy.String(500),
    2: sqlalchemy.Integer(),
    3: sqlalchemy.Float(),
    4: sqlalchemy.Boolean()
}

table_data_dict = table_column_datatype()
create_table(table_data_dict)