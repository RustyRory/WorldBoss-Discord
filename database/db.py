import mysql.connector
from mysql.connector import Error
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def create_connection():
    """Créer une connexion à la base de données MySQL"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        print("Connexion à la base de données MySQL réussie")
    except Error as e:
        print(f"Erreur lors de la connexion à la base de données: {e}")
    return connection
