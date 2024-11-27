import telebot

Tg = telebot.TeleBot('7787938172:AAFd-4QLQcjylzdF2Z6WDcQGGqhTeTL2vIU')


@Tg.message_handler(commands=['start'])
def T(message):
    Tg.send_message(message.chat.id,
                    'Привет я бот для обучения, если ты хочешь научиться чему-то новому,то ты по адресу, скорее пиши "опции" ,чтобы узнать ,что я могу')


@Tg.message_handler(commands=['опции'])
def T(message):
    Tg.send_message(message.chat.id,
                    'если хочешь сдать егэ по русскому или математику я могу подсказать где тебе помогут с этим, "русский","математика"')


@Tg.message_handler(commands=['русский'])
def T(message):
    Tg.send_message(message.chat.id, 'https://umschool.net/ege/11-class/russian/#bundle')


@Tg.message_handler(commands=['математика'])
def T(message):
    Tg.send_message(message.chat.id, 'https://umschool.net/ege/11-class/math/')


@Tg.message_handler(commands=['пока'])
def T(message):
    Tg.send_message(message.chat.id,
                    'если был полезен, ао рекомендуй друзьям, кто тоже хочет сдать егэ на 100, с умскул легче!')


Tg.infinity_polling()
