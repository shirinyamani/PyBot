import telebot
import os
from loguru import logger
from src.constants import keyboards
import emoji

class Bot:
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
		self.echo_all= self.bot.message_handler(func= lambda message:True)(self.echo_all)

	def run(self):
		logger.info("Bot is working...")
		self.bot.infinity_polling()

	def echo_all(self,message):
		#write_json(message.json, 'message.json')
		print(emoji.demojize(message.text))
		self.bot.send_message(message.chat.id, message.text,
		reply_markup=keyboards.main_keyboard)

if __name__ =="__main__":
	logger.info('Bot started')
	bot= Bot()
	bot.run()