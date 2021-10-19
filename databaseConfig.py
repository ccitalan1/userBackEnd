import mysql.connector

try:
    connection = mysql.connector.connect(user='root',
                                 password='rootPassword',
                                 host='localhost',
                                 database='test_database')
except Exception as e:
    raise Exception("NO CONNECTION TO THE DATABASE", e)

connection.close()
