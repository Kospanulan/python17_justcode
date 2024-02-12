import telebot
from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(commands=["kick_user"])
def kick_command_handler(message: Message):
    user_to_kick = message.reply_to_message.from_user

    bot.kick_chat_member(
        chat_id=message.chat.id,
        user_id=user_to_kick.id
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Юзер {user_to_kick.username} кикнут!"
    )


bot.polling()
