import nltk
from nltk import CFG, EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'dog' | 'cat'
V -> 'chased'
""")

parser = EarleyChartParser(grammar)
sentence = "the dog chased the cat".split()

for tree in parser.parse(sentence):
    print(tree)
