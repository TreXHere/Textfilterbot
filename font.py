from telethon.sync import TelegramClient, events
from telethon.tl.types import MessageEntityMentionName
from telethon.tl import types
import re

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '21364355'
api_hash = '72f11aec1dd3e5764554d477341a3d0b'
bot_token = '6337104990:AAFxTIVSr3BtFxWEossUWZRbQIY4Dac8J4U'

# Create a Telethon client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Define an event handler to delete messages with fonts
@client.on(events.NewMessage)
async def delete_fonts(event):
    if event.message.entities:
        for entity in event.message.entities:
            if isinstance(entity, MessageEntityMentionName):
                continue  # Skip mentions
            if entity.type == 'text_link':
                continue  # Skip text links
            if entity.type == 'text_mention':
                continue  # Skip text mentions

            # Check if the message contains font-related entities
            if entity.type in ['bold', 'italic', 'underline', 'strikethrough', 'code', 'pre']:
                await event.message.delete()
                break

# Run the client
client.run_until_disconnected()
