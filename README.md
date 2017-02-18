# Swag

Swag up your shell output with escape code magic!

## Usage

Run set permission via: 

`python setPermission.py`

or alternatively set permissions via chmod:

`sudo chmod +x swag.py`

Use the prettyEcho command, directly or symlink it via:

`ln -s $(pwd)/swag.py /usr/local/bin/swag`

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
                        seBackground
```

## Raw Usage

### Installation
Run the createFolder.py script via:

`python createFolder.py`

This will install all the escape codes to the ~/.colors folder.

Now you can use the colors directly from the console via:

`echo $(cat ~/.colors/blue.txt) This will be blue`
