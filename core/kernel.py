# PyOS Kernel

class Kernel:
    def __init__(self):
        self.version = "PyOS Kernel v0.1"
        self.status = "initialized"

    def boot(self):
        print("[BOOT] Kernel starting...")
        print(f"[BOOT] Kernel version: {self.version}")
        self.status = "running"
        print("[BOOT] Kernel ready. Handing control to shell...")
