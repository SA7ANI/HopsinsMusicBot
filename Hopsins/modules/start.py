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


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Hi {message.from_user.first_name}, I'm HOPSINS ┏┛\n
I am Bot Music Group, the which can play songs in Voice Chat Group in an easy way
I Have Many Practical Features Such as:
┏━━━━━━━━━━━━━━
┣ • Playing Music.
┣ • Downloading Songs.
┣ • Search Song you want to Play or Download.
┗━━━━━━━━━━━━━━
❃ Managed by : [SATAN](https://t.me/SA7ANI)
━━━━━━━━━━━━━━━
Wanna Add me to your Group? Just click the button below!
</b>""",

# Edit What You Need to Change
# But don't delete it. Thanks to. Yes: D

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 How to Use BOT 📜", url="https://telegra.ph/HOPSINS-Music-Bot-05-30")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/TheKonoha11"
                    ),
                    InlineKeyboardButton(
                        "Coming Soon", url="https://t.me/HopsinsMusicBot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

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
                        "Group Support", url="https://t.me/TheKonoha11"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/SA7ANI"
                    )
                ]
            ]
        )
   )