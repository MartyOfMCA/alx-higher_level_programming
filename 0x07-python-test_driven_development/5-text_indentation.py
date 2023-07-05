#!/usr/bin/python3
"""
This module defines the text_indentation function
# Test for a valid text
>>> text_indentation("Martin Amankwaa. Martin:Amankwaa? Martin")
Martin Amankwaa
<BLANKLINE>
Martin
<BLANKLINE>
Amankwaa
<BLANKLINE>
Martin
"""


def text_indentation(text=""):
    """
    Prints text in a given string.

    Parameters
    text : string
        The sequence of tex to be displayed

    Raises
    TypeError
        When the given text is not a string
    """

    delimiters = (".", "?", ":")
    skip_flag = False

    if (type(text) is not str or text == ""):
        raise TypeError("text must be a string")

    for character in text:
        if (character in delimiters):
            skip_flag = True
            print("{}\n".format(character))
            continue
        if (skip_flag is True and character == " "):
            continue
        else:
            skip_flag = False
        print(character, end="")
