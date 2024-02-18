from src.Student_performance_prediction.Pipelines.prediction_pipeline import CustomData, PredictPipeline

import streamlit as st


def main():
    st.title("Welcome to student marks prediction app!")

    gender = st.selectbox("Please enter your gender", ("male", "female"))
    race_ethinicity = st.selectbox("Please enter your ethnicity", ("group A", "group B", "group C", "group D", "group E"))
    parental_level_of_education = st.selectbox("Please enter your parents education", 
                                               ("associate's degree", "bachelor's degree", "high school", "master's degree",
                                                "some college", "some high school"))
    
    lunch = st.selectbox("Please enter type of lunch you have opted for", ("free/reduced", "standard"))
    test_preparation_course = st.selectbox("Please enter the course status", ("none", "completed"))
    reading_score = st.number_input("Please enter the reading score")
    writing_score = st.number_input("Please enter the writing score")

    data = CustomData(gender, race_ethinicity, parental_level_of_education, lunch, 
                      test_preparation_course, reading_score, writing_score)
    
    final_data = data.get_data_as_df()
    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(final_data)
    result = round(prediction[0],2)

    st.button("Submit")

    st.write(f"The result of the student is: {result}")

if __name__ == "__main__":
    main()



