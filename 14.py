import nltk
from nltk import CFG, ChartParser

grammar = CFG.fromstring("""
S -> NP_s VP_s
NP_s -> 'He'
VP_s -> 'runs'
""")

parser = ChartParser(grammar)

sentence = "He runs".split()
print("Valid" if list(parser.parse(sentence)) else "Invalid")
