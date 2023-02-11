
import pandas as pd
import numpy as np

import pickle
import streamlit as st
st.title("Crop Prediction on Soil factors")
st.write('Get most suitable crop on basis of Temperature, Humidity, pH, Rainfall and Soil factors - N, P, K for your farm with respective prices.')
st.write()

cropPrice = {'amaranthus': 3500,
 'banana - green': 700,
 'bhindi': 3300,
 'bitter gourd': 4000,
 'black pepper': 29250,
 'bottle gourd': 885,
 'brinjal': 2250,
 'cabbage': 500,
 'carrot': 700,
 'cauliflower': 650,
 'cluster beans': 3400,
 'coconut': 950,
 'colacasia': 1550,
 'onion': 1300,
 'potato': 550,
 'tomato': 1300,
 'bengal gram': 5075,
 'jowar': 1400,
 'paddy': 1770,
 'lentil': 5450,
 'rice': 3500,
 'cucumbar': 5400,
 'field pea': 1360,
 'french beans': 4000,
 'green chilli': 7600,
 'knool khol': 1000,
 'pumpkin': 900,
 'raddish': 300,
 'black gram': 5900,
 'green gram': 7000,
 'jute': 4500,
 'maida atta': 2370,
 'mustard': 4100,
 'wheat atta': 3500,
 'garlic': 1350,
 'masur dal': 6300,
 'ridgeguard': 3300,
 'arecanut': 1500,
 'arhar': 6400,
 'maize': 1930,
 'dry chillies': 4000,
 'groundnut': 4900,
 'capsicum': 1720,
 'guar': 4050,
 'lemon': 1350,
 'bajra': 1400,
 'castor seed': 4870,
 'coriander': 120,
 'cowpea': 4550,
 'drumstick': 2000,
 'elephant yam': 1300,
 'ginger': 8000,
 'indian beans': 4000,
 'methi': 1000,
 'onion green': 1200,
 'peas cod': 900,
 'pegeon pea': 3000,
 'sponge gourd': 1950,
 'surat beans': 2500,
 'sweet potato': 1145,
 'tinda': 1550,
 'guar seed': 3875,
 'cotton': 5200,
 'wheat': 2100,
 'gram raw': 1000,
 'little gourd': 2000,
 'round gourd': 1400,
 'leafy vegetable': 320,
 'mint': 6,
 'papaya': 1400,
 'spinach': 650,
 'pointed gourd': 5250,
 'banana': 750,
 'ber': 1150,
 'grapes': 1800,
 'kinnow': 750,
 'peas wet': 1150,
 'apple': 3050,
 'orange': 1800,
 'pomegranate': 3500,
 'chikoos': 2300,
 'mashrooms': 20000,
 'mousambi': 2610,
 'pineapple': 4000,
 'guava': 4800,
 'turnip': 400,
 'squash': 1400,
 'beans': 2800,
 'beetroot': 1400,
 'chilly capsicum': 3500,
 'green avare': 2900,
 'seemebadnekai': 1500,
 'snakeguard': 1700,
 'suvarna gadde': 2500,
 'water melon': 3000,
 'copra': 9300,
 'amphophalus': 2000,
 'ashgourd': 850,
 'coconut oil': 18150,
 'rubber': 12350,
 'cashewnuts': 10500,
 'pepper garbled': 27750,
 'coconut seed': 1950,
 'long melon': 2700,
 'tapioca': 220,
 'turmeric': 7325,
 'mango': 4500,
 'amla': 3800,
 'duster beans': 3600,
 'soyabean': 3615,
 'linseed': 3475,
 'niger seed': 4150,
 'green gram dal': 3650,
 'lime': 1000,
 'karbuja': 1700,
 'pear': 8000,
 'rajgir': 3,
 'sweet pumpkin': 1500,
 'tender coconut': 400,
 'bengal gram dal': 5430,
 'betal leaves': 26500,
 'broken rice': 1200,
 'gur': 2600,
 'sugar': 3440,
 'sesamum': 8600,
 'moath dal': 7400,
 'corriander seed': 4152,
 'ground nut seed': 3500,
 'taramira': 3256,
 'tobacco': 1900,
 'tamarind fruit': 10100,
 'kulthi': 2630,
 'ragi': 2579,
 't.v. cumbu': 1969,
 'gingelly oil': 10649,
 'kodo millet': 1989,
 'hybrid cumbu': 1825,
 'karamani': 6263,
 'thinai': 1205,
 'wood': 240,
 'barley': 1700,
 'fish': 4300,
 'green peas': 800,
 'arhar dal': 6000,
 'black gram dal': 6430,
 'mustard oil': 10530,
 'ghee': 29000,
 'white pumpkin': 310,
 'peas': 4600,
 'plum': 570}


# possibleCrops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
#        'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
#        'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
#        'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']


def allZero(arr):
    arr = arr.reshape(-1,)
    for ele in arr:
        if ele != 0: return False
    return True


import requests
import config

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    
    base_url = "http://api.openweathermap.org/data/2.5/weather/?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None

# import model:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
model = pickle.load(open('RandomForest.pkl','rb'))


with st.sidebar:
    st.image("image.jpeg")
    st.title('Crop Recommender System')
    


N = st.number_input('Nitrogen: ')
P = st.number_input('Phosphorus: ')
K = st.number_input('Potassium: ')

# allCity = ['Andaman and Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
#        'Assam', 'Bihar', 'Chandigarh', 'Chattisgarh',
#        'Dadra and Nagar Haveli', 'Goa', 'Gujarat', 'Haryana',
#        'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka',
#        'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
#        'Mizoram', 'Nagaland', 'Odisha', 'Pondicherry', 'Punjab',
#        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
#        'Uttar Pradesh', 'Uttrakhand', 'West Bengal']

# city = st.selectbox(
#      'Select location: ',
#      allCity)

# temp, hum = weather_fetch(city)
temp = st.number_input('Temperature: ')
hum = st.number_input('Humidity: ')

ph = st.number_input('pH: ')
rain = st.number_input('Rainfall: ')

inputData = np.array([[N, P, K, temp, hum, ph, rain]])

if st.button('Predict Crop'):
    
    if allZero(inputData):
        st.text("Kindly give some non zero parameters.")
    else:
        outputCrop = model.predict(inputData)
        print(outputCrop)
        st.title(f"The suitable crop is: {outputCrop[0]}")

        if outputCrop[0] in cropPrice.keys(): 
            st.title(f"Price: {cropPrice[outputCrop[0]]}")

