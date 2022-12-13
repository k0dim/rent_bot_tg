from telebot import TeleBot
from Module.avito import avito_main
from loguru import logger
import os

bot = TeleBot('5976202984:AAHMn4Yhye3w-Mzvoombab0GuQw-Lpy-IdQ')

@bot.message_handler(commands=['help'])
def help(message):
    help_message = """
Ну смотри, когда нажимаешь /start, то я начинаю искать новые объявления на Авито (Циан в работе).
Ищу по фильтру: 
Город: Самара
Комнаты: Студия, 1, 2
Цена: до 20.000 р
Поиск идет по ссылке: https://www.avito.ru/samara/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?f=ASgBAQECAkSSA8gQ8AeQUgFAzAg0kFmOWYxZAUXGmgwVeyJmcm9tIjowLCJ0byI6MjAwMDB9&i=1&s=104&user=1
---
Ну все, давай, не болей 
    """
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_video(message.chat.id, 'https://media.tenor.com/e55q1Aor1yoAAAAd/lets-work-work.gif')
    bot.send_message(message.chat.id, 'Работаем')
    bot.send_message(message.chat.id, 'Как появится новое объявление - дам знать')
    text = avito_main()

    new_dict = text

    while True:
        try:
            logger.info(f"new_dict = {new_dict}")
            if new_dict['href'] == text['href']:
                logger.info(f"Check dict: new_dict = text")
                logger.info(f"Success: Сообщение НЕ отправленно")
                text = avito_main()
                continue

            else:
                new_dict = text
                logger.info(f"Check dict: new_dict != text")
                markdown = f"""
[{text['name']}]({text['href']})
*{text['price']}*
{text['deposit']}
{text['geo']}
"""
            # bot.send_message(message.chat.id, markdown, parse_mode="Markdown", disable_notification=True)
            bot.send_photo(message.chat.id, text['photo'], "Markdown", disable_notification=True)
            logger.info(f"Success: Сообщение отправленно")
            text = avito_main()
            continue

        except:
            continue

if __name__ == "__main__":
    ROAD = os.getcwd() 
    full_path_log = os.path.join(ROAD, 'log', 'file.log')
    logger.add(full_path_log, format="{time} {level} {message}", level="INFO", retention="10 days")

    bot.infinity_polling()
