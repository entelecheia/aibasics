"""Command line interface for aibasics"""

from aibasics import get_version


def main() -> None:
    """Main function for the CLI"""
    print(f"aibasics {get_version()}")


if __name__ == "__main__":
    main()
