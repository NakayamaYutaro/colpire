#-*- coding: utf-8 -*-
import morphological_analysis
from gensim.corpora import Dictionary

def create_dictionary(texts):
  dictionary = corpora.Dictionary(texts)
  return dictionary

def remove_stopwords(word_list: list, stopwords: list):
  removed_list = word_list.copy()
  for ele in stopwords:
    try:
      lst.remove(element)
    except ValueError:
      pass
  return removed_list
