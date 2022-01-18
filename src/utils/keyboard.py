from types import SimpleNamespace
from telebot import types
import emoji



def create_keyboard(*keys, row_width=3,  resize_keyboard=True):
    markup = types.ReplyKeyboardMarkup(row_width=row_width,
     resize_keyboard=resize_keyboard)
    keys=map(emoji.emojize, keys)
    bottoms= map(types.KeyboardButton, keys)
    markup.add(*bottoms)
    return markup
