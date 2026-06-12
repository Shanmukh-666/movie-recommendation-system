# Movie Recommendation System

## Overview

A Movie Recommendation System built using Machine Learning and Streamlit.

This project implements a content-based movie recommendation system that suggests similar movies based on genre information. The recommendation engine uses TF-IDF vectorization and cosine similarity to identify movies with similar characteristics and provides recommendations through an interactive Streamlit web application.

---

## Features

- Select a movie
- Get Top 5 recommendations
- Content-based filtering
- Interactive Streamlit interface

---

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- Streamlit

---

## Machine Learning Techniques

- TF-IDF Vectorization
- Cosine Similarity

---

## Dataset

MovieLens Small Dataset

https://grouplens.org/datasets/movielens/

---

## Project Structure

movie-recommendation-system/

app.py

train_model.py

movie_list.pkl

similarity.pkl

README.md

data/movies.csv

---

## Run Project

Install dependencies:

```bash
uv sync
```

Create model:

```bash
uv run python train_model.py
```

Run app:

```bash
uv run streamlit run app.py
```

---

## Future Improvements

- Movie Posters
- Search Feature
- User Ratings
- Collaborative Filtering