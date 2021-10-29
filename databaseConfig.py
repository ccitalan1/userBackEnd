import mysql.connector

# def connect_to_database():
try:
    connection = mysql.connector.connect(user='root',
                                         password='myRootPassword',
                                         host='localhost',
                                         database='test_database')
    print("Connected")
except Exception as e:
    raise Exception("NO CONNECTION TO THE DATABASE", e)

# def close_connection(self):
connection.close()
print("MySQL connection is closed")
