#! env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import os

import argparse

import colors

directory = os.path.expanduser("~") + "/.colors"

parser = argparse.ArgumentParser()

subParsers = parser.add_subparsers(help='[command] help')

installParser = subParsers.add_parser("install",
                                      help="install the colors to the folder of choice")

installParser.add_argument_group()
installParser.add_argument("-d", "--dest", default="default",
                           help="default = ~/.colors - install the color escape sequences to the specified destination")

installParser.add_argument("-l", "--list", default=False, action="store_true")

printParser = subParsers.add_parser("print",
                                    help="prints the text with the specified color and type to the console")

printParser.add_argument_group()
printParser.add_argument("-c", "--color", default="white",
                         help="default = white - which color to format the text in : black|red|green|yellow|blue|purple|cyan|white")

printParser.add_argument("-t", "--type", default="normal",
                         help="default = normal - format the string with either: normal|underline|background|bold|intense|intenseBold|intenseBackground")

printParser.add_argument("text", type=str, default="", help="the text to prettyEcho")


def getKey(color, type):
    if type is "normal":
        if color.lower() in "black|red|green|yellow|blue|purple|cyan|white".split("|"):
            return color
        else:
            return "white"

    elif type.lower() in "underline|background|bold|intense|intenseBold|intenseBackground":
        if color.lower() in "black|red|green|yellow|blue|purple|cyan|white".split("|"):
            return type.lower() + color.lower().capitalize()
        else:
            return type.lower() + "White"
    else:
        return "white"


def install(dest):
    import createFolders
    createFolders.install(dest)


def list():
    colorDictionary = colors.COLORS
    for i, key in enumerate(colorDictionary):
        print (colors.COLORS["reset"] + colors.COLORS[key] + key + colors.COLORS["reset"])


def main():
    args = parser.parse_args()

    if "dest" in args:
        dest = args.dest
        if not args.list:
            install(dest)
        else:
            list()
    else:
        color = args.color
        type = args.type
        text = args.text
        key = getKey(color, type)
        colorMod = colors.COLORS[key]
        print(colorMod + text)


if __name__ == '__main__':
    main()
