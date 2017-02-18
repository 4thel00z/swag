# -*- coding: UTF-8 -*-
import os

import os
import stat

st = os.stat('prettyEcho.py')
os.chmod('prettyEcho.py', st.st_mode | stat.S_IEXEC)

directory = os.path.expanduser("~")+"/.colors"
colorDictionary={}
# Reset
colorDictionary["reset"]="\033[0m"       # Text Reset

# Regular Colors
colorDictionary["black"]="\033[0;30m"        # Black
colorDictionary["red"]="\033[0;31m"          # Red
colorDictionary["green"]="\033[0;32m"        # Green
colorDictionary["yellow"]="\033[0;33m"       # Yellow
colorDictionary["blue"]="\033[0;34m"         # Blue
colorDictionary["purple"]="\033[0;35m"       # Purple
colorDictionary["cyan"]="\033[0;36m"         # Cyan
colorDictionary["white"]="\033[0;37m"        # White

# Bold
colorDictionary["boldBlack"]="\033[1;30m"       # Black
colorDictionary["boldRed"]="\033[1;31m"         # Red
colorDictionary["boldGreen"]="\033[1;32m"       # Green
colorDictionary["boldYellow"]="\033[1;33m"      # Yellow
colorDictionary["boldBlue"]="\033[1;34m"        # Blue
colorDictionary["boldPurple"]="\033[1;35m"      # Purple
colorDictionary["boldCyan"]="\033[1;36m"        # Cyan
colorDictionary["boldWhite"]="\033[1;37m"       # White

# Underline
colorDictionary["underlineBlack"]="\033[4;30m"       # Black
colorDictionary["underlineRed"]="\033[4;31m"         # Red
colorDictionary["underlineGreen"]="\033[4;32m"       # Green
colorDictionary["underlineYellow"]="\033[4;33m"      # Yellow
colorDictionary["underlineBlue"]="\033[4;34m"        # Blue
colorDictionary["underlinePurple"]="\033[4;35m"      # Purple
colorDictionary["underlineCyan"]="\033[4;36m"        # Cyan
colorDictionary["underlineWhite"]="\033[4;37m"       # White

# Background
colorDictionary["backgroundBlack"]="\033[40m"       # Black
colorDictionary["backgroundRed"]="\033[41m"         # Red
colorDictionary["backgroundGreen"]="\033[42m"       # Green
colorDictionary["backgroundYellow"]="\033[43m"      # Yellow
colorDictionary["backgroundBlue"]="\033[44m"        # Blue
colorDictionary["backgroundPurple"]="\033[45m"      # Purple
colorDictionary["backgroundCyan"]="\033[46m"        # Cyan
colorDictionary["backgroundWhite"]="\033[47m"       # White

# High Intensity
colorDictionary["intenseBlack"]="\033[0;90m"       # Black
colorDictionary["intenseRed"]="\033[0;91m"         # Red
colorDictionary["intenseGreen"]="\033[0;92m"       # Green
colorDictionary["intenseYellow"]="\033[0;93m"      # Yellow
colorDictionary["intenseBlue"]="\033[0;94m"        # Blue
colorDictionary["intensePurple"]="\033[0;95m"      # Purple
colorDictionary["intenseCyan"]="\033[0;96m"        # Cyan
colorDictionary["intenseWhite"]="\033[0;97m"       # White

# Bold High Intensity
colorDictionary["intenseBoldBlack"]="\033[1;90m"      # Black
colorDictionary["intenseBoldRed"]="\033[1;91m"        # Red
colorDictionary["intenseBoldGreen"]="\033[1;92m"      # Green
colorDictionary["intenseBoldYellow"]="\033[1;93m"     # Yellow
colorDictionary["intenseBoldBlue"]="\033[1;94m"       # Blue
colorDictionary["intenseBoldPurple"]="\033[1;95m"     # Purple
colorDictionary["intenseBoldCyan"]="\033[1;96m"       # Cyan
colorDictionary["intenseBoldWhite"]="\033[1;97m"      # White

# High Intensity backgrounds
colorDictionary["intenseBackgroundBlack"]="\033[0;100m"   # Black
colorDictionary["intenseBackgroundRed"]="\033[0;101m"     # Red
colorDictionary["intenseBackgroundGreen"]="\033[0;102m"   # Green
colorDictionary["intenseBackgroundYellow"]="\033[0;103m"  # Yellow
colorDictionary["intenseBackgroundBlue"]="\033[0;104m"    # Blue
colorDictionary["intenseBackgroundPurple"]="\033[0;105m"  # Purple
colorDictionary["intenseBackgroundCyan"]="\033[0;106m"    # Cyan
colorDictionary["intenseBackgroundWhite"]="\033[0;107m"   # White


for i, key in enumerate(colorDictionary):
    print key
    file = open( directory+"/"+key+".txt" , "w" )
    file.write( colorDictionary[key] )
    file.close()


if not os.path.exists(directory):
    os.makedirs(directory)
