## © copyright infringement on Telugu coders 
## © @telugucoders

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import Bot as client
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["bcast"]))
async def bcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**ʙʀᴏᴀᴅᴄᴀsᴛ ɪs sᴛᴀʀᴛɪɴɢ 💞...**")
        if not message.reply_to_message:
            await wtf.edit("**ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ 😒**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ** \n\n**sᴇɴᴛ ɢʀᴏᴜᴘs:** `{sent}` Ƈɦɑᴛs \n**ғɑɩɭɘɗ ɪŋ:** {failed} ᴄʜᴀᴛs")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`ʙʀᴏᴀᴅᴄᴀsᴛ sᴜᴄᴄᴇssғᴜʟʟ` \n\n**sɘŋᴛ Ƭø:** `{sent}` Ƈɦɑᴛs \n**ғɑɩɭɘɗ ɪŋ:** {failed} Ƈɦɑᴛs")
