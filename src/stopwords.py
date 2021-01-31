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

def main():
  test_sentence = "これはテスト用の文章です。"
  test_dic = create_dictionary(test_sentence)
  print(test_dic)
  print(remove_stopwords(test_dic,stopwords_list))
