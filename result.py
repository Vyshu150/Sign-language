import streamlit as st
import subprocess

def main():
    try:
        # Set page title and background color
        st.set_page_config(page_title="Sign Language Detection", page_icon=":eyes:")
        custom_css = """
<style>
    [data-testid="stAppViewContainer"] {
    background-size: cover; /* Ensure the background image covers the entire area */
    background-repeat: no-repeat; /* Prevent the background image from repeating */
    color: #ffffff; /* Set text color to white */
    padding: 20px; /* Add padding */
    margin: 0;
    background-position: center;
    animation: slideBackground 10s infinite;
}

@keyframes slideBackground {
    0% {
        background-image: url('https://wallpapercave.com/wp/wp6944999.png');
    }
    33.3% {
        background-image: url('https://png.pngtree.com/thumb_back/fw800/background/20230320/pngtree-a-young-man-using-sign-language-to-communicate-during-a-video-call-on-his-laptop-photo-image_50392366.jpg');
    }
    66.6% {
        background-image: url('https://mrwallpaper.com/images/hd/delightful-finger-heart-on-cute-pc-design-30l96p32evfftm7u.jpg');
    }
    100% {
        background-image: url('https://wallpapercave.com/wp/wp6944999.png');
    }
}


    .button-wrapper {
        padding: 20px; /* Add padding to buttons */
        background-color: #000000; /* Set button background color */
        border-radius: 10px; /* Add border radius for rounded corners */
    }
    .button-wrapper button {
        color: #ffffff !important; /* Set button text color to white */
    }
    .stButton > button {
        background-color: #00cc00 !important; /* Set button background color to green */
        color: #ffffff !important; /* Set button text color to white */
    }
    .result {
        color: #00cc00 !important; /* Set result text color to green */
        font-weight: bold; /* Make the text bold */
        font-size: 30px; /* Set font size to 30 pixels */
    }
</style>
"""

# Apply custom CSS styles using markdown
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown("<h1 style='color: green; font-size: 56px;'>Sign Language Detection</h1>", unsafe_allow_html=True)

        # Write usage instructions
        st.write("""
        ##How to Use This Sign App (There are Four buttons for Four purposes): 
                 After clicking on any button, the camera window will open. To exit, press 's'.
        1. The First button is used to predict continuously when you show your hands.
        2. The Second button will predict and provide audio feedback.
        3. The Third and Fourth buttons will provide words based on the signs.
                 
        """)

        # Load icons
        sign_icon = "sign_icon.jpg"  # Replace with the path to your sign icon image
        audio_icon = "audio_icon.jpg"  # Replace with the path to your audio icon image
        other_icon = "other_icon.jpg"  # Replace with the path to your other icon image

        # Display icons with buttons
        col1, col2, col3, col4 = st.columns(4)  # Create 4 equal columns

        with col1:
            st.image(sign_icon, width=100)
            if st.button("Predict", key="predict_sign"):
                # Execute inference_classifier.py as a subprocess
                subprocess.run(["python", "inference_classifier.py"])
        with col2:
            st.image(audio_icon, width=100)
            if st.button("Audio", key="predict_audio"):
                # Execute inference_sign_audio.py as a subprocess
                subprocess.run(["python", "app.py"])
        with col3:
            st.image(other_icon, width=100)
            if st.button("Words1", key="predict_other"):
                # Execute inference_other_words.py as a subprocess
                subprocess.run(["python", "classifier.py"])
        with col4:
            st.image(other_icon, width=100)
            if st.button("Words", key="predict_new_other"):
                # Execute inference_other_words.py as a subprocess
                subprocess.run(["python", "words.py"])

        # Add the redirect button
        redirect_url = "https://forms.office.com/r/nzxuQStXib"  # Specify the URL you want to redirect to
        if st.button("Evaluation By Only Todd Jones"):
            # Prompt the user with a JavaScript confirmation dialog
            confirm_script = """
            <script>
                var confirmed = confirm("Are you Todd Johnes?");
                if (confirmed) {
                    window.open("%s", "_blank");
                }
            </script>
            """ % redirect_url
            st.markdown(confirm_script, unsafe_allow_html=True)

        
        

        # Display images
        with col1:
            st.image("sign.png", width=100)
        with col2:
            st.image("hungry.png", width=100)
        with col3:
            st.image("wordsign1.png", width=100)
        with col4:
            st.image("wordsign2.png", width=100)
        # Display result

    # Write usage instructions
        st.write("""
        ## <h1 style='color: green; font-size: 24px;'>We utilized Python and Streamlit for the development framework. We employed the Random Forest algorithm for predictive modeling.Additionally, I employed a custom dataset tailored to the specific requirements of the project.</h1>
        """, unsafe_allow_html=True)
        st.write("""
        ## <span style='color: #008080; font-family: Arial, sans-serif; font-weight: bold; font-size: 28px;'>Team Members:</span>
        - <span style='color: #008000; font-size: 24px;'>**Divya (Python Backend):**</span> Divya spearheaded the Python backend development.
        - <span style='color: #0000FF; font-size: 24px;'>**Uday (Frontend Development):**</span> Uday was responsible for frontend development.
        - <span style='color: #800080; font-size: 24px;'>**Vyshnavi (Dataset Collection and Cleaning):**</span> Vyshnavi led the efforts in collecting and cleaning the dataset.
        - <span style='color: #FF4500; font-size: 24px;'>**Professor Todd Jones:**</span> Mr. Todd Jones provided guidance and mentorship throughout the project.
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
