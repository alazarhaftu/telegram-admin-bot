import random
import asyncio
import os
from telethon.sync import TelegramClient
from telethon.tl.functions.channels
from telethon.tl.types import ChatAdminRights
from keep_alive import keep_alive

keep_alive()

api_id = int(os.environ['22367750'])
api_hash = os.environ['d66df1ff8f59b26a8542902ed6070d8f']

channel_a_list = ['ethiocrypto_433', 'man_united_ethio_fans', 'manchester_unitedfanns']  # Replace with your channels
channel_b = 'fothfu'  # Replace with your target channel

client = TelegramClient('session', api_id, api_hash)

async def get_valid_users_from_channel(channel_name):
    try:
        entity = await client.get_entity(channel_name)
        members = await client.get_participants(entity, limit=1000)

        valid_users = []
        for user in members:
            if user.bot or user.deleted or not user.username:
                continue
            valid_users.append(user)

        return valid_users
    except Exception as e:
        print(f"Error in {channel_name}: {e}")
        return []

async def main():
    await client.start()
    target = await client.get_entity(channel_b)

    all_users = []
    for chan in channel_a_list:
        users = await get_valid_users_from_channel(chan)
        all_users.extend(users)

    unique_users = {u.id: u for u in all_users}.values()
    unique_users = list(unique_users)
    random.shuffle(unique_users)

    admin_rights = ChatAdminRights(
        post_messages=True,
        delete_messages=True,
        ban_users=True,
        invite_users=True,
        add_admins=False,
        change_info=False,
        pin_messages=True,
    )

    empty_rights = ChatAdminRights()
    used_ids = set()

    while True:
        available = [u for u in unique_users if u.id not in used_ids]

        if not available:
            used_ids.clear()
            random.shuffle(unique_users)
            continue

        user = random.choice(available)
        used_ids.add(user.id)

        try:
            await client(EditAdmin(target, user.id, admin_rights, rank="Rotating Admin"))
            print(f"Promoted: {user.username}")
            await asyncio.sleep(3)

            await client(EditAdmin(target, user.id, empty_rights, rank=""))
            print(f"Demoted: {user.username}")
            await asyncio.sleep(3)

        except Exception as e:
            print(f"Error with {user.username}: {e}")
            continue

with client:
    client.loop.run_until_complete(main())
