from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")

def costs(update, context):

    string = update.message.text
    elements = string.split(' ')
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])


def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("eat", costs))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
