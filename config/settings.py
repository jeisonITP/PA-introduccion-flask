from dotenv import load_dotenv
import os

# Carga el archivo .env a las variables
# de entorno
load_dotenv() 

MYSQL_HOSTNAME = os.environ.get('MYSQL_HOSTNAME')
MYSQ_USERNAME = os.environ.get('MYSQ_USERNAME')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_PORT = os.environ.get('MYSQL_PORT')