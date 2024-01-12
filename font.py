from pyrogram import Client, filters
from pyrogram.types import Message
from config import app 

ADMINS = [6574111464, 1600454750, 609517172, 2122515260]

@app.on_message(filters.group & filters.text & filters.user(ADMINS))
async def delete_font_messages(client: Client, message: Message):
    if message.text and not message.text.isascii():
        # If the message contains non-ASCII characters (indicating it's a font), delete it
        await message.delete()
        # Reply that fonts are not allowed
        await message.reply_text("BossNup Ultra Security No Font text allowed")


