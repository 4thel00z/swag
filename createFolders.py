# -*- coding: UTF-8 -*-
import os

import os
import stat

import colors

st = os.stat('prettyEcho.py')
os.chmod('prettyEcho.py', st.st_mode | stat.S_IEXEC)

directory = os.path.expanduser("~")+"/.colors"
colorDictionary=colors.colorDictionary


for i, key in enumerate(colorDictionary):
    print key
    file = open( directory+"/"+key+".txt" , "w" )
    file.write( colorDictionary[key] )
    file.close()


if not os.path.exists(directory):
    os.makedirs(directory)
