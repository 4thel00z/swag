#! env python
# -*- coding: UTF-8 -*-

import os

import argparse

import colors

directory = os.path.expanduser("~") + "/.colors"

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--color", default="white",
                    help="default = white - which color to format the text in : black|red|green|yellow|blue|purple|cyan|white")

parser.add_argument("-t", "--type", default="normal",
                    help="default = normal - format the string with either: normal|underline|background|bold|intense|intenseBold|intenseBackground")

parser.add_argument("text", type=str, help="the text to prettyEcho")




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


def main():

    args = parser.parse_args()
    color = args.color
    type = args.type
    text = args.text

    key = getKey(color, type)
    colorMod = colors.COLORS[key]

    print colorMod + text


if __name__ == '__main__':
    main()