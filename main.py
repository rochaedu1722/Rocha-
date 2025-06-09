
import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Updater

# Modos ativos
MODOS_ATIVOS = ["ZENITH", "OMEGA", "MOSCOU"]

# Carrega variáveis
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

def enviar_sinal_exemplo():
    print("🏆 Sinal gerado [ZENITH][OMEGA][MOSCOU]")
    # Aqui seria o envio real via Telegram

def main():
    print("Iniciando Rochinha Pé Duro v1.2 com modos:", MODOS_ATIVOS)
    enviar_sinal_exemplo()

    updater = Updater(token=TOKEN, use_context=True)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
