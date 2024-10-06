import pandas as pd
import streamlit as st
import numpy as np
import joblib

model=joblib.load('C:/Users/MOHAMMED RIFAIZ/OneDrive/Desktop/Codsoft/movie_rating_model.pkl')

def predict_rating(year,duration,genre,votes,director,actor1,actor2,actor3):
    input_data=pd.DataFrame({
        'Year':[year],
        'Duration':[duration],
        'Votes':[votes],
        'Genre':[genre],
        'Director':[director],
        'Actor 1':[actor1],
        'Actor 2':[actor2],
        'Actor 3':[actor3]
})
    
    input_data['Year']=pd.to_numeric(input_data['Year'],errors='coerce')
    input_data['Duration'] = pd.to_numeric(input_data['Duration'].str.replace(r'\D', '', regex=True), errors='coerce')

    predicted_rating=model.predict(input_data)
    return predicted_rating[0]

st.title('Movie Rating Prediction App')
st.write('Enter the details of the movie to predict its rating:')

year=st.number_input('Year',min_value=1900,max_value=2024)
duration=st.text_input('Duration (in minutes)')
genre=st.selectbox('Genre',['Action','Comedy','Drama','Horror','Romance','Sci-Fi'])
votes=st.number_input('Votes',min_value=0)
director=st.text_input('Director')
actor1=st.text_input('Actor 1')
actor2=st.text_input('Actor 2')
actor3=st.text_input('Actor 3')

if st.button('Predict Rating'):
    rating=predict_rating(year,duration,genre,votes,director,actor1,actor2,actor3)
    st.success(f'The predicted rating for the movie is:{rating:.2f}')