from openai import OpenAI
import dotenv
import os


# Cargar variables de entorno
dotenv.load_dotenv()
OpenAi_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key="OpenAi_API_KEY")

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

