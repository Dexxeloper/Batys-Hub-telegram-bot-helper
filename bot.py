import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables")

keyboard = [
    ["📌 О хабе", "📅 Мероприятия"],
    ["🧑‍💻 Резидентство", "📞 Контакты"],
    ["❓ FAQ"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать в хаб! Выберите раздел:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📌 О хабе":
        await update.message.reply_text("Наш хаб — пространство для стартапов.")

    elif text == "📅 Регистрация в клуб разработчиков":
        await update.message.reply_text("docs.google.com/forms/d/e/1FAIpQLSekio6XkFhoEIT0fq2584JnDfLfCqBgv4-Bim9O2ZJrOwjCVQ/viewform?usp=dialog")

    elif text == "🧑‍💻 Резидентство":
        await update.message.reply_text("Резиденство в Astana Hub даёт предпринимателям следующие преимущества: Налоговые преференции. Освобождение от уплаты корпоративного налога, НДС, налога на доходы работников и социальных отчислений. Это позволяет сократить издержки и реинвестировать сэкономленные средства в развитие проекта. Визовые льготы. Упрощённый режим получения рабочих виз для иностранных специалистов и членов их семей сроком до 5 лет, без необходимости получения специальных разрешений.  Доступ к инфраструктуре. Резиденты могут арендовать рабочие места в рамках программы Hub Space прямо внутри Astana Hub, в том числе лаборатории и оборудование. Участие в акселераторах и грантах. Отдельные проекты получают поддержку со стороны государства и инвесторов. Поддержка масштабирования и экспорта продуктов. Резиденты получают возможность выходить на международные рынки. ")

    elif text == "📞 Instagram":
        await update.message.reply_text("https://www.instagram.com/batys.hub?igsh=ZmJqOXUwanRuczZi")

    elif text == "❓ FAQ":
        await update.message.reply_text("Задайте вопрос 🙂")

    else:
        await update.message.reply_text("Используйте кнопки меню.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
