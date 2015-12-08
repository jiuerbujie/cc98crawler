#encoding = utf-8
import sys
import ConfigParser
from paramParser import *
from cc98GetLinks import *
def cc98crawler(configFile):
    params = paramParser(configFile)
    targets = cc98GetLinks(params)
    saveData(targets, params)
    return

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        cc98crawler('config.ini')
    else:
        cc98crawler(sys.argv[1])
