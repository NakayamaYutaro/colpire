#-*-coding: utf-8 -*-
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import getCell
import getTime
import datetime
import matplotlib
#import Tkinter
import quandl
import tkinter
from datetime import datetime, date, time 
from datetime import timedelta
from pandas	import Series, DataFrame
from pandas_datareader.data import DataReader
from getTime import getYDH
from getCell import getTable
from getStockValue import getValue

argvs = sys.argv
argc = len(argvs)

quandl_data = 

if(argc!=2):
	print('Usage #python %s brand' % argvs[0])
	quit()

print('The latest brand of %s ...' % argvs[1])
brand = argvs[1]

now = datetime.now()
start =	datetime(now.year,now.month-1,now.day)
end	= datetime(now.year,now.month,now.day)

getStockValue_class = getValue()
getStockValue_class.read(brand,start,end)
getStockValue_class.plot(brand,start,end)

