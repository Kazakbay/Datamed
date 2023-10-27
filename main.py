from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
import os
from data_manager import Data_manager
from graph_builder import Graphic_builder

keyboard = [[InlineKeyboardButton('Общий белок', callback_data='Общий белок')],
                [InlineKeyboardButton('Мочевина', callback_data='Мочевина')],
                [InlineKeyboardButton('Креатинин', callback_data='Креатинин')]]
reply_markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, Я бот, который поможет тебе с твоими анализами. Нажми на одну из опций для получения динамики медицинских показателей. Для пополнения данных просто отправь PDF файл с результатами.', reply_markup=reply_markup)


async def get_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if type(update.message.document.file_id) == str:
        file_id = update.message.document.file_id
        new_file = await context.bot.get_file(file_id=file_id)
        download_path = os.path.join('trash', update.message.document.file_name)
        await new_file.download_to_drive(download_path)
        Data_manager(download_path).run()
        await context.bot.send_message(chat_id=context._chat_id, text="Выбери опцию", reply_markup=reply_markup)
        


async def send_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if type(query.data) == str:
        if os.path.exists(f"{query.data}.png"):
            os.remove(f"{query.data}.png")
    if query.data == 'Общий белок':
        Graphic_builder('Общий белок').run()
    elif query.data == 'Мочевина':
        Graphic_builder('Мочевина').run()
    elif query.data == 'Креатинин':
        Graphic_builder('Креатинин').run()
    await query.edit_message_text(text=f"Вы выбрали: {query.data}")
    if os.path.isfile(f'{query.data}.png'):
        await context.bot.send_document(chat_id=query.from_user.id, document=f'{query.data}.png')
        text = 'Выбирите опцию'
    else:
        text = 'Нет данных, пожалуйста отправьте данные'
    await context.bot.send_message(chat_id=context._chat_id, text=text, reply_markup=reply_markup)


app = ApplicationBuilder().token('6358744092:AAF8Snr3NiV27Ke4ytSn6KTILUAdcBWZbxw').build()


app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters=filters.ALL, callback=get_doc))
app.add_handler(CallbackQueryHandler(send_result))


app.run_polling()