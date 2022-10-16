token = '5345811825:AAHnojPAYJRo-BXeNEeeoovQVMOfu96uGM8'

with open('bot_text', encoding='utf-8') as file:
    bot_text = [text.replace('\n', '') for text in file.readlines()]

with open('bot_functional', encoding='utf-8') as file:
    bot_functional = [text.replace('\n', '') for text in file.readlines()]
