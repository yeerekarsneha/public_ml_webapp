import pickle
import streamlit as st
from PIL import Image

# Loading the saved models
diabetes_model = pickle.load(open('C:/Users/heera/OneDrive/Desktop/python-ws/trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/heera/OneDrive/Desktop/python-ws/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/heera/OneDrive/Desktop/python-ws/parkinsons_model.sav', 'rb'))
migraine_model = pickle.load(open('C:/Users/heera/OneDrive/Desktop/python-ws/migraine_model.sav', 'rb'))
lungs_model = pickle.load(open('C:/Users/heera/OneDrive/Desktop/python-ws/lung_disease_classifier.sav', 'rb'))
obesity_model = pickle.load(open('C:/Users/heera/OneDrive/Desktop/python-ws/rf_model.sav', 'rb'))
covid19_model = pickle.load(open('C:/Users/heera/OneDrive/Desktop/python-ws/covid_model.sav', 'rb'))

# Styling for 3D containers
st.markdown("""
    <style>
    .card {
        background-color: white;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        width: 300px;
        border-radius: 10px;
    }

    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }

    .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }

    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Home page with 3D containers
st.title('Multiple Disease Prediction System')

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    
    if st.button('Diabetes Prediction', key='diabetes'):
        st.session_state.page = 'Diabetes Prediction'
    st.markdown("""
        <div class='card'>
            <h3>Diabetes Prediction</h3>
            <p>Predict if a person has diabetes.</p>
            <button class='button' onclick="document.getElementById('diabetes').click();">Predict</button>
        </div>
    """, unsafe_allow_html=True)

    if st.button('Heart Disease Prediction', key='heart'):
        st.session_state.page = 'Heart Disease Prediction'
    st.markdown("""
        <div class='card'>
            <h3>Heart Disease Prediction</h3>
            <p>Predict if a person has heart disease.</p>
            <button class='button' onclick="document.getElementById('heart').click();">Predict</button>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Parkinson's Prediction", key='parkinsons'):
        st.session_state.page = "Parkinson's Prediction"
    st.markdown("""
        <div class='card'>
            <h3>Parkinson's Prediction</h3>
            <p>Predict if a person has Parkinson's disease.</p>
            <button class='button' onclick="document.getElementById('parkinsons').click();">Predict</button>
        </div>
    """, unsafe_allow_html=True)

    if st.button('Migraine Prediction', key='migraine'):
        st.session_state.page = 'Migraine Prediction'
    st.markdown("""
        <div class='card'>
            <h3>Migraine Prediction</h3>
            <p>Predict if a person has migraine.</p>
            <button class='button' onclick="document.getElementById('migraine').click();">Predict</button>
        </div>
    """, unsafe_allow_html=True)

    if st.button('Lung Disease Prediction', key='lungs'):
        st.session_state.page = 'Lung Disease Prediction'
    st.markdown("""
        <div class='card'>
            <h3>Lung Disease Prediction</h3>
            <p>Predict if a person has lung disease.</p>
            <button class='button' onclick="document.getElementById('lungs').click();">Predict</button>
        </div>
    """, unsafe_allow_html=True)

    if st.button('Obesity Prediction', key='obesity'):
        st.session_state.page = 'Obesity Prediction'
    st.markdown("""
        <div class='card'>
            <h3>Obesity Prediction</h3>
            <p>Predict if a person is obese.</p>
            <button class='button' onclick="document.getElementById('obesity').click();">Predict</button>
        </div>
    """, unsafe_allow_html=True)

    if st.button('COVID-19 Prediction', key='covid19'):
        st.session_state.page = 'COVID-19 Prediction'
    st.markdown("""
        <div class='card'>
            <h3>COVID-19 Prediction</h3>
            <p>Predict if a person has COVID-19.</p>
            <button class='button' onclick="document.getElementById('covid19').click();">Predict</button>
        </div>
    """, unsafe_allow_html=True)

    if st.button('Precautionary Measures', key='precautions'):
        st.session_state.page = 'Precautionary Measures'
    st.markdown("""
        <div class='card'>
            <h3>Precautionary Measures</h3>
            <p>Learn about precautions for various diseases.</p>
            <button class='button' onclick="document.getElementById('precautions').click();">Learn</button>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Diabetes Prediction Page
if st.session_state.page == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    st.image('https://images.cnbctv18.com/wp-content/uploads/2021/02/diabetes1.jpg?impolicy=website&width=590&height=264')  # Replace with an actual URL

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.slider('Number of Pregnancies', 0, 20, 1)
    with col2:
        Glucose = st.slider('Glucose Level', 0, 200, 110)
    with col3:
        BloodPressure = st.slider('Blood Pressure value', 0, 122, 80)
    with col1:
        SkinThickness = st.slider('Skin Thickness value', 0, 99, 20)
    with col2:
        Insulin = st.slider('Insulin Level', 0, 846, 80)
    with col3:
        BMI = st.slider('BMI value', 0.0, 67.1, 25.0)
    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value', 0.0, 2.5, 0.5)
    with col2:
        Age = st.slider('Age of the Person', 0, 120, 25)

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if st.session_state.page == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    st.image('https://distilinfo.com/pophealth/wp-content/uploads/sites/13/2023/11/04-3.jpg')  # Replace with an actual URL

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider('Age', 0, 120, 25)
    with col2:
        sex = st.slider('Sex (1 = Male, 0 = Female)', 0, 1, 0)
    with col3:
        cp = st.slider('Chest Pain types', 0, 3, 1)
    with col1:
        trestbps = st.slider('Resting Blood Pressure', 0, 200, 120)
    with col2:
        chol = st.slider('Serum Cholesterol in mg/dl', 100, 400, 150)
    with col3:
        fbs = st.slider('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', 0, 1, 0)
    with col1:
        restecg = st.slider('Resting Electrocardiographic results', 0, 2, 1)
    with col2:
        thalach = st.slider('Maximum Heart Rate achieved', 60, 200, 150)
    with col3:
        exang = st.slider('Exercise Induced Angina (1 = Yes, 0 = No)', 0, 1, 0)
    with col1:
        oldpeak = st.slider('ST depression induced by exercise', 0.0, 6.2, 1.0)
    with col2:
        slope = st.slider('Slope of the peak exercise ST segment', 0, 2, 1)
    with col3:
        ca = st.slider('Number of major vessels colored by fluoroscopy', 0, 3, 0)
    with col1:
        thal = st.slider('Thal: 0 = Normal; 1 = Fixed defect; 2 = Reversible defect', 0, 2, 1)

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if st.session_state.page == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    st.image('https://www.basicthinking.com/wp-content/uploads/2024/04/ki-parkinson.jpeg')  # Replace with an actual URL

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.slider('MDVP:Fo(Hz)', 100, 200, 150)
    with col2:
        fhi = st.slider('MDVP:Fhi(Hz)', 100, 250, 150)
    with col3:
        flo = st.slider('MDVP:Flo(Hz)', 65, 210, 90)
    with col4:
        Jitter_percent = st.slider('MDVP:Jitter(%)', 0.0, 0.01, 0.005)
    with col5:
        Jitter_Abs = st.slider('MDVP:Jitter(Abs)', 0.0, 0.0001, 0.00005)
    with col1:
        RAP = st.slider('MDVP:RAP', 0.0, 0.01, 0.005)
    with col2:
        PPQ = st.slider('MDVP:PPQ', 0.0, 0.01, 0.005)
    with col3:
        DDP = st.slider('Jitter:DDP', 0.0, 0.03, 0.015)
    with col4:
        Shimmer = st.slider('MDVP:Shimmer', 0.0, 0.1, 0.05)
    with col5:
        Shimmer_dB = st.slider('MDVP:Shimmer(dB)', 0.0, 1.0, 0.5)
    with col1:
        APQ3 = st.slider('Shimmer:APQ3', 0.0, 0.05, 0.025)
    with col2:
        APQ5 = st.slider('Shimmer:APQ5', 0.0, 0.1, 0.05)
    with col3:
        APQ = st.slider('MDVP:APQ', 0.0, 0.1, 0.05)
    with col4:
        DDA = st.slider('Shimmer:DDA', 0.0, 0.1, 0.05)
    with col5:
        NHR = st.slider('NHR', 0.0, 1.0, 0.5)
    with col1:
        HNR = st.slider('HNR', 0.0, 1.0, 0.5)
    with col2:
        RPDE = st.slider('RPDE', 0.0, 1.0, 0.5)
    with col3:
        DFA = st.slider('DFA', 0.0, 1.0, 0.5)
    with col4:
        spread1 = st.slider('spread1', -1.0, 1.0, 0.0)
    with col5:
        spread2 = st.slider('spread2', -1.0, 1.0, 0.0)
    with col1:
        D2 = st.slider('D2', 0.0, 5.0, 2.5)
    with col2:
        PPE = st.slider('PPE', 0.0, 1.0, 0.5)

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person have Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

# Migraine Prediction Page
if st.session_state.page == 'Migraine Prediction':
    st.title('Migraine Prediction using ML')
    st.image('https://www.sapnamed.com/wp-content/uploads/2019/02/migraine-headaches-768x768.jpg')  # Replace with an actual URL

    col1, col2, col3 = st.columns(3)
    with col1:
        severity  = st.slider(('Severity (0-10)'), 0, 10, 5)
    with col2:
        frequency = st.slider('Frequency (per month)', 0, 10, 2)
    with col3:
        sensitivity_to_light = st.checkbox('Sensitivity to Light')
    with col1:
        sensitivity_to_sound = st.checkbox('Sensitivity to Sound')
    with col2:
       nausea = st.checkbox('Nausea')
    migraine_diagnosis = ''
    if st.button('Migraine Test Result'):
        migraine_prediction = migraine_model.predict([[severity,frequency,sensitivity_to_light,sensitivity_to_sound,nausea]])
        if migraine_prediction[0] == 1:
            migraine_diagnosis = 'The person  have migraines'
        else:
            migraine_diagnosis = 'The person does not have migraines'
        st.success(migraine_diagnosis)

# Lung Disease Prediction Page

if 'page' not in st.session_state:
    st.session_state['page'] = 'Lung Disease Prediction'

if st.session_state['page'] == 'Lung Disease Prediction':
    st.title('Lung Disease Prediction using ML')
    st.image('https://pulmonarypracticeassociates.com/wp-content/uploads/2018/11/Services-LungDisease-img.jpg')  # Replace with an actual URL

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider('Age', 0, 100, 21)
    with col2:
        smoking_history = st.slider('Smoking History (pack years)', 0, 1, 0)
    with col3:
        shortness_of_breath = st.slider('Shortness of Breath', 0, 1, 0)
    with col1:
        chest_pain = st.slider('Chest Pain', 0, 1, 0)
    with col2:
        cough = st.slider('Cough', 0, 1, 0)
    with col3:
        fatigue = st.slider('Fatigue', 0, 1, 0)
    with col1:
        fever = st.slider('Fever', 0, 1, 0)
    with col2:
        weight_loss = st.slider('Weight Loss', 0, 1, 0)

    lung_diagnosis = ''
    if st.button('Lung Disease Test Result'):
        # Predict using the model
        lung_prediction = lungs_model.predict([[age, smoking_history, shortness_of_breath, chest_pain, cough, fatigue, fever, weight_loss]])

        # Map the prediction to disease names (this is just an example, adjust according to your model)
        diseases = {
            0: 'No Lung Disease',
            1: 'Chronic Obstructive Pulmonary Disease (COPD)',
            2: 'Lung Cancer',
            3: 'Pneumonia',
            4:'Pulmonary_Embolism'
            5:'Asthma'
            6:'Bronchitis'
            7:'Emphysema'
            8:'Pulmonary_Fibrosis'
            9:'Pleural_Effusion'
            10:'Tuberculosis'
            # Add other mappings as per your model
        }

        predicted_disease = diseases.get(lung_prediction[0], 'Unknown Disease')
        lung_diagnosis = f'The person is predicted to have: {predicted_disease}'
        st.success(lung_diagnosis)

# Obesity Prediction Page
if st.session_state.page == 'Obesity Prediction':
    st.title('Obesity Prediction using ML')
    st.image('https://www.shutterstock.com/shutterstock/photos/1088402456/display_1500/stock-vector-obesity-word-with-measuring-tape-diet-theme-vector-illustration-1088402456.jpg')  # Replace with an actual URL

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider('Age', 0, 120, 25)
    with col2:
        gender = st.selectbox('Gender', ['Female', 'Male'])

    with col3:
        bmi = st.slider('BMI', min_value=10.0, max_value=50.0, value=25.0)

    with col1:
        physical_activity = st.selectbox('Physical Activity', ['Active', 'Inactive'])
  
    obesity_diagnosis = ''
    if st.button('Obesity Test Result'):
        obesity_prediction = obesity_model.predict([[age,gender, bmi, physical_activity]])
        if obesity_prediction[0] == 1:
            obesity_diagnosis = 'The person is predicted to be obese'
        else:
            obesity_diagnosis = 'The person is not predicted to be obese'
        st.success(obesity_diagnosis)

# COVID-19 Prediction Page
if st.session_state.page == 'COVID-19 Prediction':
    st.title('COVID-19 Prediction using ML')
    st.image('https://www.imf.org/-/media/Images/IMF/Topics/COVID19/lending-tracker-fullsize-istock-1213355637.ashx?h=1413&w=2122&la=en')  # Replace with an actual URL

    col1, col2, col3 = st.columns(3)
    with col1:
        fever = st.slider('Fever (°F)', 95.0, 105.0, 98.6)

    with col2:
        cough = st.slider('Cough')

    with col3:
    fatigue = st.slider('Fatigue')
    with col1:
        loss_of_taste_smell = st.slider('Loss of Taste or Smell')

    with col2:
    difficulty_breathing = st.slider('Difficulty Breathing')
   
    covid_diagnosis = ''
    if st.button('COVID-19 Test Result'):
        covid_prediction = covid19_model.predict([[fever, cough,fatigue,loss_of_taste_smell,difficulty_breathing]])
        if covid_prediction[0] == 1:
            covid_diagnosis = 'The person  have COVID-19'
        else:
            covid_diagnosis = 'The person does not  to have COVID-19'
        st.success(covid_diagnosis)

# Precautionary Measures Page
if st.session_state.page == 'Precautionary Measures':
    st.title('Precautionary Measures for Various Diseases')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF1M3psaQPeeIBImFpyvL4QR2un-fqmmznAA&s')  # Replace with an actual URL

    st.write("""
        Here are some precautionary measures you can take to prevent various diseases:
        - **Diabetes**: Maintain a healthy diet, exercise regularly, monitor blood sugar levels.
        - **Heart Disease**: Eat a balanced diet, exercise regularly, avoid smoking, monitor blood pressure.
        - **Parkinson's Disease**: Exercise regularly, eat a balanced diet, avoid head injuries.
        - **Migraine**: Manage stress, maintain a regular sleep schedule, avoid known triggers.
        - **Lung Disease**: Avoid smoking, reduce exposure to pollutants, maintain good respiratory hygiene.
        - **Obesity**: Eat a balanced diet, exercise regularly, manage stress.
        - **COVID-19**: Practice good hygiene, wear masks in crowded places, maintain social distancing.
    """)
