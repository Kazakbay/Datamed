from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram.ext import MessageHandler, filters
from graphic_builder import Graphic_builder
from data_manager import Data_manager
import os

main_keyboard = [[KeyboardButton(text='/help'), KeyboardButton(text='/get_graph')],
            [KeyboardButton(text='/AI'), KeyboardButton(text='/get_info')]]
main_markup = ReplyKeyboardMarkup(keyboard=main_keyboard)

graph_keyboard = [[KeyboardButton(text='/creatinine'), KeyboardButton(text='/urea_nitrogen')],
                  [KeyboardButton(text='/total_protein'),KeyboardButton(text='/back')]]
graph_markup = ReplyKeyboardMarkup(keyboard=graph_keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=context._chat_id, text="Hi, I'm Qolqanat, I can help you!", reply_markup=main_markup)


async def get_graph(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=context._chat_id, text='''
You pressed the get_graph button. Please choose what you want to receive:''', 
                                    reply_markup=graph_markup)


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=context._chat_id, text='Main menu', reply_markup=main_markup)


async def get_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
            await context.bot.send_message(chat_id=context._chat_id, text=f"file: {update.message.document.file_name} downloaded")
    except:
        pass

async def creatinine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update._effective_user.username
    if os.path.isfile(f'Креатинин_{username}.png'):
        os.remove(f'Креатинин_{username}.png')
    Graphic_builder('Креатинин', username=username).run()
    if os.path.isfile(f'Креатинин_{username}.png'):
        await context.bot.send_document(chat_id=context._chat_id, document=f'Креатинин_{username}.png')
        


async def total_protein(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update._effective_user.username
    if os.path.isfile(f'Общий белок_{username}.png'):
        os.remove(f'Общий белок_{username}.png')
    Graphic_builder('Общий белок', username=username).run()
    if os.path.isfile(f'Общий белок_{username}.png'):
        await context.bot.send_document(chat_id=context._chat_id, document=f'Общий белок_{username}.png')


async def urea_nitrogen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update._effective_user.username
    if os.path.isfile(f'Мочевина_{username}.png'):
        os.remove(f'Мочевина_{username}.png')
    Graphic_builder('Мочевина', username=username).run()
    if os.path.isfile(f'Мочевина_{username}.png'):
        await context.bot.send_document(chat_id=context._chat_id, document=f'Мочевина_{username}.png')

        


app = ApplicationBuilder().token('6358744092:AAF8Snr3NiV27Ke4ytSn6KTILUAdcBWZbxw').build()


app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('get_graph', get_graph))
app.add_handler(CommandHandler('back', back))
app.add_handler(CommandHandler('creatinine', creatinine))
app.add_handler(CommandHandler('total_protein', total_protein))
app.add_handler(CommandHandler('urea_nitrogen', urea_nitrogen))
app.add_handler(MessageHandler(filters=filters.ALL, callback=get_doc))




app.run_polling()