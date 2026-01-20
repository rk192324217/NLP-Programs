import  spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is located in California")

for ent in doc.ents:
    print(ent.text, ent.label_)


nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is located in California")

for ent in doc.ents:
    print(ent.text, ent.label_)
