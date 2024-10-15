import mysql.connector
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Connexion à la base MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    return connection

# Fonction pour créer les tables (au cas où elles n'existent pas)
def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS players (
        player_id VARCHAR(50) PRIMARY KEY,
        guild_id VARCHAR(50),
        username VARCHAR(100),
        class VARCHAR(50),
        level INT,
        life INT,
        action INT,
        experience INT,
        golds INT,
        damages INT,
        donation INT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS config (
        guild_id VARCHAR(50) PRIMARY KEY,
        channel_wb_id VARCHAR(50),
        channel_city_id VARCHAR(50),
        channel_graveyard_id VARCHAR(50)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS worldboss (
        guild_id VARCHAR(50) PRIMARY KEY,
        name VARCHAR(100),
        boss_id VARCHAR(50),
        level INT,
        damages INT,
        timeout INT,
        time INT,
        city_id VARCHAR(50),
        warrior_id VARCHAR(50),
        mage_id VARCHAR(50),
        rogue_id VARCHAR(50),
        adventurer_id VARCHAR(50),
        warrior_life BIGINT,
        mage_life BIGINT,
        rogue_life BIGINT,
        adventurer_life BIGINT
    )''')

    connection.commit()
    cursor.close()
    connection.close()

# Insérer un joueur dans la base de données
def insert_player(guild_id, player):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO players 
        (player_id, guild_id, username, class, level, life, action, experience, golds, damages, donation) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        ON DUPLICATE KEY UPDATE
        username=VALUES(username), class=VALUES(class), level=VALUES(level), life=VALUES(life), action=VALUES(action), experience=VALUES(experience), golds=VALUES(golds), damages=VALUES(damages), donation=VALUES(donation)''',
                   (player["id"], guild_id, player["username"], player["class"], player["level"],
                    player["life"], player["action"], player["experience"], player["golds"],
                    player["damages"], player["donation"]))

    connection.commit()
    cursor.close()
    connection.close()

# Insérer ou mettre à jour la configuration
def insert_config(guild_id, config_data):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO config (guild_id, channel_wb_id, channel_city_id, channel_graveyard_id) 
        VALUES (%s, %s, %s, %s) 
        ON DUPLICATE KEY UPDATE
        channel_wb_id=VALUES(channel_wb_id), channel_city_id=VALUES(channel_city_id), channel_graveyard_id=VALUES(channel_graveyard_id)''',
                   (guild_id, config_data["channelWBId"], config_data["channelCityId"], config_data["channelGraveyardId"]))

    connection.commit()
    cursor.close()
    connection.close()

# Insérer ou mettre à jour un world boss
def insert_worldboss(guild_id, worldboss_data):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO worldboss 
        (guild_id, name, boss_id, level, damages, timeout, time, city_id, warrior_id, mage_id, rogue_id, adventurer_id, warrior_life, mage_life, rogue_life, adventurer_life) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        ON DUPLICATE KEY UPDATE
        name=VALUES(name), boss_id=VALUES(boss_id), level=VALUES(level), damages=VALUES(damages), timeout=VALUES(timeout), time=VALUES(time), city_id=VALUES(city_id), warrior_id=VALUES(warrior_id), mage_id=VALUES(mage_id), rogue_id=VALUES(rogue_id), adventurer_id=VALUES(adventurer_id), warrior_life=VALUES(warrior_life), mage_life=VALUES(mage_life), rogue_life=VALUES(rogue_life), adventurer_life=VALUES(adventurer_life)''',
                   (guild_id, worldboss_data["name"], worldboss_data["id"], worldboss_data["level"],
                    worldboss_data["damages"], worldboss_data["timeout"], worldboss_data["time"],
                    worldboss_data["cityId"], worldboss_data["warriorId"], worldboss_data["mageId"],
                    worldboss_data["rogueId"], worldboss_data["adventurerId"], worldboss_data["warrior"],
                    worldboss_data["mage"], worldboss_data["rogue"], worldboss_data["adventurer"]))

    connection.commit()
    cursor.close()
    connection.close()

# Exemple de récupération des joueurs
def get_players(guild_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM players WHERE guild_id = %s', (guild_id,))
    players = cursor.fetchall()
    cursor.close()
    connection.close()
    return players

