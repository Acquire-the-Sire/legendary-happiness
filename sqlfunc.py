import mysql.connector
from mysql.connector import Error


## who ate all my ravioli

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(

            host = host_name,

            user = user_name,

            password = user_password,

            database = db_name

        )
        print("Connection to MySQL DB successful.")
    except Error as e:
        print(f"The error '{e}' has occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Successful query execution")
    except Error as e:
        print(f"The error '{e}' has occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' has occurred")
