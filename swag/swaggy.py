from sys import stdout

from swag import colors

BOLD = "bold"
UNDERLINE = "underline"
BACKGROUND = "background"

INTENSE = "intense"
INTENSE_BOLD = "intenseBold"
INTENSE_BACKGROUND = "intenseBackground"


def swag(color_name, content, modifier=None, continuous=False, file=stdout):

    if modifier is not None:
        color_name = modifier + color_name.title()

    color = colors.COLORS[color_name]

    text = (
        "{0}{1}".format(color, content)
        if continuous
        else "{0}{1}{2}".format(color, content, colors.COLORS["reset"])
    )

    print(text, file=file)


def black(content, modifier=None, continuous=False, file=stdout):
    swag("black", content, modifier, continuous, file=file)


def yellow(content, modifier=None, continuous=False, file=stdout):
    swag("yellow", content, modifier, continuous, file=file)


def green(content, modifier=None, continuous=False, file=stdout):
    swag("green", content, modifier, continuous, file=file)


def red(content, modifier=None, continuous=False, file=stdout):
    swag("red", content, modifier, continuous, file=file)


def blue(content, modifier=None, continuous=False, file=stdout):
    swag("blue", content, modifier, continuous, file=file)


def purple(content, modifier=None, continuous=False, file=stdout):
    swag("purple", content, modifier, continuous, file=file)


def white(content, modifier=None, continuous=False, file=stdout):
    swag("white", content, modifier, continuous, file=file)


def cyan(content, modifier=None, continuous=False, file=stdout):
    swag("cyan", content, modifier, continuous, file=file)


def reset():
    print(colors.COLORS["reset"])


def clear():
    print("\x1b[2J\x1b[H")
