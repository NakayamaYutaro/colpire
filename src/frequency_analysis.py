import MeCab
import collections
import seaborn as sns
import matplotlib.pyplot as plt

test_path = "data/bluesky_restart"
word_class_list = ["名詞","動詞","形容詞","形容動詞","副詞","連体詞","接続詞","感動詞","助動詞","助詞"]

#最頻出トップ20ワード
def most_words(text_path: str = test_path, word_num: int = 20) -> str:
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
  #品詞別の集計  
  col = collections.Counter(words)
  most_words = col.most_common(word_num)

  #ファイルオープンの解放
  f.close()
  
  return most_words 

def main():
  print(most_words(test_path,100))

