from telethon.sync import TelegramClient
from telethon import events

def get_file_num():
    with open("conf", "r") as file:
        content = file.read()
    current_file = int(content.split(":")[1].strip())
    return current_file


def update_file_num():
    try:
        current_num = get_file_num()
        if current_num == 3:
            new_num = 1
        else:
            new_num = current_num + 1
        new_content = f"current file: {new_num}\n"

        with open("conf", "w") as file:
            file.write(new_content)
        print(f"Numero incrementato con successo! Nuovo valore: {new_num}")
    except Exception as e:
        print(f"Errore durante l'incremento del numero: {e}")

def write_on_file(file_name, message):
    try:
        with open(file_name, "w") as file:
            file.write(message)
            print(f"Testo scritto con successo su '{file_name}'!")
    except Exception as e:
        print(f"Errore durante la scrittura su file: {e}")

#---------------------------------------------
#---------------------------------------------
api_id = 26774970
api_hash = '15b0b5f063553ecceaf8562cb5589593'
session_name = 'TradingTest'
channel_target = -1002485849706  # Può essere il nome del canale o l'ID
#---------------------------------------------
#---------------------------------------------

with TelegramClient(session_name, api_id, api_hash) as client:
    print("Client avviato!")

    @client.on(events.NewMessage(chats=channel_target))
    async def new_message_handler(event):
        new_message = event.message.message
        current_file = f"m{get_file_num()}"
        write_on_file(current_file, new_message)
        update_file_num()

    client.run_until_disconnected()







'''
        # Scrivi un messaggio in risposta (o in un altro canale/chat)
        await client.send_message('me', f"Messaggio ricevuto da {channel_target}: {new_message}")
'''
    # Mantieni il client attivo
    #print("In ascolto per nuovi messaggi...")
