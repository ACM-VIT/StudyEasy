import streamlit as st
from streamlit_option_menu import option_menu

# Import your page functions from the folders package
from pages import summary, flashcards, upload

st.set_page_config(page_title="StudyEasy", page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)

st.markdown('<a href="/main" target="_self">Next page</a>', unsafe_allow_html=True)