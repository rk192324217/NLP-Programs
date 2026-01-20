from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "Natural language processing is useful",
    "Information retrieval uses TF IDF",
    "TF IDF is important in NLP",
    "Machine learning helps NLP"
]

# Input query
query = "TF IDF in NLP"

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Transform query
query_vector = vectorizer.transform([query])

# Compute cosine similarity
similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

# Rank documents
ranked_docs = sorted(
    enumerate(similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("Document Ranking:\n")
for idx, score in ranked_docs:
    print(f"Document {idx + 1} (Score: {score:.4f}): {documents[idx]}")
