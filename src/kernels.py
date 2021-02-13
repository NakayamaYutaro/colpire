#-*- coding: utf-8 -*-
import sys
import numpy as np
from morphological_analysis import *

def preprocess(text)
  words = morphological_analysis_wakati(text)   
  word_to_id = {}
  id_to_word = {}
  for word in words:
    if word not in word_to_id:
      new_id = len(word_to_id)
      word_to_id[word] = new_id
      id_to_word[new_id] = word

  corpus = np.array([word_to_id[w] for w in words])  
  return corpus, word_to_id, id_to_word  

#共起行列の生成
def create_coll_matrix(corpus: list, vocab_size: int, window_size: int=1) -> list:
  corpus_size = len(corpus)
  coll_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32) 
  
  for idx, word_id in enumerate(corpus):
    for i in range(1, window_size + 1):
      left_idx = idx - i
      right_idx = idx + i
      
      if left_idx >= 0:
        left_word_id = corpus[left_idx]
        coll_matrix[word_id, left_word_id] += 1
        
      if right_idx < corpus_size:
        right_word_id = corpus[right_idx]
        coll_matrix[word_id, right_word_id] += 1
  
  return coll_matrix 

def most_similars(query, word_to_id, id_to_word, word_matrix, top=5):
  #類似単語の表示
  if query not in word_to_id:
    print('%s is not found' % query)
    return query
    
  print('\n[query]' + query)
  query_id = word_to_id[query]
  query_vec = word_matrix[query]
  
  vocab_size = len(id_to_word)
  similarlity = np.zeros()
  for i in range(vocab_size):
    similarity[i] = cos_similarlity(word_matrix[i], query_vec)

  count = 0
 
  for i in (-1 * similarity)argsort():
    if id_to_word[i] == query:
      continue
    print('%s %s' % (id_to_word[i], word[i], similarity[i]))

    count += 1
    if count >= top:
      return 

def ppmi(C, verbose=False, eps=1e-8):
  M = np.zeros_like(C, dtype=np.float32)
  N = np.sum(C)
  S = np.sum(C, axis=0)
  total = C.shape[0] * C.shae[1]
  cnt = 0

  for i in range(C.shape[0]):
    for j in range(C.shape[1]):
      pmi = np.log2(C[i,j] * N / (S[j]*S[i]) + eps)
      M[i, j] = max(0, pmi)
      
      if verbose:
        cnt += 1
        if cnt % (total//100) == 0:
          print('%.1f%% done' % (100*cnt/total))
  return M

#特異値分解
def svd(text: str):
  corpus, word_to_id, id_to_word = preprocess(text)
  vocab_size = len(id_to_word)
  C = create_co_matrix(corpus, vocab_size, window_size=1)
  W = ppmi(C)
  U, S, V = np.linalg.svd(W)
  return U, S, V
