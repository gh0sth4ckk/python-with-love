import os
import sys

from time import sleep

from colorama import init, Fore, Style
from emoji import emojize


COLORS: list = ["r", "g", "b", "p", "y", "w", "bl"]  # Text colors in terminal.
COLOR = Fore.WHITE  # Color by default
HEART = ":white_heart:"  # Heart by default
STYLE = Style.BRIGHT


# Usernames
USER1 = "u1"
USER2 = "u2"

init(autoreset=True)  # Init colorama.


def clear_screen() -> None:
    """Clear screen based on user system."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def color_settings() -> None:
    """Setting all colors in app."""
    global COLOR, HEART

    if "-c" or "--color" in sys.argv:
        color_index: int = sys.argv.index("-c")+1
        color_type: str = sys.argv[color_index]
        if color_type in COLORS:
            match color_type:
                case "r":
                    COLOR = Fore.RED
                    HEART = ":red_heart:"
                case "g":
                    COLOR = Fore.GREEN
                    HEART = ":green_heart:"
                case "b":
                    COLOR = Fore.BLUE
                    HEART = ":blue_heart:"
                case "p":
                    COLOR = Fore.MAGENTA
                    HEART = ":purple_heart:"
                case "w":
                    COLOR = Fore.WHITE
                    HEART = ":white_heart:"
                case "y":
                    COLOR = Fore.YELLOW
                    HEART = ":yellow_heart:"
                case "bl":
                    COLOR = Fore.BLACK
                    HEART = ":black_heart:"
        else:
            print(Fore.RED + "[!] You enter incorrect color type")


def main() -> None:
    clear_screen()  # Clean screen for aesthetic output.
    color_settings()  # Settings all colors before start.

    love_string = emojize(
        f"|                     {HEART} @{USER1} очень любит тебя, @{USER2}! {HEART}                     |"
    )
    wrapper = "=" * (len(love_string) + 2)

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

    input(COLOR + "\nEnter any key to exit...")
    clear_screen()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(emojize(Fore.RED + "You kill love :broken_heart:"))
