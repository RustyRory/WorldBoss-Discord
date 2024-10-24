import discord  # Ajoutez cette ligne pour importer le module discord
from discord.ext import commands
from database.db import create_connection
from database.queries import insert_guild

async def handle_on_guild_join(guild, bot):
    await bot.wait_until_ready()  # Assure que le bot est prêt avant de procéder

    owner_id = str(guild.owner.id) if guild.owner else "0"  # Récupérer le propriétaire

    # Création des channels
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=True)
    }
    channel_wb = await guild.create_text_channel('world-boss', overwrites=overwrites)
    channel_city = await guild.create_text_channel('city', overwrites=overwrites)
    channel_graveyard = await guild.create_text_channel('graveyard', overwrites=overwrites)

    # Envoi des messages dans les channels
    message_city = await channel_city.send("Message de la ville")
    message_warrior = await channel_city.send("Message pour les guerriers")
    message_mage = await channel_city.send("Message pour les mages")
    message_rogue = await channel_city.send("Message pour les voleurs")
    message_adventurer = await channel_city.send("Message pour les aventuriers")

    # Ajout dans la base de données
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        # Appeler la fonction insert_guild
        query, params = insert_guild(
            id_discord=str(guild.id),
            id_owner=owner_id,
            name=guild.name,
            channel_wb_id=str(channel_wb.id),
            channel_city_id=str(channel_city.id),
            channel_graveyard_id=str(channel_graveyard.id),
            level=1, damages=0, max_damages=0, all_damages=0,
            timeout=60, cycle=60,
            message_city_id=str(message_city.id),
            message_warrior_id=str(message_warrior.id),
            message_mage_id=str(message_mage.id),
            message_rogue_id=str(message_rogue.id),
            message_adventurer_id=str(message_adventurer.id),
            warrior_bank=0, mage_bank=0, rogue_bank=0, adventurer_bank=0
        )

        cursor.execute(query, params)
        connection.commit()
        cursor.close()
        connection.close()

    print(f"Guilde {guild.name} ajoutée avec succès à la base de données.")
