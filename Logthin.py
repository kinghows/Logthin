#!/usr/local/bin/python
# coding: utf-8

# Logthin V1.0.0 for python3
# Log slimming tool
# Copyright (C) 2017-2017 Kinghow - Kinghow@hotmail.com
# Git repository available at https://github.com/kinghows/Logthin

import getopt
import sys
import configparser
import os
import re

def get_thinlogName(filename):
    (filepath,tempfilename) = os.path.split(filename)
    (shotname,extension) = os.path.splitext(tempfilename)
    thinlogname = filepath+shotname+'_thin'+extension
    return thinlogname

if __name__=="__main__":
    config_file="Logthin.ini"
    key = ""
    including =[]
    excluding =[]

    opts, args = getopt.getopt(sys.argv[1:], "l:k:i:e:")
    for o,v in opts:
        if o == "-l":
            log_file = v
        elif o == "-k":
            key = v
        elif o == "-i":
            including = v.split(",")
        elif o == "-e":
            excluding = v.split(",")

    if len(including)==0 and len(excluding)==0 and os.path.exists(config_file):
        v =''
        config = configparser.ConfigParser()
        #config.read(config_file,encoding="utf-8-sig")
        config.read(config_file)
        try:
            v=config.get("set","including")
        except:
            pass
        else:
            if v != '':
                including = config.get("set","including").split(",")
        try:
            v=config.get("set","excluding")
        except:
            pass
        else:
            if v != '':
                excluding = config.get("set","excluding").split(",")
        

    if os.path.exists(log_file):
        srcFile = open(log_file, 'r+')
        dstFile = open(get_thinlogName(log_file), 'w+')
        lines = srcFile.readlines()

        for line in lines:
            if key in line:
                if including :
                    for includ in including:
                        if includ in line:
                            if excluding :
                                for exclud in excluding:
                                    if exclud not in line:
                                        dstFile.write(line)
                            else:
                                dstFile.write(line)
                else:
                    if excluding :
                        for exclud in excluding:
                            if exclud not in line:
                                dstFile.write(line)
                    else:
                        dstFile.write(line)

        srcFile.close()
        dstFile.close()
    else:
        print('Please check '+log_file+' exists!')

