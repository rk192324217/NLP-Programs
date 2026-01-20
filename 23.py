from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "Natural Language Processing is useful",
    "NLP helps machines understand language"
]

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(sentences)

coherence_score = cosine_similarity(vectors[0], vectors[1])[0][0]
print("Coherence Score:", coherence_score)
