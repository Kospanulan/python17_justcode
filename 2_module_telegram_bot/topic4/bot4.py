import telebot
from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(func=lambda msg: msg.text.lower() == "спасибо"
                                      and msg.reply_to_message is not None
                                      # and msg.reply_to_message.from_user.username == "justcode_ulan_bot")
                                      and msg.reply_to_message.from_user.username == bot.get_me().username)
def m_handler(message: Message):
    print(f"message: {message}")
    print(f"replied_message: {message.reply_to_message}\n")
    bot.send_message(
        chat_id=message.chat.id,
        text="Не за что!"
    )


@bot.message_handler(content_types=["text"])
def message_handler4(message: Message):
    print(message)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Поблагодарите меня!"
    )


bot.polling()
