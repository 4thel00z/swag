# -*- coding: UTF-8 -*-
import os

from swag import colors


def install(dest=None):
    if not dest:
        directory = os.path.expanduser("~") + "/.colors"
    else:
        directory = dest

    c = colors.COLORS

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, key in enumerate(c):
        print(c["reset"] + c[key] + "Installed " + directory + "/" + key + c["reset"])
        with open(directory + "/" + key, "w") as file:
            file.write(c[key])
