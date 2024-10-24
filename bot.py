import discord
from discord.ext import commands
from config import TOKEN
from events.handle_on_ready import handle_on_ready
from events.handle_on_guild_join import handle_on_guild_join 

# Définir les intents
intents = discord.Intents.default()
intents.members = True  # Activer l'intent pour accéder aux membres
intents.message_content = True  # Activer l'intent pour le contenu des messages


# Créer une instance de bot avec un préfixe de commande et les intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    await handle_on_ready(bot)

# Événement lorsque le bot rejoint une guilde
@bot.event
async def on_guild_join(guild):
    await handle_on_guild_join(guild, bot)

# Démarrer le bot avec le token
bot.run(TOKEN)
