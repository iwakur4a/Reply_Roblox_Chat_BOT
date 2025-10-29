import datetime
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command('kto_ti'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://i.ebayimg.com/images/g/rdQAAOSwzlhnMDIC/s-l1600.jpg',
        caption='эт я))')


@router.message(F.text.lower() == "брейнрот")
async def brainrot(message: Message):
    await message.answer("тунг тунг тунг сахууур")


@router.message(F.text.lower() == "тралалело")
async def tralalelo(message: Message):
    await message.answer_photo(
        photo='https://upload.wikimedia.org/wikipedia/commons/f/f6/Tralalero_Tralala.webp',
        caption="тралала")


@router.message(F.text)  # Этот хендлер ПОСЛЕДНИМ, чтобы не блокировал остальные
async def check_time(message: Message):
    now = datetime.datetime.now()
    if now.hour == 22 and now.minute == 34:
        await message.bot.send_message(chat_id=-1003220158532, text="11:11")
