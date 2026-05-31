from database import save_prediction
import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
feature_names = joblib.load('feature_names.pkl')
feature_means = joblib.load('feature_means.pkl')

st.title('House Price Prediction')
st.write('Enter the details of the house to get an estimated sale price.')

st.sidebar.header('Enter House Details')

OverallQual = st.sidebar.slider('Overall Quality (1-10)', 1, 10, 5)
GrLivArea = st.sidebar.number_input('Above Ground Living Area (sq ft)', 300, 4000, 1500)
GarageCars = st.sidebar.slider('Garage Capacity (cars)', 0, 4, 2)
TotalBsmtSF = st.sidebar.number_input('Total Basement Area (sq ft)', 0, 3000, 800)
FullBath = st.sidebar.slider('Full Bathrooms', 0, 4, 2)
YearBuilt = st.sidebar.number_input('Year Built', 1872, 2010, 1990)
YearRemodAdd = st.sidebar.number_input('Year Remodeled', 1950, 2010, 1990)
TotRmsAbvGrd = st.sidebar.slider('Total Rooms Above Ground', 1, 14, 6)
Fireplaces = st.sidebar.slider('Number of Fireplaces', 0, 3, 1)

input_data = pd.DataFrame([feature_means], columns=feature_names)

input_data['OverallQual'] = OverallQual
input_data['GrLivArea'] = GrLivArea
input_data['GarageCars'] = GarageCars
input_data['TotalBsmtSF'] = TotalBsmtSF
input_data['FullBath'] = FullBath
input_data['YearBuilt'] = YearBuilt
input_data['YearRemodAdd'] = YearRemodAdd
input_data['TotRmsAbvGrd'] = TotRmsAbvGrd
input_data['Fireplaces'] = Fireplaces

input_scaled = scaler.transform(input_data)

# Predict button
if st.sidebar.button('Predict Price'):
    prediction = model.predict(input_scaled)
    predicted_price = np.expm1(prediction[0])
    
    st.success(f'Estimated House Price: ${predicted_price:,.0f}')
    
    st.write('---')
    st.subheader('Input Summary')
    summary = pd.DataFrame({
        'Feature': ['Overall Quality', 'Living Area (sq ft)', 'Garage Capacity', 
                    'Basement Area (sq ft)', 'Full Bathrooms', 'Year Built', 
                    'Year Remodeled', 'Total Rooms', 'Fireplaces'],
        'Value': [OverallQual, GrLivArea, GarageCars, TotalBsmtSF, 
                  FullBath, YearBuilt, YearRemodAdd, TotRmsAbvGrd, Fireplaces]
    })
    st.table(summary)

    inputs = {
        'OverallQual': OverallQual,
        'GrLivArea': GrLivArea,
        'GarageCars': GarageCars,
        'TotalBsmtSF': TotalBsmtSF,
        'FullBath': FullBath,
        'YearBuilt': YearBuilt,
        'YearRemodAdd': YearRemodAdd,
        'TotRmsAbvGrd': TotRmsAbvGrd,
        'Fireplaces': Fireplaces
    }
    try:
        save_prediction(inputs, predicted_price)
        st.info('Prediction saved to database')
    except Exception as e:
        st.error(f'Database error: {e}')
    
    
    

