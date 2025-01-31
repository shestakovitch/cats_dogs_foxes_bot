from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot_phrases_dict import bot_phrases

# ---------- Creating a keyboard via ReplyKeyboardBuilder ----------

# create answer with accept and reject responses
button_yes = KeyboardButton(text=bot_phrases['yes_button'])
button_no = KeyboardButton(text=bot_phrases['no_button'])

# initialize a builder for a keyboard with “Let's go!” and “Don't want to!” buttons
yes_no_kb_builder = ReplyKeyboardBuilder()

# add buttons to the builder with argument width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# create a keyboard with “Let's go!” and “Don't want to!” buttons.
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# create buttons: cats, dogs, foxes
button_1 = KeyboardButton(text=bot_phrases['cats'])
button_2 = KeyboardButton(text=bot_phrases['dogs'])
button_3 = KeyboardButton(text=bot_phrases['foxes'])

# create a keyboard with “Cats 🐱” buttons “Dogs 🐶” and “Foxes 🦊” as a list of lists
animals_kb_builder = ReplyKeyboardBuilder()
animals_kb_builder.row(button_1, button_2, button_3, width=1)
animals_kb: ReplyKeyboardMarkup = animals_kb_builder.as_markup(
    resize_keyboard=True
)
