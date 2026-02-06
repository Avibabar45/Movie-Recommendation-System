import streamlit as st
import numpy as np
import pandas as pd
import pickle

def recommend(movie):
    movies_index = movies[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda X:X[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #fetch post from API
        
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
    

# Load the model

movies_list = pickle.load(open("movies_dict.pkl",'rb'))
#movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted ?',
     movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



