from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import qrcode
import io

# Telegram bot tokenini kiriting
TOKEN = '7268540552:AAHKBqxt4ysWqWzv-kl7e5WQPO1yKlT8bvk'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salom! Menga matn yuboring va men sizga QR kod yaratib beraman.')

async def generate_qr(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    
    bio = io.BytesIO()
    bio.name = 'qr.png'
    img.save(bio, 'PNG')
    bio.seek(0)

    await update.message.reply_photo(photo=bio, caption="Mana sizning QR kodingiz")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_qr))

    app.run_polling()

if __name__ == '__main__':
    main()
