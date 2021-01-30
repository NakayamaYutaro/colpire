import MeCab

mecab_ipadic_neologd_path = ""

def morpholigical_analysis_mecab(sentence: str, dic_path: str) -> list:
  mt = MeCab.Tagger(mecab_ipadic_neologd_path)
  return mt.parse(sentence)

def clean_mecab_sentence(sentence: str):
  word_list = []
  for l in seentence.split("\n")
    block = l.split("\t")
    word_list.append(block)
  return word_list  
