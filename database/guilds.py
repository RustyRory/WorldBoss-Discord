# guilds.py

from .connection import create_connection  # Importer la fonction de connexion

def insert_guild(guild_id):
    """Insérer une nouvelle guilde dans la base de données."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT IGNORE INTO guilds (guild_id) VALUES (%s);"
        cursor.execute(query, (guild_id,))
        connection.commit()  # Commit ici pour ne pas causer de problèmes de synchronisation
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

# Getters pour les valeurs des guildes
def get_channel_wb_id(guild_id):
    """Récupérer le channel_wb_id d'une guilde."""
    connection = create_connection()
    channel_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT channel_wb_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            channel_id = result[0]
        cursor.close()
        connection.close()
    return channel_id

def update_channel_wb_id(guild_id, channel_wb_id):
    """Mettre à jour le channel_wb_id pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET channel_wb_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (channel_wb_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_channel_city_id(guild_id):
    """Récupérer le channel_city_id d'une guilde."""
    connection = create_connection()
    channel_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT channel_city_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            channel_id = result[0]
        cursor.close()
        connection.close()
    return channel_id

def update_channel_city_id(guild_id, channel_city_id):
    """Mettre à jour le channel_city_id pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET channel_city_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (channel_city_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")
        
def get_channel_graveyard_id(guild_id):
    """Récupérer le channel_graveyard_id d'une guilde."""
    connection = create_connection()
    channel_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT channel_graveyard_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            channel_id = result[0]
        cursor.close()
        connection.close()
    return channel_id

def update_channel_graveyard_id(guild_id, channel_graveyard_id):
    """Mettre à jour le channel_graveyard_id pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET channel_graveyard_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (channel_graveyard_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_boss_id(guild_id):
    """Récupérer l'ID du boss d'une guilde."""
    connection = create_connection()
    boss_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT boss_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            boss_id = result[0]
        cursor.close()
        connection.close()
    return boss_id

def update_boss_id(guild_id, boss_id):
    """Mettre à jour l'ID du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET boss_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (boss_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_boss_level(guild_id):
    """Récupérer le niveau du boss d'une guilde."""
    connection = create_connection()
    boss_level = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT level FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            boss_level = result[0]
        cursor.close()
        connection.close()
    return boss_level

def update_boss_level(guild_id, boss_level):
    """Mettre à jour le niveau du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET level = %s WHERE guild_id = %s;"
        cursor.execute(query, (boss_level, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_boss_damages(guild_id):
    """Récupérer les dégats du boss d'une guilde."""
    connection = create_connection()
    boss_damages = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT damages FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            boss_damages = result[0]
        cursor.close()
        connection.close()
    return boss_damages

def update_boss_damages(guild_id, boss_damages):
    """Mettre à jour les dégats du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET damages = %s WHERE guild_id = %s;"
        cursor.execute(query, (boss_damages, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_boss_timeout(guild_id):
    """Récupérer les dégats du boss d'une guilde."""
    connection = create_connection()
    boss_timeout = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT timeout FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            boss_timeout = result[0]
        cursor.close()
        connection.close()
    return boss_timeout

def update_boss_timeout(guild_id, boss_timeout):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET timeout = %s WHERE guild_id = %s;"
        cursor.execute(query, (boss_timeout, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_boss_time(guild_id):
    """Récupérer le time du boss d'une guilde."""
    connection = create_connection()
    boss_time = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT time FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            boss_time = result[0]
        cursor.close()
        connection.close()
    return boss_time

def update_boss_time(guild_id, boss_time):
    """Mettre à jour le time du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET time = %s WHERE guild_id = %s;"
        cursor.execute(query, (boss_time, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_message_city_id(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    message_city_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT city_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            message_city_id = result[0]
        cursor.close()
        connection.close()
    return message_city_id

def update_message_city_id(guild_id, message_city_id):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET city_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (message_city_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_message_warrior_id(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    message_warrior_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT warrior_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            message_warrior_id = result[0]
        cursor.close()
        connection.close()
    return message_warrior_id

def update_message_warrior_id(guild_id, message_warrior_id):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET warrior_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (message_warrior_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_message_mage_id(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    message_mage_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT mage_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            message_mage_id = result[0]
        cursor.close()
        connection.close()
    return message_mage_id

def update_message_mage_id(guild_id, message_mage_id):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET mage_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (message_mage_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_message_adventurer_id(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    message_adventurer_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT adventurer_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            message_adventurer_id = result[0]
        cursor.close()
        connection.close()
    return message_adventurer_id

def update_message_adventurer_id(guild_id, message_adventurer_id):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET adventurer_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (message_adventurer_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_message_rogue_id(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    message_rogue_id = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT rogue_id FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            message_rogue_id = result[0]
        cursor.close()
        connection.close()
    return message_rogue_id

def update_message_rogue_id(guild_id, message_rogue_id):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET rogue_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (message_rogue_id, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_warrior_bank(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    warrior_bank = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT warrior_bank FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            warrior_bank = result[0]
        cursor.close()
        connection.close()
    return warrior_bank

def update_warrior_bank(guild_id, warrior_bank):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET warrior_bank = %s WHERE guild_id = %s;"
        cursor.execute(query, (warrior_bank, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_mage_bank(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    mage_bank = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT mage_bank FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            mage_bank = result[0]
        cursor.close()
        connection.close()
    return mage_bank

def update_mage_bank(guild_id, mage_bank):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET mage_bank = %s WHERE guild_id = %s;"
        cursor.execute(query, (mage_bank, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_adventurer_bank(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    adventurer_bank = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT adventurer_bank FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            adventurer_bank = result[0]
        cursor.close()
        connection.close()
    return adventurer_bank

def update_adventurer_bank(guild_id, adventurer_bank):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET adventurer_bank = %s WHERE guild_id = %s;"
        cursor.execute(query, (adventurer_bank, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_rogue_bank(guild_id):
    """Récupérer le timeout du boss d'une guilde."""
    connection = create_connection()
    rogue_bank = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT rogue_bank FROM guilds WHERE guild_id = %s;"
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            rogue_bank = result[0]
        cursor.close()
        connection.close()
    return rogue_bank

def update_rogue_bank(guild_id, rogue_bank):
    """Mettre à jour le timeout du boss pour une guilde spécifique."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE guilds SET rogue_id = %s WHERE guild_id = %s;"
        cursor.execute(query, (rogue_bank, guild_id))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")