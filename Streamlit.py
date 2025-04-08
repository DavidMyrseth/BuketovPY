import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Todo List")

def add_task():
    task = st.text_input("Sisesta uus ülsanne". key="")
