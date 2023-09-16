import mysql.connector

from mysql.connector import Error

try:

    connection = mysql.connector.connect(

        host = "cis3368fall.cormgjdgnb98.us-east-1.rds.amazonaws.com", # this is your db endpoint address

        user = "admin", # username for MySQL db on AWS

        password = "2oranges4me", # password for MySQL db on AWS

        database = "cis3368falldb" # database name which we created in MySQL workbench.

    )

except Error as err:

    print("failure in establishing connection")

    exit()



print("connection successful")



cursor = connection.cursor(dictionary=True)

sql = "select * from Users"

cursor.execute(sql)



results = cursor.fetchall()



for datarow in results:

    print(f"firstname: {datarow['firstname']}, lastname: {datarow['lastname']}, email: {datarow['email']}")


