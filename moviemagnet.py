import streamlit as st
import pickle
import pandas as pd
import requests
import time


similarity = pickle.load(open('movies_similarity.pkl','rb'))
movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
movies_titles = movies['title'].values

def fetech_poster(id):

    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNTQ4NDU3ZjZmMWI3Y2FjYTg3NmRkYTM0NGY0NWE0NyIsInN1YiI6IjY1YjY1N2M3NThlZmQzMDEyZmNhN2I2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DHqdygJUszRQb-zRrZ9b803oA2R1MCp9ZnrrquYgYPs"
    }

    response = requests.get(url, headers=headers)

    json_data =response.json()
    return 'https://image.tmdb.org/t/p/w500/'+json_data['poster_path']






st.title('MovieMagnet ',anchor=None)
option = st.selectbox(
    'Select your favourite movie',
    movies_titles)


def movies_recommander(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list=sorted(enumerate(distance),reverse=True ,key= lambda x:x[1])[1:6]
    movies_names=[]
    movies_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id	
        movies_names.append(movies.iloc[i[0]].title)
        movies_poster.append(fetech_poster(movie_id))
    return movies_names,movies_poster


if st.button('Recommand Movies'):
    name,poster=movies_recommander(option)

    progress_text = "Searching in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
   
    st.header('Must watch these movies', divider='blue')
    col1, col2, col3 ,col4,col5= st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])


