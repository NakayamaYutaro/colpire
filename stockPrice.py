from selenium import webdriver
import pandas as pd
import numpy as pd
from matplotlib import pyplot as plt


#browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path="/home/kao/stockTrade/chromedriver")
columnNames = []
ETFComparisionTable= []

for num in range(0,48):
    browser.get("https://kabuoji3.com/stock/")
    stockSearch=browser.find_element_by_class_name("form_inputs")
    stockSearchFrom=stockSearch.find_element_by_class_name("from_txt")
    stockSearchFrom.send_keys("ETF")
    btnClick=browser.find_element_by_class_name("btn_submit")
    btnClick.click()

    #choose a stock out of list
    stockClick=blowser.find_elements_by_class_name("clickable")
    stock[num].find_element_by_class_name("btn_submit")
    btnClick.click()
    
    stockTable = blowser.find_element_by_class_name("table_wrap")
    stockLine = stockTable.find_element_by_class_name("table_wrap")
    stockLine = stockTable.find_elements_by_tag_name("tr")

    #price scraping with calclation
    if len(stockLine)==302:
        ETFComparisons=[]
        for i in range(2,152):
            stockETFPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
            stockETFPriceBefore=stockLine[i].find_elements_by_tag_name("td")
            ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPrieBefore[6].text)
            ETFComparisons.append(ETFComparison)
        stockETFPriceAfter=stockLine[151].find_elememt_by_tag_name("td")
        stockETFPriceBefore=stockLine[153].find_elements_by_tag_name("td")
        ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPrieBefore[6].text)

    for i in range(154,302):
        stockETFPriceAfter=stockLine[i-1].find_elememt_by_tag_name("td")
        stockETFPriceAfter=stockLine[i].find_elememt_by_tag_name("td")
        ETFComparison=float(stockETFPriceAfter[6].text)-float(stockETFPrieBefore[6].text)
        ETFComparisons.append(ETFComparison)
    ETFComparisonsTable.append(ETFComparisons)
       
    stockTitleBox = blowser.find_element_by_class_name("base_box_ttl")
    stockTitle = stockTitleBox.find_element_by_class_name("jp").text
    columnNames.append(stockTitle)

ETFTable = pd.DataFrame(ETFComparisonsTable)
ETFTable = ETFTable.T
ETFTable.columns = columnNames

ETF.head()
