import nltk
from nltk import CFG, ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = ChartParser(grammar)
for tree in parser.parse("John runs".split()):
    tree.pretty_print()
