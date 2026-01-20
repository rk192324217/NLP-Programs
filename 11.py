grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["dog"], ["cat"]],
    "V": [["chased"]]
}

def parse(symbol, words):
    if not words:
        return False
    if symbol not in grammar:
        return words[0] == symbol
    for rule in grammar[symbol]:
        w = words[:]
        valid = True
        for sym in rule:
            if not parse(sym, w):
                valid = False
                break
            w.pop(0)
        if valid:
            return True
    return False

sentence = "the dog chased the cat".split()
print("Accepted" if parse("NP", sentence) else "Rejected")
