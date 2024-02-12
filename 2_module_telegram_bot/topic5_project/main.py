import telebot
from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from messages import start_message, help_message
from quiz_data import question_list, option_list

API_TOKEN = "6971792089:AAHoSiM360WGQUkYW_bXbM25KBJITZuLEb4"

bot = telebot.TeleBot(token=API_TOKEN)


current_question = 0


@bot.message_handler(commands=["start"])
def start_command_handler(message: Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=start_message
    )


@bot.message_handler(commands=["help"])
def help_command_handler(message: Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=help_message
    )


@bot.message_handler(commands=["start_quiz"])
def start_quiz_command_handler(message: Message):

    question_data = question_list[current_question]
    q_text = f"{current_question + 1}. {question_data['question']}"
    markup = InlineKeyboardMarkup(row_width=2)
    btns = []

    for i, option in enumerate(question_data['options']):
        btn = InlineKeyboardButton(text=option, callback_data=option_list[i])
        btns.append(btn)

    markup.add(*btns)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Викторина начинается!"
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=q_text,
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data in option_list)
def callback_handler(call: CallbackQuery):
    global current_question

    old_question_data = question_list[current_question]
    if old_question_data['correct_option'] == call.data:
        bot.answer_callback_query(callback_query_id=call.id, text="Правильно!")
    else:
        bot.answer_callback_query(callback_query_id=call.id, text="Не правильно!")

    current_question += 1

    if current_question >= len(question_list):
        bot.send_message(
            chat_id=call.message.chat.id,
            text="Конец",
        )
        current_question = 0
        return

    question_data = question_list[current_question]
    q_text = f"{current_question + 1}. {question_data['question']}"
    markup = InlineKeyboardMarkup(row_width=2)
    btns = []

    for i, option in enumerate(question_data['options']):
        btn = InlineKeyboardButton(text=option, callback_data=option_list[i])
        btns.append(btn)

    markup.add(*btns)

    bot.send_message(
        chat_id=call.message.chat.id,
        text=q_text,
        reply_markup=markup
    )


bot.polling()
