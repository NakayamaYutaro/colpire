import MeCab

# MeCabのデフォルト設定辞書を確認 [sudo update-alternatives --config mecab-dictionary]

default_tagger_arg = "" 
default_dictionary_path = ""

def morphological_analysis_default(sentence: str, dic_path: str = None) -> list:
  mt = MeCab.Tagger(default_tagger_arg)
  return mt.parse(sentence)

def morphological_analysis_wakati(sentence: str, dic_path: str = None) -> list:
  mt = MeCab.Tagger("-Owakati")
  return mt.parse(sentence).split()

def clean_mecab_sentence(sentence: str):
  word_list = []
  for l in sentence.split("\n"):
    block = l.split("\t")
    word_list.append(block[0])
  return word_list  

def main(): 
  sentence = "今日は仕事をした。"
  analysed_sentence = morphological_analysis_default(sentence)
  print(analysed_sentence)
  print(clean_mecab_sentence(analysed_sentence))
