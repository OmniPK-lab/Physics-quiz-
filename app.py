import streamlit as st

st.title("JEE Physics Practice Quiz")

st.subheader("Question 1")
st.write("What is the formula for kinetic energy?")

choice = st.radio(
    "Choose from the options below:",
    ["(A) 1/2mv²", "(B) 4/7mv⁴", "(C) 64/9m⁶v⁴"]
)

if st.button("Submit Answer"):
    if "(A)" in choice:
        st.success("You are correct! 🎉")
    else:
        st.error("It is wrong, practice harder next time! 💡")

