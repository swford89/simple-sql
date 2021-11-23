# simple-sql
A command-line program for reading from, adding to, or updating an existing database with Python

## setup
1. `pipenv install` dependencies in the Pipfile, while in your project directory
2. connect to an existing database through db_setup.py

## overview
- db_setup.py ---------> establish connection to an existing database
- menu_select.py ------> choose what action you'd like to execute
- select_data.py ------> read data from a database
- table_setup.py ------> setup table title and datatypes
- table_creation.py ---> execute the creation of your table
- insert_data.py ------> add new data to a database
- update_data.py ------> update an existing record in a database