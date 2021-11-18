import telebot

bot = telebot.TeleBot ('2076406211:AAGh2cV8ckN_VSXtDKiVOd8Xl5Xw7BWTtrM')

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}<b>!\nХочешь получать большое количество денег? То пора тыкать на кнопки ниже"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True)