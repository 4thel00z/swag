# -*- coding: UTF-8 -*-
import os

from swag.colors import COLORS


def install(dest=None):
    directory = dest
    if not dest:
        directory = os.environ.get("HOME", os.path.expanduser("~")) + "/.colors"

    c = COLORS

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, key in enumerate(c):
        print(c["reset"] + c[key] + "Installed " + directory + "/" + key + c["reset"])
        with open(directory + "/" + key, "w") as file:
            file.write(c[key])
