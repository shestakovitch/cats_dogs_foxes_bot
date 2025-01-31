import requests
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot_phrases_dict import bot_phrases
from keyboards import yes_no_kb, animals_kb

router = Router()


# start command handler
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=bot_phrases['/start'], reply_markup=yes_no_kb)


# handler is triggered by the user's consent
@router.message(F.text == bot_phrases['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=bot_phrases['yes'], reply_markup=animals_kb)


# handler is triggered by user rejection
@router.message(F.text == bot_phrases['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=bot_phrases['no'])


# handler for "cats" button
@router.message(F.text == bot_phrases['cats'])
async def process_cats_answer(message: Message):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    media = response.json()[0]["url"]
    if response.status_code == 200:
        if media.lower()[-3:] in ('gif', 'mp4', 'webm'):
            await message.answer_animation(animation=media)
        else:
            await message.answer_photo(photo=media)


# handler for "dogs" button
@router.message(F.text == bot_phrases['dogs'])
async def process_cats_answer(message: Message):
    response = requests.get('https://random.dog/woof.json')
    media = response.json()["url"]
    if response.status_code == 200:
        if media.lower()[-3:] in ('gif', 'mp4', 'webm'):
            await message.answer_animation(animation=media)
        else:
            await message.answer_photo(photo=media)


# handler for "foxes" button
@router.message(F.text == bot_phrases['foxes'])
async def process_cats_answer(message: Message):
    response = requests.get('https://randomfox.ca/floof/')
    media = response.json()["link"]
    if response.status_code == 200:
        if media.lower()[-3:] in ('gif', 'mp4', 'webm'):
            await message.answer_animation(animation=media)
        else:
            await message.answer_photo(photo=media)


# handler for messages that are not in other handlers
@router.message()
async def send_answer(message: Message):
    await message.answer(text=bot_phrases['other_answer'])
