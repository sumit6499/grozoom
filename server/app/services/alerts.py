import telegram
from app.core.config import settings

bot = None

def initialize_telegram_bot():
    global bot
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)

async def send_telegram_alert(alert_type: str, message: str):
    global bot
    await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=f"{alert_type}: {message}")
