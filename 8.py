word_probs = {
    "I": "PRP",
    "love": "VBP",
    "NLP": "NN",
    "learning": "VBG"
}

sentence = "I love NLP learning".split()

for word in sentence:
    print(word, "->", word_probs.get(word, "NN"))
