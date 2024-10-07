import discord
from discord.ext import commands

# Remplacez 'YOUR_BOT_TOKEN' par votre vrai token du bot
TOKEN = 'MTE2NzE1MTM3NzkwNzE4Nzc1NA.G1apLs.fPItFX-lE16PeINJbbFGqu4y09mMXfBdY1k9tA'

# Créer des intents
intents = discord.Intents.default()
intents.message_content = True  # Permet de lire le contenu des messages

# On crée un objet "bot" avec un préfixe de commande (par exemple, "!")
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement qui s'active quand le bot se connecte à Discord
@bot.event
async def on_ready():
    print(f'{bot.user} est connecté à Discord!')

# Commande basique pour tester
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Lancer le bot
bot.run(TOKEN)
