from random import choice
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
import datetime

now = datetime.datetime.now()


router = Router()


@router.message(F.text)
async def apfs(message: Message):
    if now.hour == 15 and now.minute == 22:
        await message.answer("11:11")


@router.message(F.text == "брейнрот" or F.text == "Брейнрот")  # сверка текста юзера, если совпадает
async def brainrot(message: Message):  # отве
    await message.answer("тунг тунг тунг сахууур")


@router.message(F.text == "тралалело" or F.text == "Тралалело")
async def tralalelo(message: Message):
    await message.answer_photo(
        photo='https://upload.wikimedia.org/wikipedia/commons/f/f6/Tralalero_Tralala.webp',
        caption="тралала")


@router.message(Command('kto_ti'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://i.ebayimg.com/images/g/rdQAAOSwzlhnMDIC/s-l1600.jpg',
                               caption='эт я))')
