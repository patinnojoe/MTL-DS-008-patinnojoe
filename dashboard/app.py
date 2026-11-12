import streamlit as st

st.title("User Registration Form")

name = st.text_input(label="Full name", placeholder="Enter name, e.g John Doe")
age = st.slider(label='Age', value=18, min_value=18, max_value=70)
button = st.button('Submit')
if button:
    st.write(f"""
    
   User Details Submitted!
   
   Name: {name} 
   
   Age: {age}
    """
    
)