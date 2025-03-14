import streamlit as st
import random
import string

def generate_password(Length , use_digits , use_sepecial):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_sepecial:
        characters += string.punctuation #add special characters (! , @ , # etc)

        return ''.join(random.choice(characters) for _ in range(Length))
    
st.title("Password Generator")
length = st.slider("Password Length", min_value=6, max_value=32 , value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")
if st.button("Generate Password"):
    password = generate_password(length , use_digits , use_special)
    st.write(f"Generated Password: `{password}`")

st.write("-----------------------")
st.write("Build with 💙 by [Tayyeba Ali](https://github.com/tayyeba-ali)")