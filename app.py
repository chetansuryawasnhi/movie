import streamlit as st
import pickle
import json
import requests


sim=pickle.load(open('similarity.pkl',"rb"))
movies=pickle.load(open("movies.pkl",'rb'))


def fetch_post(id):
    img=requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=4f0a2c1d7e5f8b9a6c0e4d1f3a2b8c5b&language=en-US')
    print(img)
    st.image()
    return id
def recommend(node):
    ind=movies[movies['title']==node].index[0]
    arr=[]
    dis=list(enumerate(sim[ind]))
    dis.sort(key=lambda x:x[1],reverse=True)
    top_5= dis[1:6]
    for i in dis[1:6]:
        # print(i[0])
        arr.append((movies.iloc[i[0]].title,movies.iloc[i[0]].id))
    return arr
st.title("Movie Recommendation System")
option=st.selectbox('Select The Movie',movies['title'].values)
if st.button('Recommend'):
    # st.write("your movie :- ", option)
    st.write('Recommended Movies')
    recomendeds=recommend(option)
    # print(recomendeds)
    for i in recomendeds:
        st.write(i[0])
    pass