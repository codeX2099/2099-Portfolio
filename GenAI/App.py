import streamlit as st
from openai import OpenAI

st.snow()
# Read API key from file
with open("Key_For_OpenAI/Key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

# Set colored page title
st.title(":red[Python Code Review through OpenAI API Key]")

# User input section
st.header(":orange[Enter Your Python Code]", divider='blue')
prompt = st.text_area("Enter your Python code here:", height=150)

# Button to trigger code review
if st.button("Code Review"):
    st.markdown("<h3 style='color:violet;'>Processing Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": "Scan the python code and generate what are the mistakes involved and recorrect all of them"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    st.balloons()
    generated_text = response.choices[0].message.content
    st.write(generated_text)
