import numpy as np
import pandas as pd
import pandas_datareader.data as web

class getValue:
	def read(self,brand,d1,d2) :	
		f = web.DataReader(brand,'morningstar',d1,d2)
		print(f.head(10))	
