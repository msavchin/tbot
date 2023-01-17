from aiogram import types
from dispatcher import dp
import asyncio
# Personal actions goes here (bot direct messages)
# Here is some example !ping command ...

WORDS = ['блять',
         'хуйня',
         'сука',
         'еблан',
         'бля',
         'сук',
         'заебись'
         ]


@dp.message_handler(is_owner=True, commands="ping", commands_prefix="!/")
async def cmd_ping_bot(message: types.Message):
    await message.reply("<b>👊 Я тут!</b>\n\n")

# Remove message if find word from array


@dp.message_handler()
async def words(message: types.Message):
    text = message.text.lower()
    for word in WORDS:
        if word in text:
            await message.reply(f'💀 {message.from_user.full_name}, матюки заборонено Вадімовською конвенцією, повідомлення видалено.')
            await message.delete()
