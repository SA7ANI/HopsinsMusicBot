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
        f"""Hi {message.from_user.first_name}.\n
[HOPSINS](https://t.me/HopsinsMusicBot) is a project designed for **play**,
as simple as possible, **music** in your **groups**
through the **voice chat** and download songs from **Youtube, Dezzer and Saavn**
━━━━━━━━━━━━━━━━━━━━━━
Hit /help to find more about how to use me to my full potential.
━━━━━━━━━━━━━━━━━━━━━━
Wanna Add me to your Group? Just click the button below!
""",

# Edit What You Need to Change
# But don't delete it. Thanks to. Yes: D

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        text="Add Me To Your Group!",
                        url=f"http://t.me/HopsinsMusicBot?startgroup=new")
                  ],[
                    InlineKeyboardButton(
                        text="Tutorial",
                        url="https://telegra.ph/HOPSINS-Music-Bot-05-30"
                    ),
                    InlineKeyboardButton(
                        text="Group Support",
                        url="https://t.me/TheKonoha11"
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
        f"""**Click the button below to see how to use the bot**""",
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
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""**Hello {message.from_user.first_name}! My name is HOPSINS!**\n\n
**Commands for Groups, Group Members Can Also Use:**

• `/playlist` - To Display the current Song playlist
• `/current` - To Show the currently playing Song
• `/song <song name>` : To download songs on YouTube
• `/video <song name>` : To Download Videos on YouTube with details
• `/vsong <song name>` : To Download Videos on YouTube with details
• `/deezer <song name>` : To download songs from deezer
• `/saavn <song name>` : To download songs from the saavn website
• `/search <song name>` : For Searching Videos on YouTube with details

**Command For Group Chat Admins Only:**
• `/play <song name>` : To play the song you requested via YouTube
• `/dplay <song name>`  : To play the song you requested via deezer
• `/splay <song name>`  : To play the song you requested via jio saavn
• `/pause` : To Pause Song playback
• `/resume` : To continue playing the pause Song
• `/skip` : To Skip the song playback to the next Song
• `/end` : To Stop playing the Song
• `/userbotjoin` : To Invite assistant to your chat
• `/admincache` : To Refresh the admin list

**NOTE: Videos or music that is longer than 1 hour cannot be played. Please remember don't add a lot of music to the queue at once to avoid unwanted errors. That's all the message from me! Happy Music.**
""",
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