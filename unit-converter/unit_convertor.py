import streamlit as st # streamlit is a library that allows you to create web apps easily

# Function to convert units based on predefined conversion factor or formulas
def convert_units(value , unit_from , unit_to):
    conversations = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000, # 1 kilometer = 1000 meter
        "grams_kilograms" : 0.001 , # 1 gram = 0.001 kilogram
        "kilograms_grams" : 1000 , # 1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}" # generate a key based on the units

# Logic to convert the value from unit_from to unit_to

    if key in conversations: # if the key is in the dictionary
        conversations = conversations[key] # get the conversion factor
        return value * conversations # return the converted value
    else:
        return "Conversion not supported" #return a messagae if the conversion is not supported
    
st.title("Unit Converter") # set the title of the app

# user input: numerical value to convert from
value = st.number_input("Enter the value:" , min_value= 1.0,step=1.0)

#dropdown to select unit to covert to
unit_from = st.selectbox("Convert from:",["meters" , "kilometers", "grams" , "kilograms"])

#dropdown to select unit to convert to
unit_to = st.selectbox ("Convert to:",["meters" , "kilometers", "grams" , "kilograms"])

# button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value , unit_from , unit_to) # call the function to convert the value
    st.write(f"Converted value : {result}") # display the result
    