#-*- coding: utf-8 -*-
import numpy as np

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

