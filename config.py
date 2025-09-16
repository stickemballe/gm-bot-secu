import os
import logging
from dotenv import load_dotenv

# --- Chargement .env ---
load_dotenv()

# --- Logging de base ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# --- Secrets et configuration ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
CAPTCHA_SECRET_KEY = os.getenv("CAPTCHA_SECRET_KEY")

# Compat : accepte ADMIN_IDS="id1,id2" OU ADMIN_ID="id_unique"
_raw_admins = os.getenv("ADMIN_IDS", os.getenv("ADMIN_ID", "")).replace(" ", "")
ADMIN_IDS = [int(x) for x in _raw_admins.split(",") if x]

# URLs de ton projet
MINIAPP_URL = "https://gm75shop.com/"
BOT_VERIFY_URL = "https://gm75shop.com/bot-verify"
IMAGE_ACCUEIL_URL = "https://file.garden/aIhdnTgFPho75N46/GM%20SHOP/image-acceuil.jpg"
WHATSAPP_LINK = "https://wa.me/33621884535"

# --- Validations minimales ---
if not BOT_TOKEN or not CAPTCHA_SECRET_KEY:
    raise ValueError("Les secrets du bot ou du captcha sont manquants dans .env")

if not ADMIN_IDS:
    logger.warning("Aucun admin défini. Renseigne ADMIN_IDS ou ADMIN_ID dans les variables d'environnement.")

# --- Helper pratique ---
def is_admin(user_id: int) -> bool:
    """Retourne True si l'utilisateur est admin (défini dans ADMIN_IDS)."""
    return user_id in ADMIN_IDS
