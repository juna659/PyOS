# shell/shell.py

from fs.bin.input_user_handler import handle as input_user_handle
from fs.bin.command_handler import handle as command_handle

class Shell:
    def __init__(self):
        self.running = True
        self.hostname = "localhost"
        self.system_name = "PyOS"
        self.user_home = "~"
        self.cwd = self.user_home

    def build_prompt(self):
        path = "~" if self.cwd == self.user_home else self.cwd.replace(self.user_home, "~")
        return f"{self.hostname}@{self.system_name}:{path}[$] "

    def start(self):
        print("[SHELL] PyOS Shell started.")
        print("[SHELL] Type 'exit' to quit.\n")
        while self.running:
            raw = input(self.build_prompt())
            command, args = input_user_handle(raw)

            if not command:
                continue

            if command == "exit":
                print("[SHELL] Shutting down...")
                self.running = False
                continue

            command_handle(command, args, self)
