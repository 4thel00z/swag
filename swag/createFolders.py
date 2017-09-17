# -*- coding: UTF-8 -*-
import os

import colors
from __future__ import print_function


def install(dest="default"):
    if dest == "default":
        directory = os.path.expanduser("~") + "/.colors"
    else:
        directory = dest

    colorDictionary = colors.COLORS

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, key in enumerate(colorDictionary):
        print(
            colors.COLORS["reset"] + colors.COLORS[key] + "Installed " + directory + "/" + key + colors.COLORS["reset"])
        file = open(directory + "/" + key, "w")
        file.write(colorDictionary[key])
        file.close()
