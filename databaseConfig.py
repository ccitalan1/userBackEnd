import mysql.connector


def connect_to_database():
    try:
        connection = mysql.connector.connect(user='root',
                                             password='rootPassword',
                                             host='localhost',
                                             database='test_database')
    except Exception as e:
        raise Exception("NO CONNECTION TO THE DATABASE", e)
    return connection


def close_connection(self):
    self.connection.close()
    print("MySQL connection is closed")
