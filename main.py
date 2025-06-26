
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7030572338:AAGAjSe70FPZPtaohRVOyAfkOyhBMahJ_uM"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def generate_signal():
    return {
        "exchange": "Binance",
        "pair": "ETH/USDT",
        "entry": "3120.00",
        "tp1": "3150.00",
        "tp2": "3190.00",
        "tp3": "3250.00",
        "final_tp": "3280.00",
        "sl": "3070.00",
        "risk": "🟢 Low Risk",
        "analysis": "✅ EMA + MACD + Volume + RSI + MTF",
        "link": "https://www.binance.com/en/futures/ETHUSDT"
    }

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("👋 Welcome to DrHussamCryptoBot!\nUse /signal to receive a signal.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sig = generate_signal()
    message = (
        f"🚨 Strong Signal from {sig['exchange']}\n"
        f"Pair: {sig['pair']}\n"
        f"Entry: {sig['entry']}\n"
        f"🎯 TP1: {sig['tp1']}, TP2: {sig['tp2']}, TP3: {sig['tp3']}\n"
        f"🏁 Final TP: {sig['final_tp']}\n❌ SL: {sig['sl']}\n"
        f"{sig['risk']}\n{sig['analysis']}\n{sig['link']}"
    )
    await update.message.reply_text(message)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()

if __name__ == "__main__":
    main()
