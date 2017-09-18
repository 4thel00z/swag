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
    text = "{0}{1}".format(color, content) \
        if continous else "{0}{1}{2}".format(color, content, colors.COLORS["reset"])

    print(text)


def print_black(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["black"], content, modifier, continous)


def print_yellow(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["yellow"], content, modifier, continous)


def print_green(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["green"], content, modifier, continous)


def print_red(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["red"], content, modifier, continous)


def print_blue(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["blue"], content, modifier, continous)


def print_purple(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["purple"], content, modifier, continous)


def print_white(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["white"], content, modifier, continous)


def print_cyan(content, modifier=None, continous=False):
    _print_swaggy(colors.COLORS["cyan"], content, modifier, continous)


def reset():
    print(colors.COLORS["reset"])
