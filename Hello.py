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

    | Alexander Torre Arteaga |
    | Angel Gerardo Carmen Cruzatti |
    | Jesus Orlando Gil Jauregui|
    | Jorge Luis, Marin Evangelista |
    | Nathaly Nicole Pichilingue Pimentel | 
    

    ### Especificaciones:
    **Donde muestra las predicciones/los resultados:**
    - Gráficamente. 
    - Númericamente los valores de las predicciones (print de dataframe con la predicción o clasificación).
    
    **Donde se muestra el EDA:**
    - Ploteo de los precios reales.
    (Ploteo de media móvil los precios reales.)

    **Donde el usuario pueda indicar:**
    - El modelo ejecutar.
    - La acción o instrumento financiero que quiera analizar..
"""
)
