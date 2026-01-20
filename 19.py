import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet

# Download required resources
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

# Input sentence and ambiguous word
sentence = "He deposited money in the bank"
word = "bank"

# Apply Lesk algorithm
sense = lesk(sentence.split(), word)

# Display result
if sense:
    print("Word:", word)
    print("Sense:", sense.name())
    print("Definition:", sense.definition())
    print("Examples:", sense.examples())
else:
    print("No sense found")
