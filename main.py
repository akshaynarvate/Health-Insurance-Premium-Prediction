import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings

warnings.filterwarnings("ignore")
model = pickle.load(open("Model_Health_insurance.pkl","rb")) #loading the created model


st.set_page_config(page_title="Health Inusrance Premium Prediciton Application") #tab title

#prediction function
def predict_status(age, sex, bmi, smoker):
    input_data = np.asarray([age, sex, bmi, smoker])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("Health Insurance Premium Prediction App")

    #getting the input
    age = st.number_input("Enter your Age")
    sex = st.number_input("Enter your sex(0-Female/1-Male)")
    bmi = st.number_input("Enter your BMI Index")
    smoker = st.number_input("Enter your smoker status(0-No/1-Yes)")

    #predict value
    diagnosis = ""

    if st.button("Predict"):
    
        diagnosis = predict_status(age, sex, bmi, smoker)
        if diagnosis:
            st.write("Rs: ", diagnosis)

        else:
            st.error("Please Re-Enter your details")
        
        st.write("Project by Akshay Narvate")
    
            
if __name__=="__main__":
    main()
