from discord.ext import commands

async def handle_on_ready(bot):
    print(f'Bot {bot.user.name} est connecté et prêt.')

