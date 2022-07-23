#POWERED BY TELUGU CODERS

from modules.cache.admins import admins
from modules.clientbot import call_py, bot
from pyrogram import Client, filters
from modules.codersdesign.thumbnail import thumb
from modules.clientbot.queues import QUEUE, clear_queue
from modules.helpers.filters import other_filters
from modules.helpers.command import commandpro as command
from modules.helpers.decorators import authorized_users_only
from modules.clientbot.utils import skip_current_song, skip_item
from modules.config import BOT_USERNAME, GROUP, IMG_5, NETWORK
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


@Client.on_message(command(["/reload", f"/reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        f"**💖 sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇʟᴏᴀᴅᴇᴅ ᴍᴜsɪᴄ ʙᴏᴛ.\n💞 sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇʟᴏᴀᴅᴇᴅ ᴀᴅᴍɪɴ ʟɪsᴛ.\n╰ ᴍᴜsɪᴄ ʙᴏᴛ ʀᴇʟᴏᴀᴅᴇᴅ ᴀᴅᴍɪɴ ʙʏ: {message.from_user.mention()}**"
    )


@Client.on_message(command(["/skip", f"/skip@{BOT_USERNAME}", "/vskip"]) & other_filters)
@authorized_users_only
async def skip(c: Client, m: Message):
    await m.delete()
    user_id = m.from_user.id
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await c.send_message(chat_id, "**ɴᴏᴛʜɪɴɢ ᴛᴏ ᴘʟᴀʏ ʙᴀʙʏ 👶..**")
        elif op == 1:
            await c.send_message(chat_id, "ʏᴏᴜʀ ǫᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ ʙʏᴇ ɪᴀᴍ ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ (ᴠᴄ)😌..")
        elif op == 2:
            await c.send_message(chat_id, "**ɪᴀᴍ ᴄʟᴇᴀʀɪɴɢ ʏᴏᴜʀ ǫᴜᴇᴜᴇs ʙʏᴇ ɪᴀᴍ ʟᴇᴀᴠɪɴɢ ᴠᴄ ʙᴀʙʏ....**")
        else:
            buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="🗑 ʙɪɴ",
                            callback_data="set_close")

                ]
            ]
        )
 
            thumbnail = f"{IMG_5}"
            title = f"{op[0]}"
            userid = m.from_user.id
            image = await thumb(thumbnail, title, userid)
            await c.send_photo(
                chat_id,
                photo=image,
                reply_markup=buttons,
                caption=f"🥳 **sᴋɪᴘᴘᴇᴅ ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴏɴɢ.\n╰ ᴍᴜsɪᴄ sᴋɪᴘᴘᴇᴅ ʙʏ: {m.from_user.mention()}**",
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **ɪᴀᴍ ʀᴇᴍᴏᴠᴇᴅ sᴏɴɢ ғʀᴏᴍ ǫᴜᴇᴜᴇ\n ᴛʜᴀɴᴋ ʏᴏᴜ ❤🌹:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["/stop", f"/stop@{BOT_USERNAME}", "/end", f"/end@{BOT_USERNAME}", "/vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**ɪᴀᴍ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ ғʀᴏᴍ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ**")
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("🔥 **ɴᴏᴛʜɪɴɢ ɪs sᴛʀᴇᴀᴍɪɴɢ ʜᴇʀᴇ 😒...**")


@Client.on_message(
    command(["/pause", f"/pause@{BOT_USERNAME}", "/vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**🌹 sᴜᴄᴄᴇssғᴜʟʟʏ ᴘᴀᴜsᴇᴅ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ sᴏɴɢ.\n╰ ᴍᴜsɪᴄ ᴘᴀᴜsᴇᴅ ʙʏ: {m.from_user.mention()}**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("🔥 **ɴᴏᴛʜɪɴɢ ɪs sᴛʀᴇᴀᴍɪɴɢ ʜᴇʀᴇ 😒 ...**")


@Client.on_message(
    command(["/resume", f"/resume@{BOT_USERNAME}", "/vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**👻 sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴜᴍᴇᴅ ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ sᴏɴɢ.\n╰ ᴍᴜsɪᴄ ʀᴇsᴜᴍᴇᴅ ʙʏ: {m.from_user.mention()}**"
            )
        except Exception as e:
            await m.reply(f"🚫 **ᴇʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("🔥 **ɴᴏᴛʜɪɴɢ ɪs sᴛʀᴇᴀᴍɪɴɢ ʜᴇʀᴇ 😒**")
