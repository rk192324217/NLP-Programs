import nltk
from nltk import CFG
from nltk.parse import ChartParser
from nltk.parse.generate import generate
nltk.download('punkt')

# Define a simple CFG
grammar = CFG.fromstring("""
S  -> NP VP
NP -> Det N | Pronoun | NP PP
VP -> V NP | V 
PP -> P NP

Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'morning' | 'flight'
V -> 'chased' | 'saw' | 'took'
P -> 'on' | 'to'
Pronoun -> 'he' | 'she'
""")

# Create a parser
parser = ChartParser(grammar)

# Sentence to parse
sentence = "the cat chased a dog"

# Tokenize
tokens = sentence.split()

# Parse
print("Parse Trees:\n")
for tree in parser.parse(tokens):
    tree.pretty_print()
