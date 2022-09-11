import sys


def get_username() -> tuple[str, str] | tuple:
    """Return tuple with usernames and empty tuple if usernames not state."""
    if "-n1" in sys.argv or "-n2" in sys.argv:
        nick1_index: int = sys.argv.index("-n1")+1
        nick2_index: int = sys.argv.index("-n2")+1
        nick1: str = sys.argv[nick1_index]
        nick2: str = sys.argv[nick2_index]
        return nick1, nick2
    else:
        return ()
