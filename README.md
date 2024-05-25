# Swag

Color your shell output with escape code magic.

[![Demo](https://asciinema.org/a/fciEE57CeLkKBQl5uoU51rgPR.svg)](https://asciinema.org/a/fciEE57CeLkKBQl5uoU51rgPR)

## Installation

`pip install swag`

## Usage

```
Usage: swag [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  install
  list
  print
```

## CLI Usage

### Print to the cli

You can print colored from the shell as follows:

```shell
swag print --color yellow --modifier intense_bold "This text will be intense_bold and yellow :-)"
```

The possible modifiers are:

* underline
* background
* bold
* intense
* intense_bold
* intense_background

### Installation to a folder

From the commandline do:

```shell
swag install --dest <path/to/folder> # default is ~/.colors
```

This will install all the escape codes to the ~/.colors or <path/to/folder> folder.

Now you can use the colors directly from the console via:

`echo $(cat ~/.colors/blue) This will be blue`

### List all colors

Prints a list of colors (color coded).

```shell
swag list
```

## Use from code

### Print to the console

```python
from swag import red, green, reset, INTENSE

red("This will be red")
green("Blah", modifier=INTENSE)  # Prints an intense green
# Prints an intense green, to the end of the output, means if you use print after it will be green too:
green("This is green until the end", modifier=INTENSE, continuous=True)
print("This will still be green")
reset()  # From now on the default cli color will be used
```

### Use the colors in a string

```python
from swag import colors
print(f"{colors.red}This will be red{colors.reset}")
```

## License

This project is licensed under the GPL-3 license.
