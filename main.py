from pyrogram import Client
from pyrogram.types import ChatPrivileges
import asyncio
import random
from keep_alive import keep_alive

# Replace these with your actual values
API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"

app = Client("admin-bot", api_id=API_ID, api_hash=API_HASH)

# List of channel usernames or IDs
CHANNELS = ["channel_username_1", "channel_username_2", "channel_username_3"]

# Admin privileges to grant temporarily
admin_rights = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_invite_users=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_promote_members=False,
    can_manage_video_chats=True
)

# No privileges (to demote)
no_rights = ChatPrivileges(
    can_change_info=False,
    can_delete_messages=False,
    can_invite_users=False,
    can_restrict_members=False,
    can_pin_messages=False,
    can_promote_members=False,
    can_manage_video_chats=False
)

async def cycle_admins():
    await app.start()

    while True:
        # Choose a random channel from the list
        channel = random.choice(CHANNELS)

        try:
            # Get a list of participants
            async for member in app.get_chat_members(channel):
                user_id = member.user.id

                print(f"Promoting {user_id} in {channel}")
                await app.promote_chat_member(channel, user_id, admin_rights)
                await asyncio.sleep(3)
                print(f"Demoting {user_id} in {channel}")
                await app.promote_chat_member(channel, user_id, no_rights)
                await asyncio.sleep(3)
                break  # Only process 1 user per cycle
        except Exception as e:
            print(f"Error in {channel}: {e}")
            await asyncio.sleep(5)

    await app.stop()

if name == "main":
    keep_alive()  # Start Flask keep-alive
    asyncio.run(cycle_admins())
