
import numpy as np

import pickle
import streamlit as st
st.title("Crop Prediction on Soil factors")
st.write('Get most suitable crop on basis of Temperature, Humidity, pH, Rainfall and Soil factors - N, P, K for your farm with respective prices.')

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


# # possibleCrops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
# #        'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
# #        'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
# #        'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']


def allZero(arr):
    arr = arr.reshape(-1,)
    for ele in arr:
        if ele != 0: return False
    return True


# import requests
# import config
# import json



# import model:
import numpy as np
import pickle
import streamlit as st
model = pickle.load(open('RandomForest.pkl','rb'))


with st.sidebar:
    st.image("image.jpeg")
    st.title('Crop Recommender System')
    st.markdown('Fill your lovely farm with most suitable crops depending upon your location, season and within your price range :)')
    


N = st.number_input('Nitrogen: ')
P = st.number_input('Phosphorus: ')
K = st.number_input('Potassium: ')

temp = st.number_input('Temperature: ')
hum = st.number_input('Humidity: ')

ph = st.number_input('pH: ')
rain = st.number_input('Rainfall: ')

inputData = np.array([[N, P, K, temp, hum, ph, rain]])
if ph<3.5 or ph>10.3:
    st.text("Kindly Provide suitable ph range")
if st.button('Predict Crop', key=1):
    
    if allZero(inputData):
        st.text("Kindly give some non zero parameters.")
    else:
        outputCrop = model.predict(inputData)
        print(outputCrop)
        st.title(f"The suitable crop is: {outputCrop[0]}")

        if outputCrop[0] in cropPrice.keys(): 
            st.title(f"Price: {cropPrice[outputCrop[0]]}")



# model 2:
st.title("Crop Prediction on basis of Location, Season and Price")
st.write('Get most suitable crop on basis of your location and eason within your own price range for your lovely farm.')

seasonMap = {'Autumn': 0, 'Kharif': 1, 'Rabi': 2, 'Summer': 3, 'Whole Year': 4, 'Winter': 5}

stateMap = {'Andaman and Nicobar Islands': 0, 'Andhra Pradesh': 1, 'Arunachal Pradesh': 2, 'Assam': 3, 'Bihar': 4, 'Chandigarh': 5, 'Chhattisgarh': 6, 'Dadra and Nagar Haveli': 7, 'Goa': 8, 'Gujarat': 9, 'Haryana': 10, 'Himachal Pradesh': 11, 'Jammu and Kashmir ': 12, 'Jharkhand': 13, 'Karnataka': 14, 'Kerala': 15, 'Madhya Pradesh': 16, 'Maharashtra': 17, 'Manipur': 18, 'Meghalaya': 19, 'Mizoram': 20, 'Nagaland': 21, 'Odisha': 22, 'Puducherry': 23, 'Punjab': 24, 'Rajasthan': 25, 'Sikkim': 26, 'Tamil Nadu': 27, 'Telangana ': 28, 'Tripura': 29, 'Uttar Pradesh': 30, 'Uttarakhand': 31, 'West Bengal': 32}

