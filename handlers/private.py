from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIBamBudETEPJsY5yGqy8k2Bec8i2ykAAKJAQACBalSM0U9vAY2kPV5HgQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [MrC《》VENOM](https://t.me/MrC_VENOM).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎 Creater 😎", url="https://t.me/MrC_VENOM")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/tvseriezzz"
                    ),
                    InlineKeyboardButton(
                        "❣ Support ❣", url="https://t.me/tvseriezzz"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/ain1bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎈 Group 🎈", url="https://t.me/tvseriezzz")
                ]
            ]
        )
   )


