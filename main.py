import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from api import tiktok, instagram, facebook, snapchat
from models import User

TOKEN = '7460589468:AAGBO8NYVTFX7Bscr_7QC9a6693IawSwr3s'
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = {
        "user_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
    }
    user = User(**user)
    if not user.select(user_id=message.from_user.id):
        user.insert()
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer('Send a link')


@dp.message(F.text.contains('instagram.com'))
async def instagram_handler(message: Message) -> None:
    await bot.send_chat_action(chat_id=message.from_user.id, action='upload_video')
    video = await instagram(message.text)
    await message.answer_video(video)


@dp.message(F.text.contains('tiktok.com'))
async def tiktok_handler(message: Message):
    await bot.send_chat_action(chat_id=message.from_user.id, action='upload_video')
    video, music = await tiktok(message.text)
    await message.answer_video(video)
    await message.answer_audio(music)


@dp.message(F.text.contains('facebook.com'))
async def facebook_handler(message: Message):
    await bot.send_chat_action(chat_id=message.from_user.id, action='upload_video')
    video = await facebook(message.text)
    await message.answer_video(video)
    # await message.answer_audio(music)


@dp.message(F.text.contains('snapchat.com'))
async def snapchat_handler(message: Message):
    await bot.send_chat_action(chat_id=message.from_user.id, action='upload_video')
    video, title = await snapchat(message.text)
    await message.answer_video(video, caption=f'{title}')


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
