from telebot import TeleBot
from telebot import types

bot = TeleBot("6358744092:AAF8Snr3NiV27Ke4ytSn6KTILUAdcBWZbxw")
chat_id = 12345

button_foo = types.InlineKeyboardButton('Foo', callback_data='foo')
button_bar = types.InlineKeyboardButton('Bar', callback_data='bar')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(button_foo)
keyboard.add(button_bar)
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, text='Press one of the buttons', reply_markup=keyboard)


@bot.callback_query_handler(func = lambda callback: callback.data)
def check_callback(callback):
    if (callback.data == 'foo'):
        bot.send_message(callback.message.chat.id, "Send the file: ")

@bot.message_handler(content_types=['document', 'photo'])
def save_the_file(message):
    print('someting happened')
    print(message.photo[0].file_id)
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    print('downloaded')
    bot.send_photo(message.chat.id, photo=message.photo[0].file_id)

bot.polling()
