import re

words = "running played cats quickly".split()

for word in words:
    if re.match(r'.*ing$', word):
        tag = 'VBG'
    elif re.match(r'.*ed$', word):
        tag = 'VBD'
    elif re.match(r'.*s$', word):
        tag = 'NNS'
    else:
        tag = 'NN'
    print(word, "->", tag)
