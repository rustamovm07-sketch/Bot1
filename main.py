import telebot

# API Tokeningizni qo'shtirnoq ichiga yozing
TOKEN = '8659157555:AAG1v3nGfFlc4ZRIq2Pj5N0GqvFYEx6oG_M'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Salom! Men iPhone-dan yaratilgan botman. 24/7 ishlayman!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

print("Bot ishlashga tayyor...")
bot.infinity_polling()
