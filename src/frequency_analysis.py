import MeCab
import collections
import seaborn as sns
import matplotlib.pyplot as plt

test_path = "data/bluesky_restart"
test_word_class_list = ["名詞","動詞","形容詞"]
word_class_list = ["名詞","動詞","形容詞","形容動詞","副詞","連体詞","接続詞","感動詞","助動詞","助詞"]

#最頻出トップ20ワード
def most_words(text_path: str = test_path) -> str:
  #ファイルの書き込み用の指定
  f = open(text_path)
  text = f.read() 
  #分類用ワードリスト作成
  words = []
  #文章の分かち書き
  mt = MeCab.Tagger()
  node = mt.parse(text)
  #print(node) 
  #品詞の分類
  while node:
    word_class = node.feature.split(",")[4]
    print("品詞名: " + word_class)
    if word_class in test_word_class_list:
      origin = node.feature.split(",")[0]
      words.append(origin)
    node = node.next
  #品詞別の集計  
  col = collections.Counter(words)
  most_words = col.most_common(20)
  print(most_words)
   
  #グラフへの出力
  sns.set(context="talk")
  fig = plt.subplots(figsize=(8, 8))
  sns.countplot(y=words, order=[i[0] for i in col.most_common(20)])

  #ファイルオープンの解放
  f.close()
  
  return most_words 

def main():
  print(most_words(test_path))

main()
