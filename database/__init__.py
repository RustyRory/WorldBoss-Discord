# database/__init__.py

from .connection import create_connection
from .guilds import insert_guild, get_channel_wb_id, update_channel_wb_id, get_channel_city_id, update_channel_city_id, get_channel_graveyard_id, update_channel_graveyard_id, get_boss_id, update_boss_id, get_boss_level, update_boss_level, get_boss_damages, update_boss_damages, get_boss_timeout, update_boss_timeout, get_boss_time, update_boss_time, get_message_city_id, update_message_city_id, get_message_warrior_id, update_message_warrior_id, get_message_mage_id, update_message_mage_id, get_message_adventurer_id, update_message_adventurer_id, get_message_rogue_id, update_message_rogue_id, get_warrior_bank, update_warrior_bank, get_mage_bank, update_mage_bank, get_adventurer_bank, update_adventurer_bank, get_rogue_bank, update_rogue_bank
from .players import insert_player, get_player_by_id, update_player, delete_player  # Ajouter d'autres fonctions selon vos besoins
