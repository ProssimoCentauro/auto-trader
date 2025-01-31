with open("conf", "r") as file:
    contenuto = file.read()
current_file = int(contenuto.split(":")[1].strip())
