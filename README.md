PrettyEcho

Color your shell output with escape code magic:

Run the createFolder.py script via.

`python createFolder.py`

Then use the prettyEcho command, directly or symlink it via:

`ln -s $(pwd)/prettyEcho.py /usr/local/bin/prettyEcho`

```
usage: prettyEcho.py [-h] [-c COLOR] [-t TYPE] text

positional arguments:
  text                  the text to prettyEcho

optional arguments:
  -h, --help            show this help message and exit
  -c COLOR, --color COLOR
                        default = white - which color to format the text in :
                        black|red|green|yellow|blue|purple|cyan|white
  -t TYPE, --type TYPE  default = normal - format the string with either: norm
                        al|underline|background|bold|intense|intenseBold|inten
                        seBackground```
