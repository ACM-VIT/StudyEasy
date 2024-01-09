import streamlit as st

# Title of the web page
st.title('Website Name')

# Some description about the website
st.write('About the website')

# Sidebar for file uploader widgets
with st.sidebar:
    st.header("Upload Files")
    ppt = st.file_uploader("Upload PPT", type=['ppt', 'pptx'], key='ppt-uploader')
    csv = st.file_uploader("Upload CSV", type=['csv'], key='csv-uploader')


# You can add functionality to process the uploaded files as needed.
if ppt is not None:
    # Process the PPT file
    st.write("You have uploaded a PPT file.")

if csv is not None:
    # Process the CSV file
    st.write("You have uploaded a CSV file.")


