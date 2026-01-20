import random

text = "NLP is interesting and NLP is useful"
words = text.split()

bigrams = {}
for i in range(len(words) - 1):
    bigrams.setdefault(words[i], []).append(words[i + 1])

current = random.choice(words)
sentence = [current]

for _ in range(5):
    current = random.choice(bigrams.get(current, words))
    sentence.append(current)

print("Generated Text:", " ".join(sentence))
