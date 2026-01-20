import nltk
from nltk.corpus import wordnet as wn

# Download WordNet if not already downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')

word = "bank"

# Retrieve synsets
synsets = wn.synsets(word)

print(f"Synsets for the word '{word}':\n")

for syn in synsets:
    print("Synset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print("-" * 50)
