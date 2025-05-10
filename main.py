import telebot

bot = telebot.TeleBot("7961039857:AAEhO7O-xUQz8kucrl9b5kgRZjPq475BsPI") # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def main(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()
