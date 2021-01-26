# stockSurvey
Stock price analysis system by YutaroNakayama
This repository is under development.
---

## Detail
Yahoo!, Google Options, Google Quotes and EDGAR have been immediately deprecated due to large changes in their API.
And it cannot create system on print Japanse Brand. 
So we create system through New York Stock Exchange(NYSE) and morningstar API.
<https://pandas-datareader.readthedocs.io/en/latest/>

## Environment
Detail and How to create virtual environment on Python.
<https://qiita.com/H-A-L/items/5d5a2ef73be8d140bdf3>

$ sudo apt-get install python python3 python 3.6  
$ sudo apt-get install virtualenv
$ sudo apt-get install tk-dev

After change directory to stockTrade/bin

$ pip install scikit-learn  
$ pip install quandl   
$ pip install pandas  
$ pip install `pandas_datareader`  
$ pip install matplotlib inline  


## Directory structure
bin           --- Python,pip,etc executable file.
include       --- C header files
lib/python2.7 --- Python interpreter
local           
data/img      --- Save image files
   -getData.py
   -getTime.py 				
	 -getStockValue.py	
   -main.py
   -pip-selfcheck.json
   -sample.csv

## Execution method
First, after change directory to stockTrade/bin/ and do the following command.  
**$ source activate**

Second, after change directory to stockTrade/ and do the following command.  
**$ python main.py <Stock_Brand>**  

![実行結果](https://github.com/NakayamaYutaro/stockTrade/blob/master/data/img/sampleTM_exec.png "実行結果")


