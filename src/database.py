import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

database = mysql.connector.connect(
    host = os.getenv('HOST_DB'),
    user = os.getenv('USER_DB'),
    password = '',
    database = os.getenv('DB_NAME')
)