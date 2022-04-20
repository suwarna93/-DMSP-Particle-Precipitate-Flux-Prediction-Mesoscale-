import pandas as pd
import numpy as np
import streamlit as st
from keras.models import load_model
from tensorflow import keras
import tensorflow as tf

from prediction import get_prediction


st.set_page_config(page_title='DMSP Particle Precipitate Flux Prediction', page_icon="🌎", layout="wide", initial_sidebar_state='expanded')

NN_model = load_model('keras_NN_model.h5')

# creating option list for dropdown menu

features = ['SC_AACGM_LAT', 'ID_SC', 'cos_SC_AACGM_LTIME', 'F107', 'vsw_6hr']

st.markdown("<h1 style='text-align: center;'>DMSP Particle Precipitate Flux Prediction 🌎 </h1>", unsafe_allow_html=True)


def main():
    with st.form('prediction_form'):

        st.header("Predict the input for following features:") 


        SC_AACGM_LAT= st.selectbox( 'SC_AACGM_LAT:', [46.96, 49.61, 52.27, 54.92, 57.58, 62.92, 65.71, 68.39])
        
        
        ID_SC  = st.slider('ID_SC', 0.0, 18.0, value=0.0, format="%f")
        cos_SC_AACGM_LTIME = st.slider('os_SC_AACGM_LTIME', 0.0, 0.087845, value=0.0, format="%f")
        F107  = st.slider('F107', 0.0, 68.9, value=0.0, format="%f")
        vsw_6hr  = st.slider('vsw_6hr', 0.0, 337.700, value=0.0, format="%f")
        
        submit = st.form_submit_button("Predict")

    if submit:

        data= np.array([SC_AACGM_LAT, ID_SC, cos_SC_AACGM_LTIME, F107, vsw_6hr]).reshape(1, -1)
        
        pred = get_prediction(data=data, NN_model=NN_model)

       

        
        
        
        st.write(f"The predicted ELE_TOTAL_ENERGY_FLUX is:  {pred}")



if __name__ == '__main__':
    main()
