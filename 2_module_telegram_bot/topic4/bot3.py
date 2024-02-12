import telebot
from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(token=API_TOKEN)
# new_chat_members
# left_chat_member


@bot.message_handler(content_types=["new_chat_members"])
def new_member_handler(message: Message):

    print(message)
    print(message.new_chat_members)
    for new_member in message.new_chat_members:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Здесь новый участник, давайте поприветствуем {new_member.username}!"
        )


@bot.message_handler(content_types=["left_chat_member"])
def new_member_handler(message: Message):

    print(message)
    print(message.left_chat_member)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Пока {message.left_chat_member.username}!"
    )


@bot.message_handler(content_types=["text"])
def message_handler4(message: Message):

    print(message)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"blah-blah-blah"
    )




bot.polling()
