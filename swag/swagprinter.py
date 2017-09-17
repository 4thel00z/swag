from __future__ import print_function

from swag import colors

#
#   Modifier
#

BOLD = "bold"
UNDERLINE = "underline"
BACKGROUND = "background"

INTENSE = "intense"
INTENSE_BOLD = "intenseBold"
INTENSE_BACKGROUND = "intenseBackground"


def _print_swaggy(color, content, modifier=None, continous=False):
    if modifier is not None:
        color = modifier + color.title()
    text = "{}{}".format(color, content) \
        if continous else "{}{}{}".format(color, content, colors.COLORS["reset"])

    print(text)


def print_black(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["black"], content, continous)


def print_yellow(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["yellow"], content, continous)


def print_green(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["green"], content, continous)


def print_red(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["red"], content, continous)


def print_blue(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["blue"], content, continous)


def print_purple(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["purple"], content, continous)


def print_white(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["white"], content, continous)


def print_cyan(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["cyan"], content, continous)


def reset():
    print(colors.COLORS["reset"])
