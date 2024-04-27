import streamlit as st
import subprocess

def main():
    st.title("Sign Language Detection")
    
    # Add a button to run the inference_classifier.py script
    if st.button("Run Inference Classifier"):
        # Execute inference_classifier.py as a subprocess
        process = subprocess.Popen(["python", "inference_classifier.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for the process to finish and capture output
        stdout, stderr = process.communicate()
        
        # Display the output
        st.text("Output:")
        st.text(stdout.decode())
        st.text("Errors:")
        st.text(stderr.decode())

if __name__ == "__main__":
    main()
