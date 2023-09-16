import mysql.connector
from mysql.connector import Error
import credentials
from sqlfunc import create_connection
from sqlfunc import execute_query
from sqlfunc import execute_read_query


myCreds = credentials.Creds
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

query = """INSERT INTO USERS (firstname, lastname)
values = (Thomas, Edison)"""

create_invoice_table = """
CREATE TABLE IF NOT EXISTS invoices(
    id INT AUTO_INCREMENT,
    amount INT,
    description VARCHAR(255) NOT NULL,
    user_id INTEGER NOT NULL FOREIGN KEY fk_user_id(user_id) REFERENCES users(id)
    PRIMARY KEY (id)
)"""
invoice_from_user = 1
invoice_amount = 50
invoice_description = "HARRY POTTER BOOKS"

execute_query(conn, create_invoice_table)

query = "INSERT INTO invoices (amount, description, user_id) VALUES (%s, '%s', %s)" % (invoice_amount, invoice_description, invoice_from_user)
execute_query(conn, query)

new_amount = 30
update_invoice_query = """
UPDATE invoices
SET amount = %s
WHERE id = 1""" % (new_amount)
execute_query(conn, update_invoice_query)

invoice_id_to_delete = 1
delete_statement = "DELETE FROM invoices WHERE id = %s" % (invoice_id_to_delete)
execute_query(conn, delete_statement)

delete_table_statement = "DROP TABLE invoices"
execute_query(conn, delete_table_statement)