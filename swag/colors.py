COLORS = {}
# Reset
COLORS["reset"] = "\033[0m"  # Text Reset
# Clear
COLORS["clear"] = "\x1b[2J\x1b[H"
# Regular Colors
COLORS["black"] = "\033[0;30m"  # Black
COLORS["red"] = "\033[0;31m"  # Red
COLORS["green"] = "\033[0;32m"  # Green
COLORS["yellow"] = "\033[0;33m"  # Yellow
COLORS["blue"] = "\033[0;34m"  # Blue
COLORS["purple"] = "\033[0;35m"  # Purple
COLORS["cyan"] = "\033[0;36m"  # Cyan
COLORS["white"] = "\033[0;37m"  # White

# Bold
COLORS["bold_black"] = "\033[1;30m"  # Black
COLORS["bold_red"] = "\033[1;31m"  # Red
COLORS["bold_green"] = "\033[1;32m"  # Green
COLORS["bold_yellow"] = "\033[1;33m"  # Yellow
COLORS["bold_blue"] = "\033[1;34m"  # Blue
COLORS["bold_purple"] = "\033[1;35m"  # Purple
COLORS["bold_cyan"] = "\033[1;36m"  # Cyan
COLORS["bold_white"] = "\033[1;37m"  # White

# Underline
COLORS["underline_black"] = "\033[4;30m"  # Black
COLORS["underline_red"] = "\033[4;31m"  # Red
COLORS["underline_green"] = "\033[4;32m"  # Green
COLORS["underline_yellow"] = "\033[4;33m"  # Yellow
COLORS["underline_blue"] = "\033[4;34m"  # Blue
COLORS["underline_purple"] = "\033[4;35m"  # Purple
COLORS["underline_cyan"] = "\033[4;36m"  # Cyan
COLORS["underline_white"] = "\033[4;37m"  # White

# Background
COLORS["background_black"] = "\033[40m"  # Black
COLORS["background_red"] = "\033[41m"  # Red
COLORS["background_green"] = "\033[42m"  # Green
COLORS["background_yellow"] = "\033[43m"  # Yellow
COLORS["background_blue"] = "\033[44m"  # Blue
COLORS["background_purple"] = "\033[45m"  # Purple
COLORS["background_cyan"] = "\033[46m"  # Cyan
COLORS["background_white"] = "\033[47m"  # White

# High Intensity
COLORS["intense_black"] = "\033[0;90m"  # Black
COLORS["intense_red"] = "\033[0;91m"  # Red
COLORS["intense_green"] = "\033[0;92m"  # Green
COLORS["intense_yellow"] = "\033[0;93m"  # Yellow
COLORS["intense_blue"] = "\033[0;94m"  # Blue
COLORS["intense_purple"] = "\033[0;95m"  # Purple
COLORS["intense_cyan"] = "\033[0;96m"  # Cyan
COLORS["intense_white"] = "\033[0;97m"  # White

# Bold High Intensity
COLORS["intense_bold_black"] = "\033[1;90m"  # Black
COLORS["intense_bold_red"] = "\033[1;91m"  # Red
COLORS["intense_bold_green"] = "\033[1;92m"  # Green
COLORS["intense_bold_yellow"] = "\033[1;93m"  # Yellow
COLORS["intense_bold_blue"] = "\033[1;94m"  # Blue
COLORS["intense_bold_purple"] = "\033[1;95m"  # Purple
COLORS["intense_bold_cyan"] = "\033[1;96m"  # Cyan
COLORS["intense_bold_white"] = "\033[1;97m"  # White

# High Intensity backgrounds
COLORS["intense_background_black"] = "\033[0;100m"  # Black
COLORS["intense_background_red"] = "\033[0;101m"  # Red
COLORS["intense_background_green"] = "\033[0;102m"  # Green
COLORS["intense_background_yellow"] = "\033[0;103m"  # Yellow
COLORS["intense_background_blue"] = "\033[0;104m"  # Blue
COLORS["intense_background_purple"] = "\033[0;105m"  # Purple
COLORS["intense_background_cyan"] = "\033[0;106m"  # Cyan
COLORS["intense_background_white"] = "\033[0;107m"  # White

class AttrDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"No such attribute: {name}")

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError:
            raise AttributeError(f"No such attribute: {name}")

colors_attr = AttrDict(COLORS)