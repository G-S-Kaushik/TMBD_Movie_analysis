import streamlit as st
import pickle
import pandas as pd

movie_dict= pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

def recommand(movie):
    movie_index=movies[movies.title_x==movie].index[0] #finding index of movie
    distances=simalarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] #sorting top 5 movie with holding the index value 
    
    recommanded_movies=[]
    for i in movie_list: #removing the movie in side tuple holding index value
        recommanded_movies.append(movies.iloc[i[0]].title_x)
    return recommanded_movies

simalarity= pickle.load(open('simalarity.pkl','rb'))

st.title('Movie Recommender System')

option = st.selectbox(
'Recommanded Movies',
movies['title_x'].values
)

if st.button('Recommand'):
    recommendation=recommand(option)
    for i in recommendation:
        st.write(i)

