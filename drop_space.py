#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : drop_space.py
# Author        : Ljz
# Created       : 30th December 2016
# Last Modified : 30th December 2016
# Version       : 1.0
# 
# Description   : Through the current directory and subdirectory files, remove all blank lines in the file
#*****************************************************************************

import sys
import os
import re

#白名单
filter_file_type = [".py",".jpg",".JPG",".png",".PNG"]
filter_file_name = ["drop_space.py"]

def dropSpace(file_name):
    try:
        f=open(file_name)
        lines=f.readlines()
        f.close()
        f=open(file_name,"w+")
        for line in lines:
            if len(line.strip()) != 0:
                f.write(line)
        return True
    except BaseException,e:
        print e 
    finally:
        f.close()
        
        
for parent,dirnames,filenames in os.walk(sys.path[0]):
    for filename in filenames:
        if os.path.splitext(filename)[1] not in filter_file_type and filename not in filter_file_name:
            file_path=os.path.join(parent,filename)
            space_lenth=100-len(file_path)
            if dropSpace(file_path):
                print file_path," "*space_lenth,"%s"%("[ OK ]")
            else:
                print file_path," "*space_lenth,"%s"%("[ PR ]")




        