# bot.py

import os  # Ajoutez cette ligne
import discord
from discord.ext import commands
from events import handle_guild_join, send_messages_to_all_guilds  # Importer la fonction

# Créez votre bot avec les intents nécessaires
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Autres parties de votre code...

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

    # Envoie des messages à tous les guildes enregistrées dans la base de données
    await send_messages_to_all_guilds(bot)  # Appelle la fonction pour traiter toutes les guildes

@bot.event
async def on_guild_join(guild):
    await handle_guild_join(guild, bot)  # Appelle la fonction depuis init.py

# Lancez le bot
bot.run(os.getenv("DISCORD_TOKEN"))
