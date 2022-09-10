import os

from time import sleep
from colorama import init, Fore, Style

COLOR = Fore.MAGENTA  # text color in terminal
STYLE = Style.BRIGHT

# users
USER1 = "u1"
USER2 = "u2"

init(autoreset=True)  # init colorama


def clear_screen() -> None:
    """Clear screen based on user system."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main() -> None:
    clear_screen()  # clean screen for aesthetic output

    love_string = f"|                      @{USER1} очень любит тебя, @{USER2}!                      |"
    wrapper = "=" * len(love_string)

    text: list = [
        wrapper,
        love_string,
        wrapper,
    ]

    for text_line in text:
        print("\n")
        for char in text_line:
            print(COLOR + STYLE + char, flush=True, end="")
            sleep(.03)


if __name__ == "__main__":
    main()
