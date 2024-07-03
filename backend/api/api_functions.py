import pyodbc
import os

def connect_to_database():

    server = os.getenv('sql_server_name')
    database = os.getenv('sql_server_database')
    username = os.getenv('sql_server_username')
    password = os.getenv('sql_server_password')
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=' + server + ';'
                          'DATABASE=' + database + ';'
                          'UID=' + username + ';'
                          'PWD=' + password)
    cursor = cnxn.cursor()

    return cnxn, cursor
