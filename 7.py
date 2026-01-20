import nltk
from nltk import word_tokenize, pos_tag

sentence = "Natural Language Processing is very useful"
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

print(tags)
