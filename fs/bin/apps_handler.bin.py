# apps_handler.bin.py
# Handler untuk mengelola aplikasi di folder apps/

import os

APPS_DIR = os.path.abspath("./apps")

def handle(command, args, shell):
    """
    command: string dari command_handler
    args: list argumen
    shell: instance Shell
    """

    if command == "run_app":
        _run_app(args)
    elif command == "list_apps":
        _list_apps()
    else:
        print(f"apps_handler: unknown apps command '{command}'")

# ---------- IMPLEMENTASI ----------
def _list_apps():
    if not os.path.exists(APPS_DIR):
        print("No apps folder found.")
        return
    apps = [f for f in os.listdir(APPS_DIR) if os.path.isfile(os.path.join(APPS_DIR, f))]
    if not apps:
        print("No applications installed.")
        return
    print("Installed applications:")
    for a in apps:
        print(" -", a)

def _run_app(args):
    if not args:
        print("run_app: missing application name")
        return
    app_name = args[0]
    app_path = os.path.join(APPS_DIR, app_name)
    if not os.path.exists(app_path):
        print("run_app: application not found:", app_name)
        return

    try:
        # jalankan aplikasi sebagai Python script
        with open(app_path, "r") as f:
            code = f.read()
        exec(code, {})
    except Exception as e:
        print("run_app: error running", app_name, "-", e)
