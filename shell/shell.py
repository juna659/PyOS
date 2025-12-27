# PyOS Shell (handler-ready)
from fs.bin.input_user_handler import handle as input_user_handler
from fs.bin.command_handler import handle as command_handler

class Shell:
    def __init__(self):
        self.running = True
        self.hostname = "localhost"
        self.system_name = "PyOS"
        self.user_home = "~"
        self.cwd = self.user_home

    # ---------- PROMPT ----------
    def build_prompt(self):
        path = "~" if self.cwd == self.user_home else self.cwd.replace(self.user_home, "~")
        return f"{self.hostname}@{self.system_name}:{path}[$] "

    # ---------- MAIN LOOP ----------
    def start(self):
        print("[SHELL] PyOS Shell started.")
        print("[SHELL] Type 'exit' to quit.\n")
        while self.running:
            raw = input(self.build_prompt())
            command, args = input_user_handler.handle(raw)

            if not command:
                continue

            # exit is special internal command
            if command == "exit":
                print("[SHELL] Shutting down...")
                self.running = False
                continue

            # kirim ke command_handler
            command_handler.handle(command, args, self)
