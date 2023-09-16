import mysql.connector
from mysql.connector import Error
import credentials
from sqlfunc import create_connection
from sqlfunc import execute_query
from sqlfunc import execute_read_query


myCreds = credentials.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
