#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
import configparser
import requests
import random


def name_gen(word_list, name_length=3):
    """
    Function returns random silly name.
    :param word_list: list[str]
    List of the words to brew a special soup.
    :param name_length: int
    Number of parts in the name. Default 3.
    :return: str
    Random stupid name.
    """
    name = ''
    temp_words = word_list.copy()
    temp_words = list(set(temp_words))
    for i in range(name_length):
        position = random.randint(0, len(temp_words) - 1)
        name += temp_words[position].title()
        temp_words.remove(temp_words[position])
    return name


def send_message(link, chat_id, text='Default text of the message.'):
    """
    Send a message to user.
    :param link: str
    Telegram API URL with token inserted.
    :param chat_id: str or int
    Telegram chat id.
    :param text: str, optional
    Text to be sent.
    :return:
    """
    param = {'chat_id': chat_id, 'text': text}
    requests.post(link + 'sendMessage', json=param)


# configs parsing
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
token = config['bot']['token']
address = config['server']['address']
port = config['server']['port']
public_key = config['ssl']['public_key']
private_key = config['ssl']['private_key']
report_chat_id = config['errors']['report_chat_id']

# inserting tg bot token to API link
url = f'https://api.telegram.org/bot{token}/'

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    # standard messages
    welcome_message = 'Привет!'
    goodbye_message = 'Пока.'
    help_message = 'Начни вводить "/", появится список команд.'
    why_message = ('Создаёшь компанию и не знаешь, как назвать? 🤨\n\n'
                   'Наверняка часто замечаешь названия в стиле РемСнабПром или КапЭнергоКомплект.\n\n'
                   'Лучшие дельцы дали название своим конторам с этим ботом. Отвечаю. 😎\n'
                   'Иначе откуда такой безумный суп из слов, которые невозможно запомнить?\n\n'
                   'Пользуйся. Не благодари.')
    clarify_message = ('Тебе нужно имя для комании?\n'
                       'Жми /new_name.')
    report_message = '**Unexpected event**\nTake a look:\n\n'

    # read webhook
    if request.method == 'POST':
        r = request.get_json()
        # check events
        try:
            # expected event
            chat_id = r['message']['chat']['id']
            message = r['message']['text']
        except:
            # unexpected event
            chat_id = int(report_chat_id)
            for item in r:
                send_message(
                    url,
                    chat_id,
                    report_message + item
                )
            return 'bug reported', 200
        # check messages
        if message == '/start':
            send_message(url, chat_id, welcome_message)
            return 'success', 200
        elif message == '/new_name':
            f = open("list.txt", "r", encoding='utf-8')
            data = f.read()
            f.close()
            words = data.split()
            option_1 = name_gen(words)
            option_2 = name_gen(words)
            option_3 = name_gen(words)
            options = (f'Вот несколько вариантов:\n'
                       f'1. {option_1}\n'
                       f'2. {option_2}\n'
                       f'3. {option_3}')
            send_message(url, chat_id, options)
            return 'success - names are generated', 200
        elif message == '/help':
            send_message(url, chat_id, help_message)
            return 'success - help message is sent', 200
        elif message == '/why':
            send_message(url, chat_id, why_message)
            return 'success - help message is sent', 200
        elif message == '/stop':
            send_message(url, chat_id, goodbye_message)
            return 'success - bot stoped', 200
        else:
            send_message(url, chat_id, clarify_message)
            return 'success - other respond is send', 200


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=int(port), ssl_context=(public_key, private_key))
