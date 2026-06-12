import streamlit as st
import pickle

# Load files
movies = pickle.load(
    open("movie_list.pkl", "rb")
)

similarity = pickle.load(
    open("similarity.pkl", "rb")
)

# Recommendation function
def recommend(movie):

    movie_index = movies[
        movies["title"] == movie
    ].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations


# UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommend(
        selected_movie
    )

    st.subheader(
        "Recommended Movies"
    )

    for movie in recommendations:
        st.write(movie)