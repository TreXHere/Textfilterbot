from pyrogram import Client, filters
from pyrogram.types import Message

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '21364355'
api_hash = '72f11aec1dd3e5764554d477341a3d0b'
bot_token = '6337104990:AAFxTIVSr3BtFxWEossUWZRbQIY4Dac8J4U'

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

ADMINS = [6574111464, 1600454750, 609517172, 2122515260]

@app.on_message(filters.group & filters.text & filters.user(ADMINS))
async def delete_font_messages(client: Client, message: Message):
    if message.text and not message.text.isascii():
        # If the message contains non-ASCII characters (indicating it's a font), delete it
        await message.delete()
        # Reply that fonts are not allowed
        await message.reply_text("BossNup Ultra Security No Font text allowed")


app.run()
