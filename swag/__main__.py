#! env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

from typing import Optional

import typer

import swag
from swag import colors
from swag.colors import COLORS

TYPE_MODIFIERS = ['underline', 'background', 'bold', 'intense', 'intenseBold', 'intenseBackground']
COLOR_MODIFIERS = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']

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
        reset: bool = True,
        color: str = "white",
        modifier: str = "normal",
):
    swag.swag(color, text, modifier=modifier, continuous=not reset)


@app.command(
    name="list",
)
def list_handler():
    c = COLORS
    for i, key in enumerate(c):
        print(colors.reset + c[key] + key + colors.reset)


if __name__ == '__main__':
    app()
