# events.py

import discord
from database import insert_guild, get_channel_wb_id, get_boss_id  # Importez vos fonctions de gestion de base de données

async def handle_guild_join(guild, bot):
    """Gère l'ajout d'une guilde lors de son adhésion."""
    insert_guild(guild.id)  # Appel de la fonction d'insertion directement

    # Récupérer le channel_wb_id
    channel_wb_id = get_channel_wb_id(guild.id)

    if channel_wb_id:  # Vérifie si channel_wb_id n'est pas None
        channel_wb = bot.get_channel(int(channel_wb_id))
        if channel_wb:
            # Vérifie si un message avec boss_id existe
            boss_id = get_boss_id(guild.id)
            
            if boss_id:  # Vérifie si boss_id existe
                try:
                    # Tente de récupérer le message existant
                    message = await channel_wb.fetch_message(boss_id)
                    # Met à jour le message existant
                    await message.edit(content=f"Guilde {guild.name} ajoutée à la base de données !")
                    print(f"Message avec boss_id {boss_id} mis à jour dans le channel {channel_wb.name}.")
                except discord.NotFound:
                    # Si le message n'existe pas, envoie un nouveau message
                    new_message = await channel_wb.send(f"Guilde {guild.name} ajoutée à la base de données !")
                    # Met à jour le boss_id dans la base de données
                    update_boss_id(guild.id, new_message.id)
                    print(f"Nouveau message envoyé dans le channel {channel_wb.name} avec boss_id {new_message.id}.")
            else:
                # Si boss_id n'existe pas, envoie un nouveau message
                new_message = await channel_wb.send(f"Guilde {guild.name} ajoutée à la base de données !")
                # Met à jour le boss_id dans la base de données
                update_boss_id(guild.id, new_message.id)
                print(f"Nouveau message envoyé dans le channel {channel_wb.name} avec boss_id {new_message.id}.")
        else:
            # Si le channel_wb n'est pas trouvé, utilise le canal principal
            system_channel = guild.system_channel
            if system_channel:
                new_message = await system_channel.send(f"Serveur non initialisé. Allez à cette adresse pour le configurer http://...")
                print(f"Message de demande de config envoyé dans le canal principal.")
    else:
        # Envoie dans le canal principal si channel_wb_id est None
        system_channel = guild.system_channel
        if system_channel:
            new_message = await system_channel.send(f"Serveur non initialisé. Allez à cette adresse pour le configurer http://...")
            print(f"Message de demande de config envoyé dans le canal principal.")

async def send_messages_to_all_guilds(bot):
    """Envoyer des messages à tous les serveurs."""
    for guild in bot.guilds:
        await handle_guild_join(guild, bot)