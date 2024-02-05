import telebot

TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def message_handler_func(message):
    print(f"message: {message}")

    if "hi" in message.text:
        text = "Hello"
    elif message.text == "Как ты?":
        text = "Все отлично, ты как?"
    else:
        text = "Не понял:("
        # text = ""

    bot.send_message(message.chat.id, text)


bot.polling()
# bot.infinity_polling()
