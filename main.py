from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import MessageHandler, filters
from graphic_builder import Graphic_builder
from data_manager import Data_manager
import os





eng_texts = [
    ['/help🙋‍♂️', '/get_graph📊', '/extra⚙️', '/language🇰🇿/🇺🇲'],
    ['/creatinine', '/urea_nitrogen', '/total_protein', '/red_blood_cell', '/hemoglobin', '/thrombocytes','/total_cholesterol','/blood_glucose', '/back🔙'],
    ['/ChatGPT🤖', '/site🌐', '/delete_db🗑️', '/back🔙'],
    ['/YES✅', '/back❌'],
    ["Hi, I'm Qolqanat Bot 🤗, I am ready to serve you 24/7 ⏰! Just don’t forget to send command  /start❕ Send me your  medical results in PDF format..."],
    ['Good 🖖 you pressed the get_graph📊 button. Please choose what you want to receive😁:'],
    ['Main menu'],
    ['file: ', ' downloaded'],
    ['Oh i can’t see any files in my data😢,please send me PDF files!💁‍♂️'],
    ["""$ /get_graph test result graphs.
    /extra Here you can see three main buttons.
    /ChatGPT sends you a link to the ChatGPT
    /site sends you a link to our official site.
    /delete_db deletes all your data in the database
    Send PDF files to get graphs
        """],
    ['Extra functions: '],
    ['Are you sure?: '],
    ['Data deleted!'],
    ['ChatGPT-пен сөйлесу үшін [мына жерді](https://platform.openai.com/playground) басыңыз!'],
    ["Click [here](https://qolkanat.tilda.ws/kz) to visit official site!"],
    ['Please wait, your request is in process...'],
    ['eng']
]

kaz_texts = [
['/k Көмек⛑️', '/g график_алу📊', '/q қосымша⚙️', '/t тіл🇰🇿/🇺🇲'],
['/kr креатинин', '/mo мочевина', '/za жалпы_ақуыз', '/rbc қызыл_қан_клеткасы', '/hm гемоглобин','/tr тромбоцит', '/zhh жалпы_холестерин','/kgl қандағы_глюкоза', '/n кері_көшу🔙'],
['/ChatGPT👾', '/s сайт🌐', '/d өшіру_бағдарламасы🗑️', '/n кері_көшу🔙'],
['/y Иә✅', '/n кері_көшу❌'],
['''Сәлем, мен Qolqanat, мен сізге көмектесе аламын! Маған медициналық сынақ нәтижелері бар PDF файлдарын жіберіңіз.'''],
['''Сіз 🖖графикті📊 алу батырмасын бастыңыз. Нені алғыңыз келетінін таңдаңыз😁 :'''],
['Басты меню'],
['файл:', 'жүктелген'],
['Деректер жоқ! Тек сіз менімен PDF файлдарды жіберіңіз!'],
["""$ /get_graph сынақ нәтижелерінің графиктері.
    /extra Мұнда сіз үш негізгі түймені көре аласыз.
    /ChatGPT сізге ChatGPT сілтемесін жібереді
    /сайт сізге біздің ресми сайтымызға сілтеме жібереді.
    /delete_db дерекқордағы барлық деректеріңізді жояды
    Графиктерді алу үшін PDF файлдарын жіберіңіз"""],
['Қосымша функциялар: '],
['Сіз сенімдісіз бе?: '],
['Деректер жойылды!'],
['Сілтеме ашу үшін [осында](https://platform.openai.com/playground) басыңыз!'],
["Ресми сайтқа кіру үшін [мына жерді](https://qolkanat.tilda.ws/kz) басыңыз!"],
['Күте тұрыңыз, сұрауыңыз орындалуда...'],
['kz']
]



language = eng_texts

main_keyboard = [[KeyboardButton(text=language[0][0]), KeyboardButton(text=language[0][1])],
                    [KeyboardButton(text=language[0][2]), KeyboardButton(text=language[0][3])]]
main_markup = ReplyKeyboardMarkup(keyboard=main_keyboard)

