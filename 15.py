import nltk
from nltk import PCFG, ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'dogs' [0.5] | 'cats' [0.5]
VP -> 'bark' [1.0]
""")

parser = ViterbiParser(grammar)
for tree in parser.parse("dogs bark".split()):
    print(tree)
