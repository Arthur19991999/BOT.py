from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я эхо бот. Напиши мне что-нибудь, и я повторю это.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    application = Application.builder().token("7171736301:AAETU4ouCUv48dUpTSRQtU_FIkcUcg5hnRw").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, echo))  # Исправлено использование фильтров

    application.run_polling()

if __name__ == '__main__':
    main()



