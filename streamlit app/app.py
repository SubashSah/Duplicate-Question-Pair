import streamlit as st
import helper
import pickle

# Load the .pkl file
with open('model.pkl', 'rb') as file:  # 'rb' = read binary mode
    model = pickle.load(file)

st.header("Duplicate Question Pairs")

q1=st.text_input("Enter question 1")
q2=st.text_input("Enter question 2")

if st.button("Find"):
    query=helper.query_point_creator(q1,q2)
    result=model.predict(query)[0]

    if result:
        st.header("Duplicate")
    else:
        st.header("Not Duplicate")
    