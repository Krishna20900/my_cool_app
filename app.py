import streamlit as st

st.title("My Super Cool Calculator!")

# Add cute emojis for fun
st.write("🔢 Let's add some numbers! ✨")

# Get numbers from the user
number1 = st.number_input("Enter the first number", value=0)
number2 = st.number_input("Enter the second number", value=0)

# Add a colorful button
if st.button("Calculate! 🎈"):
    result = number1 + number2
    st.success(f"The answer is {result}! 🎉")