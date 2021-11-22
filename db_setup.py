import os

import sqlalchemy

# set up MYSQL database connection
def database_create():
    secret = os.environ['MYSQL_PASS']
    engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{secret}@localhost/TravelCompany')
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()
    return engine, connection, metadata