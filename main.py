import streamlit as st


st.title("Student details")
Name = st.text_input("Enter your name : ")
Father_name = st.text_input("Enter your father name : ")
Add = st.text_area("Enter your add : ")
Class = st.selectbox("Which is best turist place:", ("Hazarduari", "katramasjit", "Katgola Bagan", "House of Jegeth seth"))
button = st.button("Done")

if button:
    st.markdown(
        f"Name : {Name} "
        f"Father name : {Father_name} "
        f"Address : {Add} "
        f"Best turist place : {Class}"
                 )