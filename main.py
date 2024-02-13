# Crear un sitio con streamlit que responda al siguiente objetivo de interacción, considerando lo que está entre llaves las variables dinámicas a aportar entre los usuarios: "Genera un discurso político {tipo_discurso} sobre {tema} destinado a {publico_objetivo}. Incluye argumentos convincentes y utiliza un tono {tono_deseado}. Incluye estos datos duros: {datos_duros}" 

import streamlit as st
import os
import dotenv
from openai import OpenAI, AuthenticationError
# from funciones import generador_discurso_politico
from env import OPENAI_API_KEY


# Cargar variables de entorno
dotenv.load_dotenv()
OpenAi_API_KEY = os.getenv(OPENAI_API_KEY)


try:
    # Inicializar el cliente de OpenAI con la clave de API
    client = OpenAI(api_key="OpenAi_API_KEY")
except AuthenticationError as e:
    st.error(f"Error de autenticación: {e}")


# client = OpenAI(api_key="OpenAi_API_KEY")

# Función para generar el discurso político. Que datos_duros sea opcional y que se pueda generar el discurso con o sin datos duros.

def generador_discurso_politico(tipo_discurso, tema, publico_objetivo, tono_deseado, datos_duros=None):
    prompt=f"Genera un discurso político {tipo_discurso} sobre {tema} destinado a {publico_objetivo}. Incluye argumentos convincentes y utiliza un tono {tono_deseado}"
    if datos_duros:
        prompt += f" Incluye estos datos duros: {datos_duros}"

    response = client.chat.completions.create(

        model="gpt-3.5-turbo",
         messages=[
        {
            "role": "user",
            "content": prompt
        }
        ],
        max_tokens=150
    )
    return response.choices[0].message.content



# Cabecera de sitio en streamlit

st.title('Generador de discursos políticos')

st.subheader('Completa los siguientes campos para generar un discurso político. El discurso será de 100 palabras como máximo.')



# Campos a rellenar por el usuario, adaptados a streamlit

tema = st.text_input('Tema central a tratar:')


# crear lista de tipo discursos para mostrar en un select, adaptado a streamlit
tipo_discurso = st.selectbox('Elige el tipo de discurso:', ['Informativo', 'Persuasivo', 'Inspiracional', 'Motivacional', 'Educativo'])


#crear selección múltiple de público objetivo a partir de una lista de opciones, adaptado a streamlit
publico_objetivo = st.multiselect('Elige el público objetivo (pueden ser varias opciones):', ['Jóvenes', 'Adultos', 'Adultos mayores', 'Mujeres', 'Hombres', 'Niños', 'Niñas', 'Empresarios', 'Trabajadores', 'Estudiantes', 'Profesionales', 'Desempleados', 'Inmigrantes', 'Refugiados', 'Población en general'])



# crear lista ratio para escoger el tono deseado, adaptado a streamlit. Que sea en dos columnas para que se vea mejor

tono_deseado = st.select_slider('Elige el tono deseado:', ['Serio', 'Respetuoso', 'Irreverente', 'Sarcástico', 'Inspiracional', 'Motivacional', 'Educativo', 'Desafiante', 'Optimista', 'Pesimista', 'Realista', 'Futurista', 'Conservador', 'Progresista', 'Radical', 'Moderado', 'Extremista', 'Centrista', 'Populista', 'Elitista', 'Incluyente', 'Excluyente', 'Tolerante', 'Intolerante', 'Pacífico', 'Beligerante', 'Conciliador', 'Confrontativo', 'Cooperativo', 'Competitivo', 'Solidario', 'Egoísta', 'Altruista', 'Individualista', 'Colectivista', 'Nacionalista', 'Internacionalista', 'Globalista', 'Localista', 'Regionalista', 'Universalista', 'Particularista', 'Pragmático', 'Idealista', 'Realista', 'Visionario', 'Oportunista', 'Conservador', 'Progresista', 'Reaccionario', 'Revolucionario', 'Reformista', 'Informal', 'Divertido'])




# Campo de texto para datos duros, opcional para el usuario
datos_duros = st.text_area('Datos duros a incluir en el discurso (opcional):')



# botón para generar el discurso político, vinculada a la funcionalidad de generador_discurso_politico
if st.button('Generar discurso político'):
    discurso = generador_discurso_politico(tipo_discurso, tema, publico_objetivo, tono_deseado, datos_duros=None)
    st.write(discurso)  # Mostrar el discurso generado en el sitio



    