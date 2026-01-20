sentence = [("They", "NN"), ("are", "NN"), ("playing", "NN")]

for i in range(len(sentence)):
    word, tag = sentence[i]
    if word.endswith("ing"):
        sentence[i] = (word, "VBG")
    elif word == "are":
        sentence[i] = (word, "VBP")

print(sentence)
