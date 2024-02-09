import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

API_TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(token=API_TOKEN)

REPLY_KEYBOARD_OPTIONS = ["Алматы", "Астана", "Актобе", "Шымкент"]
# REPLY_KEYBOARD_OPTIONS = ["Алматы", "Астана"]


@bot.message_handler(commands=["start"])
def handler_with_keyboard(
        message: Message
):

    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

    # variant 1
    btn1 = KeyboardButton("Алматы")
    btn2 = KeyboardButton("Астана")
    btn3 = KeyboardButton("Актобе")
    btn4 = KeyboardButton("Шымкент")

    markup.add(btn1, btn2, btn3, btn4)

    # variant 2 testing ...
    # markup.add(btn1, btn2)
    # markup.add(btn3, btn4)

    # variant 3
    # for option in REPLY_KEYBOARD_OPTIONS:
    #     btn = KeyboardButton(option)
    #     markup.add(btn)

    bot.send_message(
        chat_id=message.chat.id,
        text="test",
        reply_markup=markup
    )


@bot.message_handler(func=lambda msg: msg.text in REPLY_KEYBOARD_OPTIONS)
def reply_keyboard_handler(message: Message):
    if message.text == "Алматы":
        reply_text = "Hello"
    else:
        reply_text = "тест"

    remove_kb = ReplyKeyboardRemove()

    bot.send_message(
        chat_id=message.chat.id,
        text=reply_text,
        reply_markup=remove_kb
    )


@bot.message_handler(content_types=["text"])
def reply_keyboard_handler(message: Message):

    bot.send_message(
        chat_id=message.chat.id,
        text="Прошу отправить корректный ответ из клавиатуры"
    )


bot.polling()
