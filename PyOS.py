# PyOS Launcher

from core.kernel import Kernel
from shell.shell import Shell

def main():
    print("=== PyOS Launcher ===")
    
    kernel = Kernel()
    kernel.boot()

    shell = Shell()
    shell.start()

if __name__ == "__main__":
    main()
