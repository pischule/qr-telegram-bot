import urllib
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

API_URL = r"https://chart.googleapis.com/chart?cht=qr&choe=UTF-8&chs=500x500&chl="


def get_qr_url(text):
    message_encoded = urllib.parse.quote(text)
    url = API_URL + message_encoded
    return url


def qr(update, context):
    photo_url = get_qr_url(update.message.text)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=photo_url)


def main():
    TOKEN = open('token.txt').read().strip()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, qr))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
