#-*- coding: utf-8 -*-
from stopwords import *
from graph_output import words_bar_graph

import sys
import MeCab
import collections

test_path = "data/bluesky_restart"
word_class_list = ["名詞","動詞","形容詞","形容動詞","副詞","連体詞","接続詞","感動詞","助動詞","助詞"]

word_num_err_msg_upper= "引数[word_num]の値の上限が超えていたので異常終了しました。"
word_num_err_msg_lower = "引数[word_num]の値の下限が超えていたので異常終了しました。"

#最頻出トップワード
def most_words(text_path: str = test_path, word_num: int = 10, stop_words_flag: bool = 1) -> str:
  #word_numの上限30を超えていないかのチェック
  if word_num > 30:
    sys.exit(word_num_err_msg_upper)
  elif word_num < 1:
    sys.exit(word_num_err_msg_lower)
  else:
    pass
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
  words_bar_graph(most_words, "最頻出ワードTOP20","単語","頻出回数") 
    
  return most_words 

def main():
  print(most_words(test_path,10,1))
main()

