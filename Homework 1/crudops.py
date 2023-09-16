from sql import create_connection
from credentials import Creds
create_connection(Creds.conString, Creds.dbName, Creds.userName)