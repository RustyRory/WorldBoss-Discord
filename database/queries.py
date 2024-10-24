def insert_guild(
    id_discord, id_owner, name,
    channel_wb_id, channel_city_id, channel_graveyard_id,
    level, damages, max_damages, all_damages,
    timeout, cycle, message_city_id,
    message_warrior_id, message_mage_id,
    message_rogue_id, message_adventurer_id,
    warrior_bank, mage_bank, rogue_bank, adventurer_bank
):
    query = """
    INSERT INTO Guilds (
        id_discord, id_owner, name,
        channel_wb_id, channel_city_id, channel_graveyard_id,
        level, damages, max_damages, all_damages,
        timeout, cycle, message_city_id,
        message_warrior_id, message_mage_id,
        message_rogue_id, message_adventurer_id,
        warrior_bank, mage_bank, rogue_bank, adventurer_bank,
        created_at, updated_at
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, NOW(), NOW()
    )
    """

    params = (
        id_discord, id_owner, name,
        channel_wb_id, channel_city_id, channel_graveyard_id,
        level, damages, max_damages, all_damages,
        timeout, cycle, message_city_id,
        message_warrior_id, message_mage_id,
        message_rogue_id, message_adventurer_id,
        warrior_bank, mage_bank, rogue_bank, adventurer_bank
    )

    return query, params
