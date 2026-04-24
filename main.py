import telebot
import requests # Boshqa saytlarga buyurtma yuborish uchun

BOT_TOKEN = '8659157555:AAG1v3nGfFlc4ZRIq2Pj5N0GqvFYEx6oG_M'
PANEL_API_KEY = '1a321763e449228140a11028135671df' # Mana shu yerga qo'yasiz

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['check'])
def check_balance(message):
    # Bu kod panelga borib balansingizni tekshirib keladi
    url = f"https://turfaseen.net/api/v2?key={PANEL_API_KEY}&action=balance"
    response = requests.get(url).json()
    bot.reply_to(message, f"Sizning panelingizdagi balans: {response['balance']} so'm")

bot.infinity_polling()



