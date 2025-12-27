# user_handler.bin.py
# Handler untuk informasi user

class UserState:
    username = "user"
    fullname = "PyOS User"
    role = "default"

def handle(command, args, shell):
    """
    command: string dari command_handler
    args: list argumen
    shell: instance Shell
    """

    if command == "whoami":
        _whoami()
    elif command == "user_info":
        _user_info()
    else:
        print(f"user_handler: unknown user command '{command}'")

# ---------- IMPLEMENTASI ----------
def _whoami():
    print(UserState.username)

def _user_info():
    print("User Information:")
    print(" Username:", UserState.username)
    print(" Fullname:", UserState.fullname)
    print(" Role    :", UserState.role)
