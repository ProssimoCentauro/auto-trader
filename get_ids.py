from telethon.sync import TelegramClient
import sys
from colorama import Fore, Back, Style, init

init()

# Credenziali per Telegram API
api_id = 26774970
api_hash = '15b0b5f063553ecceaf8562cb5589593'

# Nome della sessione
session_name = 'TradingTest'


# Creazione del client
with TelegramClient(session_name, api_id, api_hash) as client:
    # Stampa il tuo nome per confermare l'accesso
    me = client.get_me()
    print(f"Autenticato come: {me.first_name}")

# Creazione del client
with TelegramClient(session_name, api_id, api_hash) as client:
    # Ottieni tutti i dialoghi (canali, gruppi, chat)
    dialogs = client.get_dialogs()

    # Filtra solo i canali
    for dialog in dialogs:
        if dialog.is_channel:
            # Aggiungi entity.username per ottenere l'username
            username = dialog.entity.username if dialog.entity.username else "No username"
            print(f"Canale: {dialog.name}, Username: {username}, ID: {dialog.id}")
