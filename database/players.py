# database/players.py

from .connection import create_connection

def insert_player(player_id, guild_id, player_class, level, life, action, experience, golds, damages, donation):
    """Insérer un nouveau joueur dans la base de données."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        INSERT INTO players (player_id, guild_id, class, level, life, action, experience, golds, damages, donation)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (player_id, guild_id, player_class, level, life, action, experience, golds, damages, donation))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def get_player_by_id(player_id):
    """Récupérer les informations d'un joueur par son ID."""
    connection = create_connection()
    player_info = None
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM players WHERE player_id = %s;"
        cursor.execute(query, (player_id,))
        result = cursor.fetchone()
        if result:
            player_info = {
                "player_id": result[0],
                "guild_id": result[1],
                "class": result[2],
                "level": result[3],
                "life": result[4],
                "action": result[5],
                "experience": result[6],
                "golds": result[7],
                "damages": result[8],
                "donation": result[9],
            }
        cursor.close()
        connection.close()
    return player_info

def update_player(player_id, level=None, life=None, action=None, experience=None, golds=None, damages=None, donation=None):
    """Mettre à jour les informations d'un joueur."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE players SET "
        updates = []
        params = []
        
        if level is not None:
            updates.append("level = %s")
            params.append(level)
        if life is not None:
            updates.append("life = %s")
            params.append(life)
        if action is not None:
            updates.append("action = %s")
            params.append(action)
        if experience is not None:
            updates.append("experience = %s")
            params.append(experience)
        if golds is not None:
            updates.append("golds = %s")
            params.append(golds)
        if damages is not None:
            updates.append("damages = %s")
            params.append(damages)
        if donation is not None:
            updates.append("donation = %s")
            params.append(donation)

        if updates:
            query += ", ".join(updates)
            query += " WHERE player_id = %s;"
            params.append(player_id)
            cursor.execute(query, tuple(params))
            connection.commit()

        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")

def delete_player(player_id):
    """Supprimer un joueur de la base de données."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM players WHERE player_id = %s;"
        cursor.execute(query, (player_id,))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Erreur lors de la connexion à la base de données.")
