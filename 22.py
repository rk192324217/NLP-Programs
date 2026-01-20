text = "John went to the store. He bought milk."

words = text.split()
last_noun = None

for word in words:
    if word.istitle():
        last_noun = word
    if word.lower() in ["he", "she"]:
        print(f"{word} refers to {last_noun}")
