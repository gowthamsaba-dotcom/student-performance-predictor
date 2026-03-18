import streamlit as st
import joblib
import pandas as pd

# Title
st.title("Student Performance Predictor")

# Title description
st.write("Enter student details to predict math score")

# Load the trained model
model = joblib.load("model/student_model.pkl")

# Creating user inputs in the web browser
gender = st.selectbox(
    "Gender",
    ["male","female"]
)
race = st.selectbox(
    "Race / Ethnicity",
    ["group A","group B","group C","group D","group E"]
)
parent_edu = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)
lunch = st.selectbox(
    "Lunch Type",
    ["standard","free/reduced"]
)
test_prep = st.selectbox(
    "Test Preparation",
    ["none","completed"]
)
reading = st.slider("Reading Score",0,100,50)
writing = st.slider("Writing Score",0,100,50)


# Convert user inputs into a data frame
input_data = pd.DataFrame({
    "gender":[gender],
    "race/ethnicity":[race],
    "parental level of education":[parent_edu],
    "lunch":[lunch],
    "test preparation course":[test_prep],
    "reading score":[reading],
    "writing score":[writing]
})


# One Hot Encoding- Convert text to boolean
input_encoded = pd.get_dummies(input_data)

# fetch the actual columns/features exist in the model
model_columns = model.feature_names_in_


# Match the input data with the features that model expects
# This will fill Model's extra features which was not present in the input as 0
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)


# Get the predicted score from the model by passing the input data
if st.button("Predict Math Score"):
    prediction = model.predict(input_encoded)
    st.success(f"Predicted Math Score: {prediction[0]:.2f}")