distMap = {'24 PARAGANAS NORTH': 0, '24 PARAGANAS SOUTH': 1, 'ADILABAD': 2, 'AGAR MALWA': 3, 'AGRA': 4, 'AHMADABAD': 5, 'AHMEDNAGAR': 6, 'AIZAWL': 7, 'AJMER': 8, 'AKOLA': 9, 'ALAPPUZHA': 10, 'ALIGARH': 11, 'ALIRAJPUR': 12, 'ALLAHABAD': 13, 'ALMORA': 14, 'ALWAR': 15, 'AMBALA': 16, 'AMBEDKAR NAGAR': 17, 'AMETHI': 18, 'AMRAVATI': 19, 'AMRELI': 20, 'AMRITSAR': 21, 'AMROHA': 22, 'ANAND': 23, 'ANANTAPUR': 24, 'ANANTNAG': 25, 'ANJAW': 26, 'ANUGUL': 27, 'ANUPPUR': 28, 'ARARIA': 29, 'ARIYALUR': 30, 'ARWAL': 31, 'ASHOKNAGAR': 32, 'AURAIYA': 33, 'AURANGABAD': 34, 'AZAMGARH': 35, 'BADGAM': 36, 'BAGALKOT': 37, 'BAGESHWAR': 38, 'BAGHPAT': 39, 'BAHRAICH': 40, 'BAKSA': 41, 'BALAGHAT': 42, 'BALANGIR': 43, 'BALESHWAR': 44, 'BALLIA': 45, 'BALOD': 46, 'BALODA BAZAR': 47, 'BALRAMPUR': 48, 'BANAS KANTHA': 49, 'BANDA': 50, 'BANDIPORA': 51, 'BANGALORE RURAL': 52, 'BANKA': 53, 'BANKURA': 54, 'BANSWARA': 55, 'BARABANKI': 56, 'BARAMULLA': 57, 'BARAN': 58, 'BARDHAMAN': 59, 'BAREILLY': 60, 'BARGARH': 61, 'BARMER': 62, 'BARNALA': 63, 'BARPETA': 64, 'BARWANI': 65, 'BASTAR': 66, 'BASTI': 67, 'BATHINDA': 68, 'BEED': 69, 'BEGUSARAI': 70, 'BELGAUM': 71, 'BELLARY': 72, 'BEMETARA': 73, 'BENGALURU URBAN': 74, 'BETUL': 75, 'BHADRAK': 76, 'BHAGALPUR': 77, 'BHANDARA': 78, 'BHARATPUR': 79, 'BHARUCH': 80, 'BHAVNAGAR': 81, 'BHILWARA': 82, 'BHIND': 83, 'BHIWANI': 84, 'BHOJPUR': 85, 'BHOPAL': 86, 'BIDAR': 87, 'BIJAPUR': 88, 'BIJNOR': 89, 'BIKANER': 90, 'BILASPUR': 91, 'BIRBHUM': 92, 'BISHNUPUR': 93, 'BOKARO': 94, 'BONGAIGAON': 95, 'BOUDH': 96, 'BUDAUN': 97, 'BULANDSHAHR': 98, 'BULDHANA': 99, 'BUNDI': 100, 'BURHANPUR': 101, 'BUXAR': 102, 'CACHAR': 103, 'CHAMARAJANAGAR': 104, 'CHAMBA': 105, 'CHAMOLI': 106, 'CHAMPAWAT': 107, 'CHAMPHAI': 108, 'CHANDAULI': 109, 'CHANDEL': 110, 'CHANDIGARH': 111, 'CHANDRAPUR': 112, 'CHANGLANG': 113, 'CHATRA': 114, 'CHHATARPUR': 115, 'CHHINDWARA': 116, 'CHIKBALLAPUR': 117, 'CHIKMAGALUR': 118, 'CHIRANG': 119, 'CHITRADURGA': 120, 'CHITRAKOOT': 121, 'CHITTOOR': 122, 'CHITTORGARH': 123, 'CHURACHANDPUR': 124, 'CHURU': 125, 'COIMBATORE': 126, 'COOCHBEHAR': 127, 'CUDDALORE': 128, 'CUTTACK': 129, 'DADRA AND NAGAR HAVELI': 130, 'DAKSHIN KANNAD': 131, 'DAMOH': 132, 'DANG': 133, 'DANTEWADA': 134, 'DARBHANGA': 135, 'DARJEELING': 136, 'DARRANG': 137, 'DATIA': 138, 'DAUSA': 139, 'DAVANGERE': 140, 'DEHRADUN': 141, 'DEOGARH': 142, 'DEOGHAR': 143, 'DEORIA': 144, 'DEWAS': 145, 'DHALAI': 146, 'DHAMTARI': 147, 'DHANBAD': 148, 'DHAR': 149, 'DHARMAPURI': 150, 'DHARWAD': 151, 'DHEMAJI': 152, 'DHENKANAL': 153, 'DHOLPUR': 154, 'DHUBRI': 155, 'DHULE': 156, 'DIBANG VALLEY': 157, 'DIBRUGARH': 158, 'DIMA HASAO': 159, 'DIMAPUR': 160, 'DINAJPUR DAKSHIN': 161, 'DINAJPUR UTTAR': 162, 'DINDIGUL': 163, 'DINDORI': 164, 'DODA': 165, 'DOHAD': 166, 'DUMKA': 167, 'DUNGARPUR': 168, 'DURG': 169, 'EAST DISTRICT': 170, 'EAST GARO HILLS': 171, 'EAST GODAVARI': 172, 'EAST JAINTIA HILLS': 173, 'EAST KAMENG': 174, 'EAST KHASI HILLS': 175, 'EAST SIANG': 176, 'EAST SINGHBUM': 177, 'ERNAKULAM': 178, 'ERODE': 179, 'ETAH': 180, 'ETAWAH': 181, 'FAIZABAD': 182, 'FARIDABAD': 183, 'FARIDKOT': 184, 'FARRUKHABAD': 185, 'FATEHABAD': 186, 'FATEHGARH SAHIB': 187, 'FATEHPUR': 188, 'FAZILKA': 189, 'FIROZABAD': 190, 'FIROZEPUR': 191, 'GADAG': 192, 'GADCHIROLI': 193, 'GAJAPATI': 194, 'GANDERBAL': 195, 'GANDHINAGAR': 196, 'GANGANAGAR': 197, 'GANJAM': 198, 'GARHWA': 199, 'GARIYABAND': 200, 'GAUTAM BUDDHA NAGAR': 201, 'GAYA': 202, 'GHAZIABAD': 203, 'GHAZIPUR': 204, 'GIRIDIH': 205, 'GOALPARA': 206, 'GODDA': 207, 'GOLAGHAT': 208, 'GOMATI': 209, 'GONDA': 210, 'GONDIA': 211, 'GOPALGANJ': 212, 'GORAKHPUR': 213, 'GULBARGA': 214, 'GUMLA': 215, 'GUNA': 216, 'GUNTUR': 217, 'GURDASPUR': 218, 'GURGAON': 219, 'GWALIOR': 220, 'HAILAKANDI': 221, 'HAMIRPUR': 222, 'HANUMANGARH': 223, 'HAPUR': 224, 'HARDA': 225, 'HARDOI': 226, 'HARIDWAR': 227, 'HASSAN': 228, 'HATHRAS': 229, 'HAVERI': 230, 'HAZARIBAGH': 231, 'HINGOLI': 232, 'HISAR': 233, 'HOOGHLY': 234, 'HOSHANGABAD': 235, 'HOSHIARPUR': 236, 'HOWRAH': 237, 'HYDERABAD': 238, 'IDUKKI': 239, 'IMPHAL EAST': 240, 'IMPHAL WEST': 241, 'INDORE': 242, 'JABALPUR': 243, 'JAGATSINGHAPUR': 244, 'JAIPUR': 245, 'JAISALMER': 246, 'JAJAPUR': 247, 'JALANDHAR': 248, 'JALAUN': 249, 'JALGAON': 250, 'JALNA': 251, 'JALORE': 252, 'JALPAIGURI': 253, 'JAMMU': 254, 'JAMNAGAR': 255, 'JAMTARA': 256, 'JAMUI': 257, 'JANJGIR-CHAMPA': 258, 'JASHPUR': 259, 'JAUNPUR': 260, 'JEHANABAD': 261, 'JHABUA': 262, 'JHAJJAR': 263, 'JHALAWAR': 264, 'JHANSI': 265, 'JHARSUGUDA': 266, 'JHUNJHUNU': 267, 'JIND': 268, 'JODHPUR': 269, 'JORHAT': 270, 'JUNAGADH': 271, 'KABIRDHAM': 272, 'KACHCHH': 273, 'KADAPA': 274, 'KAIMUR (BHABUA)': 275, 'KAITHAL': 276, 'KALAHANDI': 277, 'KAMRUP': 278, 'KAMRUP METRO': 279, 'KANCHIPURAM': 280, 'KANDHAMAL': 281, 'KANGRA': 282, 'KANKER': 283, 'KANNAUJ': 284, 'KANNIYAKUMARI': 285, 'KANNUR': 286, 'KANPUR DEHAT': 287, 'KANPUR NAGAR': 288, 'KAPURTHALA': 289, 'KARAIKAL': 290, 'KARAULI': 291, 'KARBI ANGLONG': 292, 'KARGIL': 293, 'KARIMGANJ': 294, 'KARIMNAGAR': 295, 'KARNAL': 296, 'KARUR': 297, 'KASARAGOD': 298, 'KASGANJ': 299, 'KATHUA': 300, 'KATIHAR': 301, 'KATNI': 302, 'KAUSHAMBI': 303, 'KENDRAPARA': 304, 'KENDUJHAR': 305, 'KHAGARIA': 306, 'KHAMMAM': 307, 'KHANDWA': 308, 'KHARGONE': 309, 'KHEDA': 310, 'KHERI': 311, 'KHORDHA': 312, 'KHOWAI': 313, 'KHUNTI': 314, 'KINNAUR': 315, 'KIPHIRE': 316, 'KISHANGANJ': 317, 'KISHTWAR': 318, 'KODAGU': 319, 'KODERMA': 320, 'KOHIMA': 321, 'KOKRAJHAR': 322, 'KOLAR': 323, 'KOLASIB': 324, 'KOLHAPUR': 325, 'KOLLAM': 326, 'KONDAGAON': 327, 'KOPPAL': 328, 'KORAPUT': 329, 'KORBA': 330, 'KOREA': 331, 'KOTA': 332, 'KOTTAYAM': 333, 'KOZHIKODE': 334, 'KRISHNA': 335, 'KRISHNAGIRI': 336, 'KULGAM': 337, 'KULLU': 338, 'KUPWARA': 339, 'KURNOOL': 340, 'KURUKSHETRA': 341, 'KURUNG KUMEY': 342, 'KUSHI NAGAR': 343, 'LAHUL AND SPITI': 344, 'LAKHIMPUR': 345, 'LAKHISARAI': 346, 'LALITPUR': 347, 'LATEHAR': 348, 'LATUR': 349, 'LAWNGTLAI': 350, 'LEH LADAKH': 351, 'LOHARDAGA': 352, 'LOHIT': 353, 'LONGDING': 354, 'LONGLENG': 355, 'LOWER DIBANG VALLEY': 356, 'LOWER SUBANSIRI': 357, 'LUCKNOW': 358, 'LUDHIANA': 359, 'LUNGLEI': 360, 'MADHEPURA': 361, 'MADHUBANI': 362, 'MADURAI': 363, 'MAHARAJGANJ': 364, 'MAHASAMUND': 365, 'MAHBUBNAGAR': 366, 'MAHE': 367, 'MAHENDRAGARH': 368, 'MAHESANA': 369, 'MAHOBA': 370, 'MAINPURI': 371, 'MALAPPURAM': 372, 'MALDAH': 373, 'MALKANGIRI': 374, 'MAMIT': 375, 'MANDI': 376, 'MANDLA': 377, 'MANDSAUR': 378, 'MANDYA': 379, 'MANSA': 380, 'MARIGAON': 381, 'MATHURA': 382, 'MAU': 383, 'MAYURBHANJ': 384, 'MEDAK': 385, 'MEDINIPUR EAST': 386, 'MEDINIPUR WEST': 387, 'MEERUT': 388, 'MEWAT': 389, 'MIRZAPUR': 390, 'MOGA': 391, 'MOKOKCHUNG': 392, 'MON': 393, 'MORADABAD': 394, 'MORENA': 395, 'MUKTSAR': 396, 'MUMBAI': 397, 'MUNGELI': 398, 'MUNGER': 399, 'MURSHIDABAD': 400, 'MUZAFFARNAGAR': 401, 'MUZAFFARPUR': 402, 'MYSORE': 403, 'NABARANGPUR': 404, 'NADIA': 405, 'NAGAON': 406, 'NAGAPATTINAM': 407, 'NAGAUR': 408, 'NAGPUR': 409, 'NAINITAL': 410, 'NALANDA': 411, 'NALBARI': 412, 'NALGONDA': 413, 'NAMAKKAL': 414, 'NAMSAI': 415, 'NANDED': 416, 'NANDURBAR': 417, 'NARAYANPUR': 418, 'NARMADA': 419, 'NARSINGHPUR': 420, 'NASHIK': 421, 'NAVSARI': 422, 'NAWADA': 423, 'NAWANSHAHR': 424, 'NAYAGARH': 425, 'NEEMUCH': 426, 'NICOBARS': 427, 'NIZAMABAD': 428, 'NORTH AND MIDDLE ANDAMAN': 429, 'NORTH DISTRICT': 430, 'NORTH GARO HILLS': 431, 'NORTH GOA': 432, 'NORTH TRIPURA': 433, 'NUAPADA': 434, 'OSMANABAD': 435, 'PAKUR': 436, 'PALAKKAD': 437, 'PALAMU': 438, 'PALGHAR': 439, 'PALI': 440, 'PALWAL': 441, 'PANCH MAHALS': 442, 'PANCHKULA': 443, 'PANIPAT': 444, 'PANNA': 445, 'PAPUM PARE': 446, 'PARBHANI': 447, 'PASHCHIM CHAMPARAN': 448, 'PATAN': 449, 'PATHANAMTHITTA': 450, 'PATHANKOT': 451, 'PATIALA': 452, 'PATNA': 453, 'PAURI GARHWAL': 454, 'PERAMBALUR': 455, 'PEREN': 456, 'PHEK': 457, 'PILIBHIT': 458, 'PITHORAGARH': 459, 'PONDICHERRY': 460, 'POONCH': 461, 'PORBANDAR': 462, 'PRAKASAM': 463, 'PRATAPGARH': 464, 'PUDUKKOTTAI': 465, 'PULWAMA': 466, 'PUNE': 467, 'PURBI CHAMPARAN': 468, 'PURI': 469, 'PURNIA': 470, 'PURULIA': 471, 'RAE BARELI': 472, 'RAICHUR': 473, 'RAIGAD': 474, 'RAIGARH': 475, 'RAIPUR': 476, 'RAISEN': 477, 'RAJAURI': 478, 'RAJGARH': 479, 'RAJKOT': 480, 'RAJNANDGAON': 481, 'RAJSAMAND': 482, 'RAMANAGARA': 483, 'RAMANATHAPURAM': 484, 'RAMBAN': 485, 'RAMGARH': 486, 'RAMPUR': 487, 'RANCHI': 488, 'RANGAREDDI': 489, 'RATLAM': 490, 'RATNAGIRI': 491, 'RAYAGADA': 492, 'REASI': 493, 'REWA': 494, 'REWARI': 495, 'RI BHOI': 496, 'ROHTAK': 497, 'ROHTAS': 498, 'RUDRA PRAYAG': 499, 'RUPNAGAR': 500, 'S.A.S NAGAR': 501, 'SABAR KANTHA': 502, 'SAGAR': 503, 'SAHARANPUR': 504, 'SAHARSA': 505, 'SAHEBGANJ': 506, 'SAIHA': 507, 'SALEM': 508, 'SAMASTIPUR': 509, 'SAMBA': 510, 'SAMBALPUR': 511, 'SAMBHAL': 512, 'SANGLI': 513, 'SANGRUR': 514, 'SANT KABEER NAGAR': 515, 'SANT RAVIDAS NAGAR': 516, 'SARAIKELA KHARSAWAN': 517, 'SARAN': 518, 'SATARA': 519, 'SATNA': 520, 'SAWAI MADHOPUR': 521, 'SEHORE': 522, 'SENAPATI': 523, 'SEONI': 524, 'SEPAHIJALA': 525, 'SERCHHIP': 526, 'SHAHDOL': 527, 'SHAHJAHANPUR': 528, 'SHAJAPUR': 529, 'SHAMLI': 530, 'SHEIKHPURA': 531, 'SHEOHAR': 532, 'SHEOPUR': 533, 'SHIMLA': 534, 'SHIMOGA': 535, 'SHIVPURI': 536, 'SHOPIAN': 537, 'SHRAVASTI': 538, 'SIDDHARTH NAGAR': 539, 'SIDHI': 540, 'SIKAR': 541, 'SIMDEGA': 542, 'SINDHUDURG': 543, 'SINGRAULI': 544, 'SIRMAUR': 545, 'SIROHI': 546, 'SIRSA': 547, 'SITAMARHI': 548, 'SITAPUR': 549, 'SIVAGANGA': 550, 'SIVASAGAR': 551, 'SIWAN': 552, 'SOLAN': 553, 'SOLAPUR': 554, 'SONBHADRA': 555, 'SONEPUR': 556, 'SONIPAT': 557, 'SONITPUR': 558, 'SOUTH ANDAMANS': 559, 'SOUTH DISTRICT': 560, 'SOUTH GARO HILLS': 561, 'SOUTH GOA': 562, 'SOUTH TRIPURA': 563, 'SOUTH WEST GARO HILLS': 564, 'SOUTH WEST KHASI HILLS': 565, 'SPSR NELLORE': 566, 'SRIKAKULAM': 567, 'SRINAGAR': 568, 'SUKMA': 569, 'SULTANPUR': 570, 'SUNDARGARH': 571, 'SUPAUL': 572, 'SURAJPUR': 573, 'SURAT': 574, 'SURENDRANAGAR': 575, 'SURGUJA': 576, 'TAMENGLONG': 577, 'TAPI': 578, 'TARN TARAN': 579, 'TAWANG': 580, 'TEHRI GARHWAL': 581, 'THANE': 582, 'THANJAVUR': 583, 'THE NILGIRIS': 584, 'THENI': 585, 'THIRUVALLUR': 586, 'THIRUVANANTHAPURAM': 587, 'THIRUVARUR': 588, 'THOUBAL': 589, 'THRISSUR': 590, 'TIKAMGARH': 591, 'TINSUKIA': 592, 'TIRAP': 593, 'TIRUCHIRAPPALLI': 594, 'TIRUNELVELI': 595, 'TIRUPPUR': 596, 'TIRUVANNAMALAI': 597, 'TONK': 598, 'TUENSANG': 599, 'TUMKUR': 600, 'TUTICORIN': 601, 'UDAIPUR': 602, 'UDALGURI': 603, 'UDAM SINGH NAGAR': 604, 'UDHAMPUR': 605, 'UDUPI': 606, 'UJJAIN': 607, 'UKHRUL': 608, 'UMARIA': 609, 'UNA': 610, 'UNAKOTI': 611, 'UNNAO': 612, 'UPPER SIANG': 613, 'UPPER SUBANSIRI': 614, 'UTTAR KANNAD': 615, 'UTTAR KASHI': 616, 'VADODARA': 617, 'VAISHALI': 618, 'VALSAD': 619, 'VARANASI': 620, 'VELLORE': 621, 'VIDISHA': 622, 'VILLUPURAM': 623, 'VIRUDHUNAGAR': 624, 'VISAKHAPATANAM': 625, 'VIZIANAGARAM': 626, 'WARANGAL': 627, 'WARDHA': 628, 'WASHIM': 629, 'WAYANAD': 630, 'WEST DISTRICT': 631, 'WEST GARO HILLS': 632, 'WEST GODAVARI': 633, 'WEST JAINTIA HILLS': 634, 'WEST KAMENG': 635, 'WEST KHASI HILLS': 636, 'WEST SIANG': 637, 'WEST SINGHBHUM': 638, 'WEST TRIPURA': 639, 'WOKHA': 640, 'YADGIR': 641, 'YAMUNANAGAR': 642, 'YANAM': 643, 'YAVATMAL': 644, 'ZUNHEBOTO': 645}


# State = st.number_input('State: ')
# Season = st.number_input('Season: ')
# District = st.number_input('District: ')

model2 = pickle.load(open('svm.pkl','rb'))

state = st.selectbox(
     'Select State: ',
     stateMap.keys())
district = st.selectbox(
     'Select district: ',
     distMap.keys())
season = st.selectbox(
     'Select Season: ',
     seasonMap.keys())

price = st.number_input('Price: ', value=500)
if price < 220 or price > 29250:
    st.text("Kindly provide price under range.")
else:
    inputData = np.array([[stateMap[state], distMap[district], price, seasonMap[season]]])
    
    if st.button('Predict Crop', key=2):
        outputCrop = model2.predict(inputData)
        print(outputCrop)
        st.title(f"The suitable crop is: {outputCrop[0]}")
        
    

