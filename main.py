import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import database  # Assure-toi que le fichier database.py est dans le même répertoire

# Charger les variables d'environnement
load_dotenv()

# Configuration du bot Discord
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} est connecté et prêt à fonctionner!')

# Commande pour ajouter un joueur
@bot.command()
async def add_player(ctx, username: str, level: int):
    guild_id = str(ctx.guild.id)
    player_data = {
        "id": str(ctx.author.id),
        "username": username,
        "class": "N/A",
        "level": level,
        "life": 1000,
        "action": 5,
        "experience": 0,
        "golds": 0,
        "damages": 0,
        "donation": 0
    }
    database.insert_player(guild_id, player_data)
    await ctx.send(f"Le joueur **{username}** a été ajouté avec le niveau **{level}**.")

# Commande pour lister les joueurs
@bot.command()
async def list_players(ctx):
    guild_id = str(ctx.guild.id)
    players = database.get_players(guild_id)
    if players:
        players_list = "\n".join([f"{player[2]} (Level {player[4]})" for player in players])
        await ctx.send(f"Joueurs dans le serveur :\n{players_list}")
    else:
        await ctx.send("Aucun joueur trouvé pour ce serveur.")

# Commande pour configurer le bot
@bot.command()
async def set_config(ctx, channel_wb_id: str, channel_city_id: str, channel_graveyard_id: str):
    guild_id = str(ctx.guild.id)
    config_data = {
        "channelWBId": channel_wb_id,
        "channelCityId": channel_city_id,
        "channelGraveyardId": channel_graveyard_id
    }
    database.insert_config(guild_id, config_data)
    await ctx.send(f"Configuration enregistrée pour le serveur **{ctx.guild.name}**.")

# Commande pour ajouter un world boss
@bot.command()
async def add_worldboss(ctx, name: str, boss_id: str, level: int, damages: int):
    guild_id = str(ctx.guild.id)
    worldboss_data = {
        "name": name,
        "id": boss_id,
        "level": level,
        "damages": damages,
        "timeout": 20,  # valeur par défaut
        "interval": 45,  # valeur par défaut
        "cityId": "123456789",  # à adapter
        "warriorId": "123456789",  # à adapter
        "mageId": "123456789",  # à adapter
        "rogueId": "123456789",  # à adapter
        "adventurerId": "123456789",  # à adapter
        "warrior": 200000000,
        "mage": 200000000,
        "rogue": 200000000,
        "adventurer": 200000000
    }
    database.insert_worldboss(guild_id, worldboss_data)
    await ctx.send(f"World Boss **{name}** a été ajouté avec succès!")

# Lancer le bot
if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_TOKEN'))
