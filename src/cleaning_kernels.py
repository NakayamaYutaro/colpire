#-*- coding: utf-8 -*-
import re
import sys
from bs4 import BeautifulSoup

#２次元リストチェック
def check_2dlist(conversion_table: list) -> bool:
  return len(conversion_table) > 1 and isinstance(conversion_table[0], list)
 
#２次元辞書チェック
def check_2ddict(conversion_table: dict) -> bool:
  return len(conversion_table) > 1 and isinstance(conversion_table[0], dict) 

#単一文字に対しての変換処理
def convert_single_char(string: str, char1: str, char2: str) -> str:
  return string.translate(str.maketrans({char1, char2}))

#複数の単一文字に対しての変換処理
def convert_single_chars(string: str, conversion_table: dict) -> str:
  return string.translate(str.maketras(conversion_table))

#文字列に対しての変換処理
def convert_string(string: str, char1: str, chara2: str) -> str:
  return string.replace(char1,char2)

#複数の文字列に対しての変換処理
def convert_string(strings: list, conversion_table: list): -> list:
  for i in range(len(conversion_table[0])):
    string = string.replace(conversoin_table[0][i], conversion_table[1][i])
  return string

# neologdnを用いた文章の正規化処理
# 同一文字が連続で出現していた場合、[repeat=6]などの引数で繰り返し回数の指定し除去可能
# https://github.com/ikegami-yukino/neologdn/blob/master/test_neologdn.py
# neologdn.normalize(string, repeat=1)

# 自作正規化処理（
#   1.urlの除去,
#   2.スペースの除去,
#   3.小文字への統一,
#   4.半角を全角に変換,
#   5.数字を0に変換 
#   6.英文などの日本語以外の自然言語の除去
#   7.()【】,（）【】内の文字列の除去
#   8.タイトルの除去【例: 2. ４.】
#   9.図、グラフのキャプション除去
#   10.グラフ内文字列の除去
#   11.注釈の除去
#   12.参考文献の除去【例：1), 】
#   13.数式などの形式言語の除去
#   etc. 一文区切りの文書分割
#）
def original_normalize(string: str) -> str:
  conversion_table = [
    "(http|https)://([-\w]+\.)+[-\w]+(/[-\w./?%&=]*)?",
    " {1,}",
    "　{1,}",
    "[0-9０-９]",
    "([a-zA-Z0-9_]*( )?[a-zA-Z0-9])*(.).",
    "^(【|()\w(】|))$",
    "[0-9０-９](.).",
    "^(fig.|図.|表.)\w(.)$"
  ]
  for regex in conversion_table: 
    string = re.sub(r"%s" % regex, "", string)
  return string







 
