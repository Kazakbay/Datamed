from telebot import TeleBot
from telebot import types

import fitz
import re
import sqlite3
import os

class Data_manager:
    def __init__(self, filename):
        self.filename = filename
        self.text_lines = []
        self.test_results = []
        self.test_types = ['Общий белок','Мочевина','Креатинин']
        self.doc = fitz.open(self.filename) #opens PDF file
        self.page = self.doc[0]
        self.data = ''

    def extract_text(self):
        text_blocks = self.page.get_text('blocks') # extracts sentences with coordinates

        # this loop extracts only sentences
        for line in text_blocks:
            self.text_lines.append(re.split('\n',line[4]))

    def get_test_result(self):
        for type in self.test_types:
            for sentence in self.text_lines:
                for i, word in enumerate(sentence):
                    if type.lower() in word.lower():
                        if re.findall(r'\d+', sentence[i + 1]) != []:
                            lst = re.findall(r'\d+', sentence[i + 1])
                            num = ''
                            if len(lst) > 1:
                                num = lst[0] + '.' + lst[1]
                            else:
                                num = lst[0]
         
                            self.test_results.append((type, float(num)))                
                  

    def get_date(self):
        data_strange = self.doc.metadata['creationDate'][2:10]
        data = ''
        data += data_strange[0:4] + '.'
        data += data_strange[4:6] + '.'
        data += data_strange[6:8] 
        self.data = data
        

    def db_connecter(self):
        self.conn = sqlite3.connect('laboratory_data.db')
        self.c = self.conn.cursor()

    def insert_data(self):
        if os.path.isfile('laboratory_data.db') == False:
            self.db_connecter()
            self.c.execute("""CREATE TABLE storage_of_results (
                      test_name text,
                      result real,
                      data text
            )""")

        self.db_connecter()
        for item in self.test_results:
            self.c.execute(f"INSERT INTO storage_of_results VALUES {(item[0], item[1], self.data)}")
        self.conn.commit()
        self.conn.close()

    def run(self):
        self.extract_text()
        self.get_test_result()
        self.get_date()
        self.insert_data()
        print('Done')
        



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

@bot.message_handler(content_types=['document'])
def save_the_file(message):
    print('someting happened')
    print(message.document.file_id)
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    print('downloaded')
    print(downloaded_file)
    with open(message.document.file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_document(message.chat.id, downloaded_file)

    print(message.document.file_name)
    
    i = Data_manager(filename=message.document.file_name)
    i.run()
    

bot.polling()