graph_keyboard = [[KeyboardButton(text=language[1][0]), KeyboardButton(text=language[1][1])],
                        [KeyboardButton(text=language[1][2]),KeyboardButton(text=language[1][3])],
                        [KeyboardButton(text=language[1][4]), KeyboardButton(text=language[1][5])],
                        [KeyboardButton(text=language[1][6]), KeyboardButton(text=language[1][7])],
                        [KeyboardButton(text=language[1][8])]]
graph_markup = ReplyKeyboardMarkup(keyboard=graph_keyboard, resize_keyboard=True)


extra_keyboard = [[KeyboardButton(text=language[2][0]), KeyboardButton(text=language[2][1])],
                        [KeyboardButton(text=language[2][2]), KeyboardButton(text=language[2][3])]]
extra_markup = ReplyKeyboardMarkup(keyboard=extra_keyboard)

delete_keyboard = [[KeyboardButton(text=language[3][0]), KeyboardButton(text=language[3][1])]]
delete_markup = ReplyKeyboardMarkup(keyboard=delete_keyboard)

language_keyboard = [[KeyboardButton(text='🇺🇸'), KeyboardButton(text='🇰🇿')]]
language_markup = ReplyKeyboardMarkup(keyboard=language_keyboard)
# try except

while True:
    
    def markup_maker(type='main', lan=eng_texts):
        language = lan
        if type == 'main':
            main_keyboard = [[KeyboardButton(text=language[0][0]), KeyboardButton(text=language[0][1])],
                    [KeyboardButton(text=language[0][2]), KeyboardButton(text=language[0][3])]]
            main_markup = ReplyKeyboardMarkup(keyboard=main_keyboard)
            return main_markup
        
        elif type == 'graph':
            graph_keyboard = [[KeyboardButton(text=language[1][0]), KeyboardButton(text=language[1][1])],
                            [KeyboardButton(text=language[1][2]),KeyboardButton(text=language[1][3])],
                            [KeyboardButton(text=language[1][4]), KeyboardButton(text=language[1][5])],
                            [KeyboardButton(text=language[1][6]), KeyboardButton(text=language[1][7])],
                            [KeyboardButton(text=language[1][8])]]
            graph_markup = ReplyKeyboardMarkup(keyboard=graph_keyboard)
            return graph_markup
        
        elif type == 'extra':
            extra_keyboard = [[KeyboardButton(text=language[2][0]), KeyboardButton(text=language[2][1])],
                            [KeyboardButton(text=language[2][2]), KeyboardButton(text=language[2][3])]]
            extra_markup = ReplyKeyboardMarkup(keyboard=extra_keyboard)
            return extra_markup
        
        elif type == 'del':
            delete_keyboard = [[KeyboardButton(text=language[3][0]), KeyboardButton(text=language[3][1])]]
            delete_markup = ReplyKeyboardMarkup(keyboard=delete_keyboard)
            return delete_markup

        elif type == 'language':
            language_keyboard = [[KeyboardButton(text='🇺🇸'), KeyboardButton(text='🇰🇿')]]
            language_markup = ReplyKeyboardMarkup(keyboard=language_keyboard)
            return language_markup

 
    
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print(language)
        #main_markup = markup_maker('main', lan=language)
        await context.bot.send_message(chat_id=context._chat_id, text=language[4][0], 
                                       reply_markup=markup_maker('language', lan=language))


    async def get_graph(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #graph_markup =  markup_maker('graph', language)
        await context.bot.send_message(chat_id=context._chat_id, text=language[5][0], 
                                       reply_markup=markup_maker('graph', lan=language))


    async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker(language)
        await context.bot.send_message(chat_id=context._chat_id, text=language[6][0], 
                                       reply_markup=markup_maker('main', language))


    async def get_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        print('im working right now get_doc')
        try:
            if type(update.message.document.file_id) == str:
                file_id = update.message.document.file_id
                new_file = await context.bot.get_file(file_id=file_id)
                download_path = os.path.join('trash', update.message.document.file_name)
                await new_file.download_to_drive(download_path)
                Data_manager(download_path, username=update.effective_user.username).run()
                print(context._user_id)
                file_for_delete = os.path.join('trash', update.message.document.file_name)
                os.remove(file_for_delete)
                await context.bot.send_message(chat_id=context._chat_id, 
                                               text=f"{language[7][0]}{update.message.document.file_name} {language[7][1]}")
        except:
            pass

    async def creatinine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Креатинин_{username}.png'):
            os.remove(f'Креатинин_{username}.png')
        chat_gpt_opinion = Graphic_builder('Креатинин', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Креатинин_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Креатинин_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))


    async def total_protein(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Общий белок_{username}.png'):
            os.remove(f'Общий белок_{username}.png')
        chat_gpt_opinion = Graphic_builder('Общий белок', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Общий белок_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Общий белок_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))

    async def urea_nitrogen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Мочевина_{username}.png'):
            os.remove(f'Мочевина_{username}.png')
        chat_gpt_opinion = Graphic_builder('Мочевина', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Мочевина_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Мочевина_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))
        
    
    async def red_blood_cell(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Эритроциты_{username}.png'):
            os.remove(f'Эритроциты_{username}.png')
        chat_gpt_opinion = Graphic_builder('эритроциты', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Эритроциты_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Эритроциты_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))


    async def hemoglobin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Гемоглобин_{username}.png'):
            os.remove(f'Гемоглобин_{username}.png')
        chat_gpt_opinion = Graphic_builder('Гемоглобин', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Гемоглобин_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Гемоглобин_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))


    async def thrombocytes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Тромбоциты_{username}.png'):
            os.remove(f'Тромбоциты_{username}.png')
        chat_gpt_opinion = Graphic_builder('Тромбоциты', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Тромбоциты_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Тромбоциты_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))
            

    async def total_cholesterol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Холестерин_{username}.png'):
            os.remove(f'Холестерин_{username}.png')
        chat_gpt_opinion = Graphic_builder('Холестерин', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Холестерин_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Холестерин_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))
            

    async def blood_glucose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        username = update._effective_user.username
        if os.path.isfile(f'Глюкоза_{username}.png'):
            os.remove(f'Глюкоза_{username}.png')
        chat_gpt_opinion = Graphic_builder('Глюкоза', username=username, lan=language[16][0]).run()
        await context.bot.send_message(chat_id=context._chat_id, text=language[15][0])
        if os.path.isfile(f'Глюкоза_{username}.png'):
            await context.bot.send_document(chat_id=context._chat_id, document=f'Глюкоза_{username}.png')
            await context.bot.send_message(chat_id=context._chat_id, text=chat_gpt_opinion)
        else:
            await context.bot.send_message(chat_id=context._chat_id, 
                                           text=language[8][0], reply_markup=markup_maker('main', language))
            

    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        text = language[9][0]
        await context.bot.send_message(chat_id=context._chat_id, 
                                       text=text, reply_markup=markup_maker('main', language))


    async def extra(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker(language)
        text = language[10][0]
        await context.bot.send_message(chat_id=context._chat_id, 
                                       text=text, reply_markup=markup_maker('extra', language))


    async def delete_db(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        await context.bot.send_message(chat_id=context._chat_id, 
                                       text=language[11][0], reply_markup=markup_maker('del', language))


    async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        Data_manager(filename=None, username=update.effective_user.username).delete_table()
        await context.bot.send_message(chat_id=context._chat_id, 
                                       text=language[12][0], reply_markup=markup_maker('main', language))


    async def ChatGPT(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker()
        message_text = language[13][0]
        await context.bot.send_message(chat_id=context._chat_id, 
                                       text=message_text, reply_markup=markup_maker('main', language))


    async def site(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker(language)
        message_text = language[14][0]
        await context.bot.send_message(chat_id=context._chat_id, 
                                       text=message_text, reply_markup=markup_maker('main', language))


    async def language_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #markup_maker(language)
        await context.bot.send_message(chat_id=context._chat_id, 
                                       text='Language/тіл', reply_markup=markup_maker('language', language))

    async def mess_process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        global language  # Use the global variable language
        try:
            if type(update.message.document.file_id) == str:
                file_id = update.message.document.file_id
                new_file = await context.bot.get_file(file_id=file_id)
                download_path = os.path.join('', update.message.document.file_name)
                await new_file.download_to_drive(download_path)
                Data_manager(download_path, username=update.effective_user.username).run()
                print(context._user_id)
                file_for_delete = os.path.join('', update.message.document.file_name)
                os.remove(file_for_delete)
                await context.bot.send_message(chat_id=context._chat_id, 
                    text=f"{language[7][0]}{update.message.document.file_name} {language[7][1]}")
        except:
            print('can not download doc')

        #global language  # Use the global variable language
        if update.message.text == None:
            print('it is no text')
        else:
            if '🇰🇿' in update.message.text:
                language = kaz_texts
                #markup_maker('language', lan=language)
                print(language)
                await context.bot.send_message(chat_id=update.message.chat_id, 
                                               text='Қазақ тіліне ауыстырылды!', 
                                               reply_markup=markup_maker('main', language))
                
            elif '🇺🇸' in update.message.text:
                language = eng_texts
                await context.bot.send_message(chat_id=update.message.chat_id, 
                                               text='Language switched to English!', 
                                               reply_markup=markup_maker('main', language))



    app = ApplicationBuilder().token('6358744092:AAF8Snr3NiV27Ke4ytSn6KTILUAdcBWZbxw').build()

    app.add_handler(CommandHandler('language', language_bot))
    app.add_handler(CommandHandler('t', language_bot))
    ###########################
    app.add_handler(CommandHandler('start', start))
    ############################
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('k', help))
    ############################
    app.add_handler(CommandHandler('extra', extra))
    app.add_handler(CommandHandler('q', extra))
    ############################
    app.add_handler(CommandHandler('ChatGPT', ChatGPT))
    ###########################
    app.add_handler(CommandHandler('YES', delete))
    app.add_handler(CommandHandler('y', delete))
    ############################
    app.add_handler(CommandHandler('delete_db', delete_db))
    app.add_handler(CommandHandler('d', delete_db))
    ##############################
    app.add_handler(CommandHandler('get_graph', get_graph))
    app.add_handler(CommandHandler('g', get_graph))
    ##############################
    app.add_handler(CommandHandler('site', site))
    app.add_handler(CommandHandler('s', site))
    ##############################
    app.add_handler(CommandHandler('back', back))
    app.add_handler(CommandHandler('n', back))
    #############################
    app.add_handler(CommandHandler('creatinine', creatinine))
    app.add_handler(CommandHandler('kr', creatinine))
    #############################
    app.add_handler(CommandHandler('total_protein', total_protein))
    app.add_handler(CommandHandler('za', total_protein))
    ##############################
    app.add_handler(CommandHandler('urea_nitrogen', urea_nitrogen))
    app.add_handler(CommandHandler('mo', urea_nitrogen))
    ##############################
    app.add_handler(CommandHandler('red_blood_cell', red_blood_cell))
    app.add_handler(CommandHandler('rbc', red_blood_cell))
    ##############################
    app.add_handler(CommandHandler('hemoglobin', hemoglobin))
    app.add_handler(CommandHandler('hm', hemoglobin))
    ##############################
    app.add_handler(CommandHandler('thrombocytes', thrombocytes))
    app.add_handler(CommandHandler('tr', thrombocytes))
    ##############################
    app.add_handler(CommandHandler('total_cholesterol', total_cholesterol))
    app.add_handler(CommandHandler('zhh', total_cholesterol))
    ##############################
    app.add_handler(CommandHandler('blood_glucose', blood_glucose))
    app.add_handler(CommandHandler('kgl', blood_glucose))


    app.add_handler(MessageHandler(filters=filters.ALL, callback=mess_process))
   




    app.run_polling()