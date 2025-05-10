import telebot

bot = telebot.TeleBot("7961039857:AAEXtgIVlj53ymfZez6RQ3hquRfaRsqE9M4") # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def main(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()
