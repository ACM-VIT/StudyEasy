import streamlit as st
from streamlit_option_menu import option_menu

# Importing specific functions from pages module which are assumed to be different pages of the app

# Configuring the Streamlit app's page settings such as title, icon, layout, and sidebar state
st.set_page_config(
    page_title="StudyEasy",
    page_icon="https://acmvit.in/logo.png",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None,
)

# Custom CSS to hide the Streamlit's hamburger menu on the sidebar
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Setting a header for the app
st.header("_StudyEasy_, by ACM-VIT")

# Setting background image and font style for the app using custom CSS
page_bg_img = f"""
    <style>
    .st-emotion-cache-13k62yr {{
    font-size: 20px;
    background-image: url("https://i.ibb.co/608s6dL/Untitled-design.jpg");
    background-size: cover;
    background-color: rgb(97 46 155);
    }}
    </style>
    """

# Applying the background image style to the app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Adding a text block that describes the functionality of the app
st.text(
    """Introducing ACM VIT's cutting edge Generative AI model made to generate flashcards
    from pdfs and ppts. Study Easy using generated questions that you can use to 
    practice ahead of your tests!"""
)

# Creating a custom button using HTML and CSS that links to the main page of the app
st.markdown(
    f'<a href="/main" target="_self"><button class="button-6" type="button" style="padding: 10px 20px;font-family:sans-serif;border-radius: 14px;background-color:#FFFFFF;color:black;font-size: 16px;">Get Started</button></a>',
    unsafe_allow_html=True,
)

# Subheader for following the organization's social media accounts
st.subheader("Follow us:")
# Creating four columns to add social media icons using HTML
c1, c2, c3, c4 = st.columns(4)
# Each column contains an image wrapped in a hyperlink that leads to the corresponding social media page
c1.markdown(
    "<a href=https://github.com/ACM-VIT> <img src=https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png width=70 height=70> </a>",
    unsafe_allow_html=True,
)
c2.markdown(
    '<a href=https://www.instagram.com/acmvit/> <img src= "https://i.ibb.co/9TPJqkN/Instagram-Glyph-Gradient.png" width=70 height=70> </a>',
    unsafe_allow_html=True,
)
c3.markdown(
    '<a href=https://www.linkedin.com/company/acm-vit/> <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width=70 height=70> </a>',
    unsafe_allow_html=True,
)
c4.markdown(
    '<a href=https://acmvit.in/> <img src="https://acmvit.in/logo.png" width=80 height=80> </a>',
    unsafe_allow_html=True,
)
