import streamlit as st
from audio_recorder_streamlit import audio_recorder
import modal
import json
import os



def main():
    # Enthusiastic welcome message
    st.title("Welcome to the Product Needs Portal!")
    st.write("Hello there! 🌟 We're excited to hear about your product needs. You can share your thoughts with us through text or voice!")

    # Radio button to select input type
    input_type = st.radio("Select input type:", ["Text", "Voice"])

    # Initialize variables
    product_needs_text = ""
    product_needs_audio = None

    if input_type == "Text":
        # Text box for sharing product needs
        product_needs_text = st.text_area("Share your product needs (text):", "Type here...")
    else:
        # Voice recording option
        st.write("Record your product needs in your own voice!")
        audio_bytes = audio_recorder()
        product_needs_voice = st.audio(audio_bytes, format="audio/wav")

    if st.button("Submit"):
        if product_needs_text or product_needs_voice:
            st.success("Thank you for sharing! 🙌 Your input is valuable to us.")
            process_button = st.sidebar.button("Processing Input")
            st.sidebar.markdown("**Note**: Podcast processing can take upto 5 mins, please be patient.")
            
            # Store the user input in variables
            user_input = product_needs_text if input_type == "Text" else product_needs_voice
            prod_recom = process_recommendation(user_input)
            
            # Now you can use 'user_input' for further processing
            # For example, print it to check the value:
            st.write("Product Recommended:", prod_recom) 
        else:
            st.warning("Oops! Please share your product needs with us, either through text or voice recording.")
    
def process_recommendation(user_input):
    f = modal.Function.lookup("corise-prod_recommendation-project", "prod_recommendation")
    output = f.call(url, '/content/podcast/')
    return output

if __name__ == '__main__':
    main()
