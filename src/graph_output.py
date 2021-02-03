#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def words_bar_graph(words_list: list, title: str, xlabel: str, ylabel: str): 
  left = np.array([words for words,num in words_list])  
  height = np.array([num for words,num in words_list])  
  plt.rcParams["figure.figsize"] = (8, 8)
  plt.bar(left, height, align='center')
  plt.xticks(rotation=-90)
  plt.title(title)
  plt.xlabel(xlabel) 
  plt.ylabel(ylabel)
  plt.grid(True)
  plt.show()
