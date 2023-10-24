from telegram import Update, Document, File, Message
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, TypeHandler

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def eacho(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(update.message.from_user.id, text=update.message.text)

async def get_doc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_id = update.message.document.file_id
    print(file_id)
    await context.bot.send_message(update.effective_chat.id, text=f'I recieved document! Here file id {file_id}')


app = ApplicationBuilder().token('6358744092:AAF8Snr3NiV27Ke4ytSn6KTILUAdcBWZbxw').build()

app.add_handler(CommandHandler('Hello', hello))
app.add_handler(MessageHandler(filters=filters.TEXT, callback=eacho))
app.add_handler(TypeHandler(type=Message.document, callback=get_doc))

app.run_polling()
