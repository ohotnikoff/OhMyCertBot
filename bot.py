import telebot

from pdf2cert import create_cert
import config


bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, для получения сертификата введите фамилию, имя и отчество в дательном падеже. Пример: Иванову Петру Васильевичу")


@bot.message_handler(content_types=['text'])
def send_cert(message):
    chat_id = message.chat.id
    text = message.text

    if (len(text) > 10) & (len(text) < 40):
        print(chat_id, text)
        create_cert(text)  # генерируем сертификат

        cert = open(config.OUTPUT_PDF, 'rb')  # открываем
        bot.send_photo(chat_id, photo=cert)  # отправляем фото

        cert = open(config.OUTPUT_PDF, 'rb')  # открываем
        bot.send_document(chat_id, cert)  # отправляем PDF
    else:
        bot.send_message(chat_id, "Введите фамилию, имя и отчество в дательном падеже. Ограничение до 40 символов")


bot.polling(none_stop=True, interval=0)
