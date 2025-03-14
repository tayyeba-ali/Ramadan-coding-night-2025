import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include lowercase and uppercase letters

    if use_digits:
        characters += string.digits  # Add digits (0-9)

    if use_special:
        characters += string.punctuation  # Add special characters (!, @, #, etc.)

    # Generate and return the password
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

st.write("-----------------------")
st.write("Built with 💙 by [Tayyeba Ali](https://github.com/tayyeba-ali)")
