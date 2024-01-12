import os
from dotenv import load_dotenv

load_dotenv('.env', override=True) 

USER_MSSQL = os.getenv('USER_MSSQL')
PASSWD_MSSQL = os.getenv('PASSWD_MSSQL')
DB_MSSQL = os.getenv('DB_MSSQL')
SERVER_MSSQL = os.getenv('SERVER_MSSQL')
PORT_MSSQL = int(os.getenv('PORT_MSSQL'))

