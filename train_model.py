import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("data/movies.csv")

# Keep required columns
movies = movies[["title", "genres"]]

# Convert genres into vectors
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["genres"])

# Calculate similarity
similarity = cosine_similarity(tfidf_matrix)

# Save files
pickle.dump(
    movies,
    open("movie_list.pkl", "wb")
)

pickle.dump(
    similarity,
    open("similarity.pkl", "wb")
)

print("Model Created Successfully")