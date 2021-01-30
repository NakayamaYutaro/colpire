#-*- coding: utf-8 -*-
import re
import sys
from bs4 import BeautifulSoup

#２次元配列チェック
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
