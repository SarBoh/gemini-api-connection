import os
from google import genai
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

if not clave_api:
    print("❌ Error: No se encontró la variable GEMINI_API_KEY en el archivo .env")
else:
    # Inicializar el cliente oficial de Gemini
    client = genai.Client(api_key=clave_api)

    def ejecutar_consulta():
        print("🛰️ Ejecutando consulta a Gemini...")
        try:
            respuesta = client.models.generate_content(
                model="gemini-2.5-flash",
                contents="Preséntate como experto en ML y responde de forma breve: ¿Cuáles son las mejores prácticas para entrenar un modelo?"
            )
            print("\n================ Respuesta de Gemini ================")
            print(respuesta.text)
            print("=====================================================")
        except Exception as e:
            print("❌ Error al ejecutar la consulta:", e)

    if __name__ == "__main__":
        ejecutar_consulta()