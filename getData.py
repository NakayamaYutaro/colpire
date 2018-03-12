import pandas as pd

class getTable:
	def __init__(self) :
		print("Print data of") 
	def getAll(self,f) :
		df = pd.read_csv(f,header=0)
		print(df)
			
