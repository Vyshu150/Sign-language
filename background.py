import streamlit as st

# Define the custom CSS style with background image
page_bg_img = '''
    <style>
        [data-testid="stAppViewContainer"]{
        background-color:black;
        }
    </style>
'''

# Apply the custom CSS style using Markdown
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("it is the summer")
