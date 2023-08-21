

import streamlit as st
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
    product_needs_text = None
    product_needs_voice = None

    if input_type == "Text":
        # Text box for sharing product needs
        product_needs_text = st.text_area("Share your product needs (text):", "Type here...")
    else:
        # Voice recording option
        st.write("Record your product needs in your own voice!")
        product_needs_voice = st.audio_record("Record your product needs (voice)", format="wav")

    if st.button("Submit"):
        if product_needs_text or product_needs_voice:
            st.success("Thank you for sharing! 🙌 Your input is valuable to us.")
            
            # Store the user input in variables
            user_input = product_needs_text if input_type == "Text" else product_needs_voice
            
            # Now you can use 'user_input' for further processing
            # For example, print it to check the value:
            st.write("User Input:", user_input)
            
        else:
            st.warning("Oops! Please share your product needs with us, either through text or voice recording.")




if __name__ == '__main__':
    main()
