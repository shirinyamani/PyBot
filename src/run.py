import telebot
import os
from loguru import logger
from src.constants import keyboards
from src.utils.io import write_json
from src.bot import bot
import emoji
from utils.filters import IsAdmin

from telebot import custom_filters

class Bot:
    def __init__(self, telebot):
        self.bot = telebot

        #register handler
        self.handler()

        #run bot
        logger.info("Bot is working...")
        self.bot.infinity_polling()

        #apply custom filter
        bot.add_custom_filter(IsAdmin())
        bot.add_custom_filter(custom_filters.TextStartsFilter())
	
    def handler(self):

        @self.bot.message_handler(func= lambda message:True)
        def echo(message):
            self.send_message(message.chat.id,message.text,
            reply_markup=keyboards.main_keyboard)

        @self.bot.message_handler(is_admin=True)
        def admin_of_gp(message):
            self.send_message(message.chat.id, '<strong> You are Admin!<strong>')

        @self.bot.message_handler(text=['hi','hello'])
        def text_filter(message):
            self.send_message(message.chat.id, f'Hi {message.from_user.first_name}')

    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        if emojize: 
            text = emoji.emojize(text, use_aliases=True)
        self.bot.send_message(chat_id, text, reply_markup=reply_markup)



if __name__ =="__main__":
	logger.info('Bot started')
	bot= Bot(telebot=bot)