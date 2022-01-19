import telebot
import os

bot = telebot.TeleBot(os.environ['BOT_TOKEN'], parse_mode='HTML')