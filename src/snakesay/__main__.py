"""
Command-line interface for the snakesay package.

This module provides an entry point for displaying a snake with a speech bubble
containing a user-supplied message. If no message is provided, a default message is used.
"""

import sys

from snakesay import snake


def main():
    """
    Run the snakesay CLI.

    Joins command-line arguments into a message and passes it to the snake.say function.
    If no arguments are provided, a default message is displayed.
    """
    snake.say(" ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
