#-*- coding: utf-8 -*-
import morphological_analysis
from urllib.request import *
from gensim.corpora import Dictionary

stopwords = []
stopwords_default_url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"

def get_sample_stopwords(url: str = stopwords_default_url) -> list:
  slothlib_path = url;
  with urlopen(slothlib_path) as res:
    body = res.read().decode()
  slothlib_stopwords = [line.strip() for line in body.split()]
  slothlib_stopwords = [stopwords for stopwords in slothlib_stopwords if not stopwords==u'']
  stopwords = list(set(slothlib_stopwords))
  return stopwords

def create_dictionary(texts) -> dict:
  dictionary = corpora.Dictionary(texts)
  return dictionary

def remove_stopwords(word_list: list, stopwords: list) -> list:
  #イミュータブルの場合はdeepcopyを使用
  copy_list = word_list.copy()
  return [word for word in copy_list if word not in stopwords]
