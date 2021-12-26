#! env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

from typing import Optional

import typer

from swag import colors

TYPE_MODIFIERS = ['underline', 'background', 'bold', 'intense', 'intenseBold', 'intenseBackground']
COLOR_MODIFIERS = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']


def get_key(color, type):
    if type == "normal":
        if color.lower() in COLOR_MODIFIERS:
            return color
        else:
            return "white"

    elif type.lower() in TYPE_MODIFIERS:
        if color.lower() in COLOR_MODIFIERS:
            return type.lower() + color.lower().capitalize()
        else:
            return type.lower() + "White"
    else:
        return "white"


app = typer.Typer(
    name="swag",
)


@app.command(
    name="install",
)
def install_handler(dest: Optional[str] = None):
    from swag.install import install
    install(dest)


@app.command(
    name="print",
)
def print_handler(
        text: str,
        color: str = "white",
        type: str = "normal",
):
    key = get_key(color, type)
    c = colors.COLORS
    print(f'{c["reset"]}{c[key]}{text}{c["reset"]}')


@app.command(
    name="list",
)
def list_handler():
    c = colors.COLORS
    for i, key in enumerate(c):
        print(colors.COLORS["reset"] + c[key] + key + c["reset"])


if __name__ == '__main__':
    app()
