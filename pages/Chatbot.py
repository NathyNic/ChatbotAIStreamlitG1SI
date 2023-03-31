#Importando librerias
import openai
import streamlit as st
from streamlit_chat import message

#API Key
openai.api_key = st.secrets["api_secret"]

#Creamos una función que generará las llamadas desde el API
def generar_respuesta(prompt):
    comp = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens=1024,
        n = 1,
        temperature = 0.9,
        stop = None
    )
    message = comp.choices[0].text
    return message

st.title("StarFly ChatBot")

#Guardando el chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

#Función para obtener el mensaje del usuario
def obtener_texto():
    input_text = st.text_input("Ud: ", "Hola, ¿cómo estás?", key="input")
    return input_text

user_input = obtener_texto()

if user_input:
    output = generar_respuesta(user_input)
    #Guardamos la salida
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')