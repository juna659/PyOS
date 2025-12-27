# command_handler.bin.py
# Handler untuk routing command ke handler yang sesuai

from fs.bin import shell_handler, kernel_handler, apps_handler, user_handler

def handle(command, args, shell):
    """
    command: string command dari input_user_handler
    args: list argumen
    shell: instance Shell
    """

    if not command:
        return

    # shell internal commands
    shell_commands = ["cd", "mkdir", "touch", "cat", "help", "info", "date", "whoami"]
    if command in shell_commands:
        shell_handler.handle(command, args, shell)
        return

    # kernel related commands
    kernel_commands = ["kernel_version", "boot_info"]
    if command in kernel_commands:
        kernel_handler.handle(command, args, shell)
        return

    # apps related commands
    apps_commands = ["run_app", "install_app"]
    if command in apps_commands:
        apps_handler.handle(command, args, shell)
        return

    # user related commands
    user_commands = ["whoami", "user_info"]
    if command in user_commands:
        user_handler.handle(command, args, shell)
        return

    # fallback
    print(f"command_handler: unknown command '{command}'")
