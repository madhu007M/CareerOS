"""
CareerOS Command Line Interface
"""

import sys
import subprocess


def runserver():
    subprocess.run(
        [
            "uvicorn",
            "backend.main:app",
            "--reload"
        ]
    )


def browser_test():
    subprocess.run(
        [
            sys.executable,
            "-m",
            "backend.app.browser.test_browser"
        ]
    )


def help_menu():

    print("\nCareerOS CLI\n")

    print("Available Commands:\n")

    print(" runserver")
    print(" browser-test")


def main():

    if len(sys.argv) < 2:
        help_menu()
        return

    command = sys.argv[1]

    if command == "runserver":
        runserver()

    elif command == "browser-test":
        browser_test()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()