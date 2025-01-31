from telethon.sync import TelegramClient
from telethon import events

##########################
import threading
from classes import *
import re
import keyboard
import asyncio
import os
##########################

#---------------------------------------------#
#---------------------------------------------#
api_id = 26774970
api_hash = '15b0b5f063553ecceaf8562cb5589593'
session_name = 'TradingTest'
channel_target = -1002485849706  # Può essere il nome del canale o l'ID
#---------------------------------------------#
#---------------------------------------------#

def exit_on_q():
    print("Premi 'q' per uscire.")
    while True:
        if keyboard.is_pressed('q'):
            print("Uscita...")
            os._exit(0)

exit_thread = threading.Thread(target=exit_on_q)
exit_thread.start()








def parse_order(message):
    if "BUY LIMIT" in message:
        order_type = "BUY LIMIT"
    elif "SELL LIMIT" in message:
        order_type = "SELL LIMIT"
    elif "BUY " in message and "MERCATO" in message:
        order_type = "BUY MARKET"
    elif "SELL " in message and "MERCATO" in message:
        order_type = "SELL MARKET"
    else:
        order_type = None

    # Estrazione dati con regex
    pair_match = re.search(r"([A-Z]{3}/[A-Z]{3})", message)
    price_match = re.search(r"Prezzo\s([\d.]+)", message)
    sl_match = re.search(r"Stop Loss\s+🔴\s+([\d.]+)", message)
    tp_match = re.search(r"Take Profit\s+🟢\s+([\d.]+)", message)

    if order_type and pair_match and price_match and sl_match and tp_match:
        return Order(
            type=order_type,
            pair=pair_match.group(1),
            price=float(price_match.group(1)),
            sl=float(sl_match.group(1)),
            tp=float(tp_match.group(1)),
        )
    return None

def parse_modify_price(message):
    type_match = re.search(r"(BUY|SELL) LIMIT", message)
    pair_match = re.search(r"([A-Z]{3}/[A-Z]{3})", message)
    old_price_match = re.search(r"DA ([\d.]+)", message)
    new_price_match = re.search(r"A ([\d.]+)", message)
    
    if type_match and pair_match and old_price_match and new_price_match:
        return Modify_price(
            type=type_match.group(1) + " LIMIT",
            pair=pair_match.group(1),
            old_price=float(old_price_match.group(1)),
            new_price=float(new_price_match.group(1))
        )
    return None

def handle_parsed_order(function_to_call, message):
    parsed_order = function_to_call(message)
    if parsed_order is None:
            print(f"Errore: il messaggio non è stato riconosciuto correttamente:\n{message}")
            return
    parsed_order.print_info()


def message_decoder(message):
    if message.startswith("📉") | message.startswith("📈") | message.startswith("📊"):
        handle_parsed_order(parse_order, message)
    elif message.startswith("MODIFICARE"):
        print("Modificare")
    elif message.startswith("(BUY") | message.startswith("(SELL"):
        handle_parsed_order(parse_modify_price, message)
    else:
        print(f"Errore: il messaggio non è stato riconosciuto correttamente:\n{message}")

def message_handler(message):
    message_decoder(message)

with TelegramClient(session_name, api_id, api_hash) as client:
    print("Client avviato!")

    @client.on(events.NewMessage(chats=channel_target))
    async def new_message_handler(event):
        new_message = event.message.message
        t = threading.Thread(target=message_handler, args=(new_message,))
        t.start()

    client.run_until_disconnected()