# input_user_handler.bin.py
# Handler untuk input mentah dari user sebelum masuk ke command handler

def handle(raw_input):
    """
    Menerima input mentah string dari shell.
    Mengembalikan tuple: (command, args)
    """

    if not raw_input or raw_input.strip() == "":
        return None, []

    parts = raw_input.strip().split()
    command = parts[0]
    args = parts[1:] if len(parts) > 1 else []

    return command, args
