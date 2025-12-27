# kernel_handler.bin.py
# Handler untuk akses dan operasi kernel

class KernelState:
    version = "PyOS Kernel v0.1"
    status = "running"
    boot_time = None

def handle(command, args, shell):
    """
    command: string dari command_handler
    args: list argumen
    shell: instance Shell
    """

    if command == "kernel_version":
        _kernel_version()
    elif command == "boot_info":
        _boot_info()
    else:
        print(f"kernel_handler: unknown kernel command '{command}'")

# ---------- IMPLEMENTASI ----------
def _kernel_version():
    print("Kernel Version:", KernelState.version)

def _boot_info():
    print("Kernel Status:", KernelState.status)
    print("Boot Time   :", KernelState.boot_time or "Not recorded")
