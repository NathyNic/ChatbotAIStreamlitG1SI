import streamlit as st

st.set_page_config(
    page_title="Tarea Semana 1",
    page_icon="👋",
)

st.write("# Chatbot Grupo 1 🤖")

st.sidebar.success("Seleccione un modelo del menú")

st.markdown(
    """
    # Grupo 1 - Integrantes:
    | Nombre |
    |--|--|
    | Oscar Stalyn, Yanfer Laura | 
    | Diego Tharlez Montalvo Ortega | 
    | Jorge Luis Quispe Alarcon | 
    | Wilker Edison,Atalaya Ramirez |
    | Anthony Elias,Ricse Perez | 
    | Carlos Daniel Tarmeño Noriega | 
    | Nathaly Nicole Pichilingue Pimentel | 
    | Jorge Luis, Marin Evangelista |

    ### Especificaciones:
    **Donde muestra las predicciones/los resultados:**
    - Gráficamente. 
    - Númericamente los valores de las predicciones (print de dataframe con la predicción o clasificación).
    
    **Donde se muestra el EDA:**
    - Ploteo de los precios reales.
    (Ploteo de media móvil los precios reales.)

    **Donde el usuario pueda indicar:**
    - El modelo ejecutar.
    - La acción o instrumento financiero que quiera analizar.
"""
)
