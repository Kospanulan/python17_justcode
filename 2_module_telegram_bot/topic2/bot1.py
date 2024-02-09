import telebot
from telebot.types import Message

API_TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(content_types=["photo"])
def message_handler(message: Message):
    print(message)

    photos = message.photo

    for i, photo in enumerate(photos):
        file_id = photo.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        byte_file = bot.download_file(file_path)

        print(f"Downloading... {i}: {photo.file_id}")
        filename = f"{i}_{photo.file_id}.png"
        with open(f"downloads/{filename}", 'wb') as f:
            f.write(byte_file)

    bot.send_message(
        chat_id=message.chat.id,
        text="Это фото! И мы его скачали!"
    )
    # bot.send_photo()


@bot.message_handler(content_types=["document"])
def message_handler(message: Message):
    print(message)
    doc = message.document
    file_id = doc.file_id

    # https://api.telegram.org/file/bot<token>/<file_path>
    file_info = bot.get_file(file_id)  # File
    file_path = file_info.file_path

    byte_file = bot.download_file(file_path)

    # filename = "first_image.png"
    # filename = "received_file.txt"
    filename = doc.file_name

    # with open(f"downloads/{filename}", 'wb') as f:
    #     f.write(byte_file)

    bot.send_document(
        chat_id=message.chat.id,
        # document=file_id,
        document=open(f"data/test.jpeg", 'rb'),
        caption="Это документ! И мы его уже скачали и отправили вам другой:)"
    )


@bot.message_handler(content_types=["text"])
def message_handler(message: Message):
    print(message)

    bot.send_message(
        chat_id=message.chat.id,
        text=message.text
    )


bot.polling()
