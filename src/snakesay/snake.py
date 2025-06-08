"""
Generate a snake ASCII art with a speech bubble.

This module provides functions to create a speech bubble for a message
and display it alongside a snake ASCII art.
"""

SNAKE = r"""  \
   \    __
    \  {oo}
       (__)\
         λ \\
           _\\__
          (_____)_
         (________)Oo°
"""


def bubble(message: str) -> str:
    """
    Create a speech bubble for the given message.

    Args:
        message (str): The message to display in the speech bubble.

    Returns:
        str: The formatted speech bubble as a string.
    """
    bubble_length: int = len(message) + 2
    return f"""
 {"_" * bubble_length}
( {message} )
 {"‾" * bubble_length}"""


def say(message: str) -> None:
    """
    Print a snake with a speech bubble containing the given message.

    Args:
        message (str): The message to display. If empty, a default message is used.

    Side Effects:
        Prints the speech bubble and snake ASCII art to stdout.
    """
    if not message:
        message = "I never thought I'd say this, but I have nothing to say."
    print(bubble(message))
    print(SNAKE)
