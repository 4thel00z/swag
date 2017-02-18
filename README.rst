Swag
====

Color your shell output with escape code magic. ## Installation

``pip install swag``

Usage
-----

::

    usage: swag [-h] [-c COLOR] [-t TYPE] text

    positional arguments:
      text                  the text to prettyEcho

    optional arguments:
      -h, --help            show this help message and exit
      -c COLOR, --color COLOR
                            default = white - which color to format the text in :
                            black|red|green|yellow|blue|purple|cyan|white
      -t TYPE, --type TYPE  default = normal - format the string with either: norm
                            al|underline|background|bold|intense|intenseBold|inten
                            seBackground

Raw Usage
---------

Use from code
~~~~~~~~~~~~~

::

    from swag import colors
    print colors.COLORS["red"], "This will be red"

Installation
~~~~~~~~~~~~

::

    from swag import createFolders

This will install all the escape codes to the ~/.colors folder.

Now you can use the colors directly from the console via:

``echo $(cat ~/.colors/blue.txt) This will be blue``
