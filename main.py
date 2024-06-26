# Legal Consultant App!

import streamlit as st
import openai

# Title and description
st.title("Legal Consultant!")
st.write("Ask any legal question, and get a general overview or guidance. Please note that this is not a substitute for professional legal advice.")

# Include sidebar with credentials
with st.sidebar:
    st.markdown('Legal Consultant (V 0.1)')
    st.markdown("""
    #### Let's contact:
    [Kamran Feroz](https://www.linkedin.com/in/kamranferoz/)
    #### Powered by:
    [OpenAI](https://openai.com/)
    [Langchain](https://github.com/hwchase17/langchain)
    #### Source code:
    [Legal Consultant!](https://github.com/kamranferoz/legalCons)
    """)

st.markdown("<style>#MainMenu{visibility:hidden;}</style>", unsafe_allow_html=True)

# Set OpenAI API key
openai_api_key = st.secrets['OPENAI_API_KEY']

def generate_response(input_text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=input_text,
        temperature=0.7,
        max_tokens=150,
        api_key=openai_api_key
    )
    st.info(response.choices[0].text)

with st.form('my_form'):
    # Text input and language selection
    text = st.text_area("Enter your legal question:", "")
    law_area = st.selectbox("Select under which law:", ["International", "Pakistani", "Shariah", "Indian", "US"])
    submitted = st.form_submit_button('Submit')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response("You are an experienced lawyer. Provide the consultancy regarding the following legal query under " + law_area + " law: " + text)

# Disclaimer
st.write("Disclaimer: This AI legal consultant provides general information and is not a substitute for professional legal advice. Always consult with a qualified attorney for specific legal guidance.")
