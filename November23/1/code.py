import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

# Sample word embeddings (replace with your own)
word_vectors = {
    'king': [0.1, 0.2],
    'queen': [0.2, 0.3],
    'man': [0.4, 0.1],
    'woman': [0.5, 0.2],
    'apple': [0.3, 0.5],
}

# Create a list of words and their corresponding word vectors
words = list(word_vectors.keys())
vectors = [word_vectors[word] for word in words]

# Apply t-SNE for dimensionality reduction to 2D
tsne = TSNE(n_components=2, random_state=0)
vectors_2d = tsne.fit_transform(vectors)

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], marker='o', color='b', label='Word Embeddings')

# Annotate points with words
for i, word in enumerate(words):
    plt.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]))

plt.title('Word Embeddings Visualization')
plt.legend(loc='upper right')
plt.show()

