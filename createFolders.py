# -*- coding: UTF-8 -*-
import os
import setPermission

import colors


directory = os.path.expanduser("~")+"/.colors"
colorDictionary=colors.colorDictionary


for i, key in enumerate(colorDictionary):
    print key
    file = open( directory+"/"+key+".txt" , "w" )
    file.write( colorDictionary[key] )
    file.close()


if not os.path.exists(directory):
    os.makedirs(directory)
