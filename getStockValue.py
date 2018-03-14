import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
class getValue:
	def read(self,brand,d1,d2) :	
		f = web.DataReader(brand,'morningstar',d1,d2)
		f['Close'].plot(title=brand,grid=True)
		plt.savefig('data/' + brand + '.png')
		print(f.head(10))	
	
