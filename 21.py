import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The intelligent student solved the complex problem"

tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

grammar = r"NP: {<DT>?<JJ>*<NN>}"
parser = RegexpParser(grammar)
tree = parser.parse(tags)

for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        print("Noun Phrase:", " ".join(word for word, tag in subtree.leaves()))
