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

    '''
    channel = client.get_entity('TheRealFX Signals')  # Usa il nome del canale o l'username
    print(channel.id)  # Mostra l'ID numerico del canale
    sys.exit()
    '''

    # Nome o ID del canale privato
    #channel_username = 'username_del_canale_privato'  # Oppure l'ID del canale
    channel = client.get_entity(-1001243412416)

    # Recupera i messaggi più recenti
    messages = client.get_messages(channel, limit=10)
    for message in messages:
        print(Fore.YELLOW + "--------------------------------")
        #print(Back.YELLOW + "--------------------------------")
        print(Style.RESET_ALL + message.text)

'''
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
'''
