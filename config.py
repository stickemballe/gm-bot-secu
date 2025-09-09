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

# L'URL de la boutique principale (la Mini App)
MINIAPP_URL = 'http://gmshop.tilda.ws/'
# L'URL de la page de vérification qui s'ouvrira en Mini App
BOT_VERIFY_URL = 'http://gmshop.tilda.ws/verif' # Changez si votre URL est différente

IMAGE_ACCUEIL_URL = ''
WHATSAPP_LINK = 'https://wa.me/33621884535'
WHATSAPP_SAV_LINK = ''
TELEGRAM_SECOURS_URL = ''
POTATO_URL = ''
INSTAGRAM_URL = ''
SNAPCHAT_URL = ''
