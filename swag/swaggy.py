from swag import colors
from sys import stdout

BOLD = "bold"
UNDERLINE = "underline"
BACKGROUND = "background"

INTENSE = "intense"
INTENSE_BOLD = "intenseBold"
INTENSE_BACKGROUND = "intenseBackground"


def swag(text, content, modifier=None, continuous=False, file=stdout):
    if modifier is not None:
        text = modifier + text.title()
    text = (
        "{0}{1}".format(text, content)
        if continuous
        else "{0}{1}{2}".format(text, content, colors.COLORS["reset"])
    )
    print(text, file=stdout)


def black(content, modifier=None, continuous=False):
    swag(colors.COLORS["black"], content, modifier, continuous)


def yellow(content, modifier=None, continuous=False):
    swag(colors.COLORS["yellow"], content, modifier, continuous)


def green(content, modifier=None, continuous=False):
    swag(colors.COLORS["green"], content, modifier, continuous)


def red(content, modifier=None, continuous=False):
    swag(colors.COLORS["red"], content, modifier, continuous)


def blue(content, modifier=None, continuous=False):
    swag(colors.COLORS["blue"], content, modifier, continuous)


def purple(content, modifier=None, continuous=False):
    swag(colors.COLORS["purple"], content, modifier, continuous)


def white(content, modifier=None, continuous=False):
    swag(colors.COLORS["white"], content, modifier, continuous)


def cyan(content, modifier=None, continuous=False):
    swag(colors.COLORS["cyan"], content, modifier, continuous)


def reset():
    print(colors.COLORS["reset"])


def clear():
    print("\x1b[2J\x1b[H")
