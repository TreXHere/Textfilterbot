from pyrogram import Client, filters
from pyrogram.types import Message

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '21364355'
api_hash = '72f11aec1dd3e5764554d477341a3d0b'
bot_token = '6337104990:AAFxTIVSr3BtFxWEossUWZRbQIY4Dac8J4U'

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

ADMINS = [6574111464, 1600454750, 609517172, 2122515260]


def contains_font(text):
    # Check if the message contains non-ASCII characters (indicating it's a font)
    return not all(char.isascii() or char in (' ', '\n') for char in text)


@app.on_message(filters.group & filters.text & ~filters.user(app.me))
async def delete_font_messages(client: Client, message: Message):
    has_emoji = any(char.isemoji() for char in message_text)
    if not has_emoji and contains_font(message.text):
        # If the message contains non-ASCII characters (indicating it's a font), delete it
        await message.delete()
        # Reply and mention the sender    
        await message.reply_text(f"**Font Deleted**")

app.run()
