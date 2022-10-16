import telebot
from data_for_bot import token

bot = telebot.TeleBot(token)


def main_errors(message, value):
    if value is False:
        bot.send_message(message.from_user.id, f'!error!, try again!')