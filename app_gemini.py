import os
from google import genai

def conectar_gemini():
    # Buscamos la API key en las variables de entorno por seguridad
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: La variable de entorno GEMINI_API_KEY no está configurada.")
        return

    try:
        # Inicializamos el cliente
        client = genai.Client(api_key=api_key)
        
        # Hacemos una petición simple de prueba usando el modelo flash
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents='Genera un mensaje corto que diga: "¡Conexión exitosa con la API de Gemini!"',
        )
        
        
    except Exception as e:
        print(f" Ocurrió un error al conectar con la API: {e}")

if __name__ == "__main__":
    conectar_gemini()