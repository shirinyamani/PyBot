import telebot
from src.bot import bot


class TextStartsFilter(telebot.custom_filters.AdvancedCustomFilter):

    key ='text_startswith'
    def check(self, message, text):
        return message.text.startswith(text)

class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']

