# shell_handler.bin.py
# Handler untuk semua command internal shell

import os
from datetime import datetime

def handle(command, args, shell):
    """
    command: string command dari command_handler
    args: list argumen
    shell: instance Shell
    """

    if command == "cd":
        _cd(args, shell)
    elif command == "mkdir":
        _mkdir(args, shell)
    elif command == "touch":
        _touch(args, shell)
    elif command == "cat":
        _cat(args, shell)
    elif command == "help":
        _help(args, shell)
    elif command == "info":
        _info(args, shell)
    elif command == "date":
        _date(args, shell)
    elif command == "whoami":
        _whoami(args, shell)
    else:
        print(f"shell_handler: unknown shell command '{command}'")

# ---------- IMPLEMENTASI COMMAND ----------
def _cd(args, shell):
    if not args:
        shell.cwd = shell.user_home
        return
    target = args[0]
    if target == "~":
        shell.cwd = shell.user_home
    else:
        path = os.path.abspath(os.path.join(shell.cwd, target))
        if os.path.isdir(path):
            shell.cwd = path
        else:
            print("cd: no such directory:", target)

def _mkdir(args, shell):
    if not args:
        return print("mkdir: missing argument")
    path = os.path.join(shell.cwd, args[0])
    os.makedirs(path, exist_ok=True)

def _touch(args, shell):
    if not args:
        return print("touch: missing filename")
    path = os.path.join(shell.cwd, args[0])
    open(path, "a").close()

def _cat(args, shell):
    if not args:
        return print("cat: missing filename")
    path = os.path.join(shell.cwd, args[0])
    if not os.path.exists(path):
        print("cat: file not found:", args[0])
        return
    print(open(path).read())

def _help(args, shell):
    print("Available shell commands:")
    cmds = ["cd", "mkdir", "touch", "cat", "help", "info", "date", "whoami"]
    for c in cmds:
        print(" -", c)

def _info(args, shell):
    print("PyOS System Info:")
    print(" Hostname:", shell.hostname)
    print(" System  :", shell.system_name)
    print(" Home    :", shell.user_home)

def _date(args, shell):
    print(datetime.now())

def _whoami(args, shell):
    print("user")  # nanti bisa diganti dynamic
