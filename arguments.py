import sys


def get_username() -> tuple[str, str] | tuple:
    """Return tuple with usernames and empty tuple if usernames not state."""
    if "-u1" in sys.argv or "-u2" in sys.argv:
        nick1_index: int = sys.argv.index("-u1")+1
        nick2_index: int = sys.argv.index("-u2")+1
        nick1: str = sys.argv[nick1_index]
        nick2: str = sys.argv[nick2_index]
        return nick1, nick2
    else:
        return ()


def get_text() -> str | None:
    """Return string with custom text or None if text not state."""
    if "-t" in sys.argv or "--text" in sys.argv:
        text_index: int = sys.argv.index("-t")+1 if "-t" in sys.argv else sys.argv.index("--text")+1
        text: str = sys.argv[text_index]
        return text
    else:
        return


def get_support() -> bool:
    """Print in console help menu."""
    if "-h" in sys.argv or "--help" in sys.argv:
        print("""
Syntax: python3 give_love.py [-u1|-u2|-c|-t|-h]
options:
-u1, -u2 <username>                           Set custom username. Default: user1, user2.
-c --color <r,g,b,y,p,bl,w>                   Set custom color for output text. Default: w (white).
-t --text "<custom text>"                     Set custom output text(love string). Default: "oh loves you,".
-h --help                                     Get help.
""")
        return True
    else:
        return False
