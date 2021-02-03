#-*- coding: utf-8 -*-
from stopwords import *

import MeCab
import collections
import matplotlib.pyplot as plt
import numpy as np

test_path = "data/bluesky_restart"
word_class_list = ["名詞","動詞","形容詞","形容動詞","副詞","連体詞","接続詞","感動詞","助動詞","助詞"]

#最頻出トップ20ワード
def most_words(text_path: str = test_path, word_num: int = 20, stop_words_flag: bool = 1) -> str:
  #ファイルの書き込み用の指定
  f = open(text_path)
  text = f.read() 
  #分類用ワードリスト作成
  words = []
  #文章の分かち書き
  mt = MeCab.Tagger()
  node = mt.parseToNode(text)
   
  #品詞の分類
  while node:
    #単語要素が入っているか判断 
    word_class = node.feature.split(",")[0]
    #品詞リストにword_classの品詞が含まれていた場合の処理 
    if word_class in word_class_list:
      if len(node.feature.split(",")) < 8:
        pass
      else:
        origin = node.feature.split(",")[8]
      words.append(origin)
    node = node.next
  
  #最頻出ワードからのstopwordsの削除
  if stop_words_flag == 1:
    words = remove_stopwords(words, get_sample_stopwords())
  else:
    pass
   
  #品詞別の集計（この時点で出現回数順に並び替えられている）
  col = collections.Counter(words)
  #出現回数が多い要素順にCounterオブジェクトを並び替え
  most_words = col.most_common(word_num)
  #ファイルオープンの解放
  f.close()
  #棒グラフの出力例
  left = np.array([words for words,num in most_words])  
  height = np.array([num for words,num in most_words])  
  plt.rcParams["figure.figsize"] = (8, 8)
  plt.bar(left, height, align='center')
  plt.xticks(rotation=-90)
  plt.title("最頻出ワードTOP20")
  plt.xlabel("単語リスト") 
  plt.ylabel("単語頻出回数")
  plt.grid(True)
  plt.show()
  return most_words 

def main():
  print(most_words(test_path,100,0))
  print(most_words(test_path,20,1))
main()

