import streamlit as st
import pickle

with open('SMS-spam.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    cv = pickle.load(file)

st.markdown(
    """
    <style>
    .main {background-color: #f0f0f5; padding-top: 0px;}
    .stTextArea textarea {background-color: #fffacd; color: black; height: 150px; margin: 0 auto; display: block;}
    .stButton button {background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; font-size: 16px; margin: 0 auto; display: block;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("SMS Spam Classification Application")
st.header("About")
st.write("This is a Machine Learning application to classify SMS as spam or ham.")
st.header("SMS Classification")

user_input = st.text_area("Enter an SMS to classify", placeholder="Type your SMS here...", height=150)

if st.button("Classify", use_container_width=True):
    if user_input:
        data = [user_input]
        vectorized_data = cv.transform(data).toarray()
        result = model.predict(vectorized_data)
        if result[0] == 0:
            st.success("This SMS is not a spam")
        else:
            st.error("This SMS is a spam")
    else:
        st.warning("Please type SMS to classify")
