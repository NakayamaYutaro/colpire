# -*- codig:utf-8 -*-
import datetime

class getYDH :
	def time(self,mode=0) :
		if mode == 1 :
			print(datetime.date.today())
		elif mode==2 :
			print(datetime.datetime.today())
		else : 
			print("none")
