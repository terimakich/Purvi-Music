from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/THE_INCRICIBLE"),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/ZOYU_SUPPORT")
    ],
    [
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG"),
        InlineKeyboardButton("˹ ʙᴧᴄᴋ ˼", callback_data=f"settingsback_helper")
    ]
    ]
