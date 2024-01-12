from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.group & filters.edited)
async def delete_edited_messages(client: Client, message: Message):
    # Delete the edited message
    await message.delete()
    await message.reply_text("Editing Message Deleted") 
