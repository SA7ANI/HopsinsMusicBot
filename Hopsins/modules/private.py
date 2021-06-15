# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from Hopsins.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Hopsins.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Hi {message.from_user.first_name}.\n
{PROJECT_NAME} is a project designed for **play**,
as simple as possible, **music** in your **groups**
through the **voice chat** and download songs from **Youtube, Dezzer and Saavn**
━━━━━━━━━━━━━━━━━━━━━━
Hit /help to find more about how to use me to my full potential.
━━━━━━━━━━━━━━━━━━━━━━
Wanna Add me to your Group? Just click the button below!
""",

# Edit What You Need to Change
# But don't delete it, thanks to ya :D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url=f"https://{SOURCE_CODE}"), 
                    InlineKeyboardButton(
                        "⛑ Group Support", url=f"https://t.me/{SUPPORT_GROUP}")
                ],
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if (pos==1):
        return [
            [InlineKeyboardButton(text = 'Next »', callback_data = "help+2")]
        ]
    elif pos==len(tr.HELP_MSG)-1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        return [
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group ➕",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text='💬 Channel Updates',
                    url=f"https://t.me/{UPDATES_CHANNEL}",
                ),
                InlineKeyboardButton(
                    text='⛑ Group Support', url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text='🛠 Source Code 🛠', url=f"https://{SOURCE_CODE}"
                )
            ],
            [InlineKeyboardButton(text='«', callback_data=f"help+{pos-1}")],
        ]

    else:
        return [
            [
                InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '»', callback_data = f"help+{pos+1}")
            ],
        ]


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Do you want to find YouTube Links?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Not ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Click the button below to see how to use the bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 How to Use BOT 📜", url="https://telegra.ph/HOPSINS-Music-Bot-05-30"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **restarted successfully!**\n\n• **Admin list** has been **updated**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "Owner", url=f"https://t.me/SA7ANI"
                    )
                ]
            ]
        )
   )