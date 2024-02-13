import streamlit as st
from funciones import generador_discurso_politico




# Cabecera de sitio en streamlit
st.title('Generador de discursos políticos')

st.subheader('Completa los siguientes campos para generar un discurso político. El discurso será de 100 palabras como máximo.')



st.write("###")

# Columnas para organizar el sitio
left_col, right_col = st.columns(2)


st.write("###")
# Campos a rellenar por el usuario, adaptados a streamlit
with left_col:
    tema = st.text_input('Tema central a tratar:', max_chars=30)


with right_col:
    # crear lista de tipo discursos para mostrar en un select, adaptado a streamlit
    tipo_discurso = st.selectbox('Elige el tipo de discurso:', ['Informativo', 'Propagandístico', 'Motivacional', 'Argumentativo'])


st.write("###")

#crear selección múltiple de público objetivo a partir de una lista de opciones, adaptado a streamlit
publico_objetivo = st.multiselect('Elige el público objetivo (pueden ser varias opciones):', ['Jóvenes', 'Adultos', 'Adultos mayores', 'Mujeres', 'Hombres', 'Niños', 'Niñas', 'Empresarios', 'Trabajadores', 'Estudiantes', 'Profesionales', 'Desempleados', 'Inmigrantes', 'Refugiados', 'Población en general'])

st.write("###")

# crear lista ratio para escoger el tono deseado, adaptado a streamlit. Que sea en dos columnas para que se vea mejor

tono_deseado = st.select_slider('Elige el tono deseado (opciones por orden alfabético):', ['Altruista', 'Beligerante', 'Competitivo', 'Conciliador', 'Confrontativo', 'Conservador', 'Cooperativo', 'Colectivista', 'Desafiante', 'Divertido', 'Educativo', 'Egoísta', 'Extremista', 'Futurista', 'Globalista', 'Idealista', 'Individualista', 'Informal', 'Intolerante', 'Internacionalista', 'Irreverente', 'Localista', 'Moderado', 'Motivacional', 'Nacionalista', 'Oportunista', 'Optimista', 'Pacífico', 'Pesimista', 'Populista', 'Pragmático', 'Progresista', 'Radical', 'Realista', 'Reaccionario', 'Reformista', 'Regionalista', 'Respetuoso', 'Revolucionario', 'Sarcástico', 'Serio', 'Solidario', 'Tolerante', 'Universalista', 'Visionario'])


st.write("###")

# Campo de texto para datos duros, opcional para el usuario
datos_duros = st.text_area('Datos duros a incluir en el discurso (opcional):', max_chars=80)

st.write("###")

# botón para generar el discurso político, vinculada a la funcionalidad de generador_discurso_politico
if st.button('Generar discurso político'):
    discurso = generador_discurso_politico(tipo_discurso, tema, publico_objetivo, tono_deseado, datos_duros)
    st.write(discurso)  # Mostrar el discurso generado en el sitio



    