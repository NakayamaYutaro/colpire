#-*-coding: utf-8 -*-
import sys
import pandas as pd
import getData
import getTime
from getTime import getYDH
from getData import getTable
argvs = sys.argv
argc = len(argvs)


if(argc!=2):
	print 'Usage #python %s filename' % argvs[0]
	quit()

print 'The content of %s ...n' % argvs[1]

f = open(argvs[1])

getYDH_class = getYDH()
getTable_class = getTable()
getTable_class.getAll(f)
