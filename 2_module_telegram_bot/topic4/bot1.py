import telebot
from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(token=API_TOKEN)

bad_words = []


def contains_greeting(msg):
    if "привет" in msg.text.lower() and 'бот' in msg.text.lower():
        return True
    return False


def contains_bye(msg):
    if "пока" in msg.text.lower() and 'бот' in msg.text.lower():
        return True
    return False


@bot.message_handler(func=contains_greeting)
def message_handler(message: Message):

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Привет {message.from_user.username}"
    )


@bot.message_handler(func=contains_bye)
def message_handler(message: Message):

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Пока {message.from_user.username}"
    )


bot.polling()
