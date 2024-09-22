from sys import stdout

from swag.colors import colors_attr, COLORS

BOLD = "bold"
UNDERLINE = "underline"
BACKGROUND = "background"

INTENSE = "intense"
INTENSE_BOLD = "intense_bold"
INTENSE_BACKGROUND = "intense_background"


def swag(color_name, content, modifier=None, continuous=False, file=stdout):
    """
    Swag prints colored text to the console.
    The following colors are available:
    - black
    - yellow
    - green
    - red
    - blue
    - purple
    - white
    - cyan

    Also available are the following modifiers:
    - bold
    - underline
    - background
    - intense
    - intense_bold
    - intense_background

    The color_name and modifier are case-insensitive.

    :param color_name:
    :param content:
    :param modifier:
    :param continuous:
    :param file:
    :return:
    """
    if modifier is not None:
        color_name = "_".join([modifier.lower(), color_name.lower()])

    color = COLORS[color_name]

    text = (
        f"{color}{content}"
        if continuous
        else f"{color}{content}{colors_attr.reset}"
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
    print(colors_attr.reset)


def clear():
    print(colors_attr.clear)
