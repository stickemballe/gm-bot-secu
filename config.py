import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# --- FLAG pour désactiver temporairement la vérif anti-bot ---
DISABLE_VERIFICATION = os.getenv("DISABLE_VERIFICATION", "0") == "1"

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Si la vérif est active, la clé captcha est obligatoire.
if not DISABLE_VERIFICATION:
    CAPTCHA_SECRET_KEY = os.getenv("CAPTCHA_SECRET_KEY")
    if not BOT_TOKEN or not CAPTCHA_SECRET_KEY:
        raise ValueError("Les secrets du bot ou du captcha sont manquants dans .env")
else:
    # Vérif désactivée : on n'exige pas la clé captcha.
    CAPTCHA_SECRET_KEY = os.getenv("CAPTCHA_SECRET_KEY", "")
    if not BOT_TOKEN:
        raise ValueError("Le BOT_TOKEN est manquant dans .env")

# L'URL de la boutique principale (la Mini App)
MINIAPP_URL = 'https://gm75shop.com/'
# L'URL de la page de vérification (inutile pendant la désactivation, mais on garde)
BOT_VERIFY_URL = 'https://gm75shop.com/verif'

IMAGE_ACCUEIL_URL = ''
WHATSAPP_LINK = 'https://wa.me/33621884535'
