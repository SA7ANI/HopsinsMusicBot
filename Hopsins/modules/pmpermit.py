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


from pyrogram import filters
from pyrogram.types import Message

from Hopsins.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Hello, I am **Hopsins Assistant Service.**\n\n ❗️ **Rules:**\n   - Don't Spam Order Here\n   - Do not spam songs to make it ga error\n   - Tutorial on how to use bots See [Click Here](https://telegra.ph/HOPSINS-Music-Bot-05-30) \n\n 👉 **SEND INVITE LINKS OR GROUP USERNAME, IF ASSISTANT CANNOT JOIN YOUR GROUP.**\n\n ⛑ **Group Support :** @SA7ANI\n\n",
    )
    return
