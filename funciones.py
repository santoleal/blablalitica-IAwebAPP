import os
import dotenv
from openai import OpenAI



# Cargar variables de entorno
dotenv.load_dotenv(dotenv.find_dotenv())
dotenv.load_dotenv("./.env.py")

OpenAI_API_KEY = os.getenv('OPENAI_API_KEY')



client = OpenAI(api_key=OpenAI_API_KEY)


# Función para generar el discurso político. Que datos_duros sea opcional y que se pueda generar el discurso con o sin datos duros.

def generador_discurso_politico(tipo_discurso, tema, publico_objetivo, tono_deseado, datos_duros=None):
    prompt=f"Genera un discurso político del tipo: '{tipo_discurso}' sobre el tema: '{tema}', destinado a un público: {publico_objetivo}. Incluye un tono: '{tono_deseado}'. Si es que existen datos duros ingresados por el usuario ({datos_duros}), ingresarlos textualmente en la respuesta. No más de 150 palabras. Deben abundar signos exclamativos. La última frase debe ser un remate de la idea entregada."
    
    try:
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

        respuesta = response.choices[0].message.content

        if respuesta:
            respuesta = respuesta.split('.')
            respuesta = '. '.join(respuesta[:-1]) + '...'
            return respuesta
        
    except Exception as e:
        return f"Ocurrió un error: {e}"
    
    return respuesta
