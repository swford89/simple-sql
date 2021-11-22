import sqlalchemy

from db_setup import database_create

def create_table(table_data_dict):
    """use data stored as dictionary to create table"""

    column_args_list = []

    for num in range(len(table_data_dict['column_titles'])):
        column_set = sqlalchemy.Column(table_data_dict['column_titles'][num], table_data_dict['column_datatypes'][num])
        if table_data_dict['primary_key'] == column_set.name:
            column_set = sqlalchemy.Column(table_data_dict['column_titles'][num], table_data_dict['column_datatypes'][num], primary_key=True)
            column_args_list.append(column_set)
        else:
            column_args_list.append(column_set)

    new_table = sqlalchemy.Table(table_data_dict['table_title'], metadata, *column_args_list)
    metadata.create_all(engine)
    print('''
    Table has successfully been created.
    ''')
    return 

engine, connection, metadata = database_create()