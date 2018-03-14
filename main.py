#-*-coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import getCell
import getTime
import datetime
import matplotlib
from datetime import datetime, date, time 
from datetime import timedelta
from pandas	import Series, DataFrame
from pandas_datareader.data import DataReader
from getTime import getYDH
from getCell import getTable
from getStockValue import getValue

argvs = sys.argv
argc = len(argvs)

if(argc!=2):
	print 'Usage #python %s brand' % argvs[0]
	quit()

print 'The latest brand of %s ...' % argvs[1]
brand = argvs[1]

now = datetime.now()
start =	datetime(now.year,now.month,now.day - 10)
end	= datetime(now.year,now.month,now.day)

#now_source = datetime.now().strftime('%Y-%m-%d')
#now = datetime.strptime(now_source,'%Y-%m-%d %H:%M:%S')
#start = now
#end_culc = now - timedelta(days=-5)
#end 	= end_culc.strftime('%Y-%m-%d')

getStockValue_class = getValue()
getStockValue_class.read(brand,start,end)
