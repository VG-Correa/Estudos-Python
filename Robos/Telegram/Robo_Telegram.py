import Responses
import Constantes
from telegram.ext import*

def start_command(update,context):
#    update.message.reply_text(f"Olá {update.message.from_user['first_name']} seja bem vindo")
    update.message.reply_text(f"Olá minha frô, coisa mais lindaaaaaaa, seja bem vinda a meu primeiro BOT\nVocê pode utilizar por enquanto os seguintes comandos:\nOi\nBeleza e você?\nEu te amo")

def help_command(update,context):
    update.message.reply_text(f"oi ou olá -> retorna uma saudação\ncanal -> retorna")

def handle_message(update,context):
    txt = str(update.message.text).lower()
    response = Responses.simple_responses(txt)
    update.message.reply_text(response)

def error(update,context):
    print(f"Update: {update} caused error: {context.error}")

def main():
    updater = Updater(Constantes.API_KEY,use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("Start",start_command))
    dp.add_handler(CommandHandler("Help",help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()