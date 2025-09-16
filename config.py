import os
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
CAPTCHA_SECRET_KEY = os.getenv("CAPTCHA_SECRET_KEY")

if not BOT_TOKEN or not CAPTCHA_SECRET_KEY:
    raise ValueError("Les secrets du bot ou du captcha sont manquants dans .env")

MINIAPP_URL = 'https://gm75shop.com/'

BOT_VERIFY_URL = 'https://gm75shop.com/bot-verify'

IMAGE_ACCUEIL_URL = 'https://file.garden/aIhdnTgFPho75N46/GM%20SHOP/image-acceuil.jpg'
WHATSAPP_LINK = 'https://wa.me/33621884535'