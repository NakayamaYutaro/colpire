#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

class getValue:
	def read(self,brand,d1,d2) :	
		f = web.DataReader(brand,'morningstar',d1,d2)
		f['Close'].plot(title=brand,grid=True)
		plt.savefig('data/img/' + brand + '.png')
		f.to_csv('data/csv/' + brand + '.csv')
		print(brand + '.csvを出力しました.')
		print(f.head(10))	

	def plot(self,brand,d1,d2) :
		f = web.DataReader(brand,'morningstar',d1,d2)
		f.plot()
		plt.show()
