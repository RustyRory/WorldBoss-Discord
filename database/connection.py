# database/connection.py

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    """Créer une connexion à la base de données."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        print("Connexion à la base de données réussie.")
    except Error as e:
        print(f"L'erreur '{e}' est survenue.")
    return connection
