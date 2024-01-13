from telethon.sync import TelegramClient, events
from telethon.tl import types
import re

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '21364355'
api_hash = '72f11aec1dd3e5764554d477341a3d0b'
bot_token = '6337104990:AAFxTIVSr3BtFxWEossUWZRbQIY4Dac8J4U'

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)


async def is_font_message(message):
    if isinstance(message, types.Message):
        text = message.text
        # Check if the message contains font characters
        if re.search(r'[\u2100-\u214F]', text):
            return True
    return False


@client.on(events.NewMessage)
async def handle_new_message(event):
    message = event.message
    if await is_font_message(message):
        await message.delete()


client.run_until_disconnected()
