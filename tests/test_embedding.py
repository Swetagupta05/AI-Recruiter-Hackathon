from embedding_model import create_embedding

text = """
Python Developer
Machine Learning
Embeddings
Vector Database
"""

embedding = create_embedding(text)

print("Embedding Length:", len(embedding))
print()
print("First 10 values:")
print(embedding[:10])