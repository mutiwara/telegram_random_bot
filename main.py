import functionals
from data_for_bot import token, bot_text, bot_functional
from errors import main_errors
import telebot
import random


bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, f'{bot_text[0]}, '
                                               f'{message.from_user.first_name}!')
        for text in range(1, 3):
            bot.send_message(message.from_user.id, f'{bot_text[text]}')
    elif message.text == '/functional':
        for functional in range(len(bot_functional)):
            bot.send_message(message.from_user.id, f'{bot_functional[functional]}')
    elif message.text == '/random_number':
        msg = bot.send_message(message.from_user.id, f'Input your first number')
        bot.register_next_step_handler(msg, first_random_number)
    elif message.text == '/random_dice_number':
        number = random.randint(1, 6)
        bot.send_photo(message.from_user.id, functionals.dice_photo(number))
    elif message.text == '/random_password':
        msg = bot.send_message(message.from_user.id, f'Input length of password(less then 50)')
        bot.register_next_step_handler(msg, password)


def first_random_number(message):
    global first_number
    first_number = message.text
    msg = bot.send_message(message.from_user.id, f'Input your second number')
    bot.register_next_step_handler(msg, second_random_number)


def second_random_number(message):
    second_number = message.text
    bot.send_message(message.from_user.id, f'Number can be in the range(from {first_number} to {second_number})\n'
                                           f'Your random number:'
                                           f'{random.randint(int(first_number), int(second_number))}')


def password(message):
    main_errors(message, functionals.password_creater(int(message.text)))
    if functionals.password_creater(int(message.text)) is not False:
        bot.send_message(message.from_user.id, f'{functionals.password_creater(int(message.text))}')


bot.polling(none_stop=True, interval=0)
