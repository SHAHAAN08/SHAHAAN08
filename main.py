import streamlit as st
import openai
from streamlit_chat import messages

# Set your API key here
api_key = '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'

openai.api_key = api_key


def ask_openai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  
        prompt=prompt,
        max_tokens=4000,  
        n=1,
        stop = None,
        temperature=0.7,
    )
    messages response.choices[0].text
    return messages


st.title("MSR GPT: powerd by open AI")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['pass'] = []

def get_text():
    input_text =st.text_input("You :", "ASSALAMUALIKUM EVERYONE", key = "input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)


st.session_state.past.append(user_input)
st.session_state.generated.append(user_input)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1)
    message(st.session_state["generated"][i], key=str(i))
    message(st.session_state["past"][i], is_user=True, key=str(i)+ '_user')
    

