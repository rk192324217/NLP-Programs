import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

sentence = (
    "The cat on the roof, purring softly, "
    "which belongs to my neighbor, caught a mouse."
)

doc = nlp(sentence)

# --- Token-level information ---
for token in doc:
    print(
        f"Token: {token.text}, "
        f"Lemma: {token.lemma_}, "
        f"POS: {token.pos_}, "
        f"DEP: {token.dep_}"
    )

# --- Prepositional phrases (prep + pobj) ---
prepositional_phrases = []

for token in doc:
    if token.dep_ == "prep":
        phrase = " ".join([t.text for t in token.subtree])
        prepositional_phrases.append(phrase)

print("\nPrepositional phrases:", prepositional_phrases)

# --- Gerundive phrases (VERB + VBG) ---
gerundive_phrases = []

for token in doc:
    if token.tag_ == "VBG":
        phrase = " ".join([t.text for t in token.subtree])
        gerundive_phrases.append(phrase)

print("\nGerundive phrases:", gerundive_phrases)

# --- Infinitive clauses (to + VERB) ---
infinitive_clauses = []

for token in doc:
    if token.dep_ == "xcomp" and token.pos_ == "VERB":
        phrase = " ".join([t.text for t in token.subtree])
        infinitive_clauses.append(phrase)

print("\nNon-finite clauses (Infinitive):", infinitive_clauses)

# --- Relative clauses (relcl) ---
relative_clauses = []

for token in doc:
    if token.dep_ == "relcl":
        phrase = " ".join([t.text for t in token.subtree])
        relative_clauses.append(phrase)

print("\nRelative clauses:", relative_clauses)
