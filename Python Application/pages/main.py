import streamlit as st
from streamlit_option_menu import option_menu
from pages import summary, flashcards, upload

st.set_page_config(page_title="StudyEasy", page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)

def main():
    # Using option_menu for a sidebar navigation menu

    selected = option_menu(
        menu_title=None,
        options= ["Upload","Summary", "Flashcards"], 
        icons=['book', 'book', 'book'], 
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal"
        )
    
    if selected == "Upload":
        upload.app()
    elif selected == "Summary":
        summary.app()
    elif selected == "Flashcards":
        flashcards.app()


    st.markdown('<a href="/" target="_self">Back to Home Page</a>', unsafe_allow_html=True)
    

if __name__ == "__main__":
    main()