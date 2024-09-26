import os  # Importa el módulo os para trabajar con archivos y rutas
import json  # Importa el módulo json para trabajar con archivos en formato JSON
import re  # Importa el módulo re para trabajar con expresiones regulares

# Nombre del archivo que se usará como base de datos para guardar el conocimiento
DB_FILE = "conocimiento.json"

# Función para cargar el conocimiento desde el archivo JSON
def cargar_conocimiento():
    conocimiento = {}  # Diccionario para almacenar las preguntas y respuestas
    if os.path.exists(DB_FILE):  # Verifica si el archivo existe
        # Si existe, abre el archivo en modo lectura
        with open(DB_FILE, 'r', encoding='utf-8') as file:
            # Carga el contenido del archivo en el diccionario 'conocimiento'
            conocimiento = json.load(file)
    else:
        # Si el archivo no existe, inicializa el conocimiento con datos predeterminados
        conocimiento = {
            "Hola": "Hola! ¿Cómo estás?",
            "Como estas": "Estoy bien, gracias. ¿Y tú?",
            "De que te gustaria hablar": "Podemos hablar de lo que quieras."
        }
        # Guarda el conocimiento predeterminado en el archivo
        guardar_conocimiento(conocimiento)
    return conocimiento  # Retorna el diccionario de conocimiento cargado

# Función para guardar el conocimiento en el archivo JSON
def guardar_conocimiento(conocimiento):
    # Abre el archivo en modo escritura (crea el archivo si no existe)
    with open(DB_FILE, 'w', encoding='utf-8') as file:
        # Guarda el contenido del diccionario 'conocimiento' en formato JSON
        json.dump(conocimiento, file, ensure_ascii=False, indent=4)

# Función para validar y limpiar la entrada del usuario
def limpiar_texto(texto):
    # Elimina caracteres no permitidos (solo deja letras, números y espacios)
    return re.sub(r'[^A-Za-z0-9 ]+', '', texto)

# Función para añadir una nueva pregunta-respuesta al conocimiento
def agregar_conocimiento(pregunta, respuesta, conocimiento):
    # Limpia las entradas de pregunta y respuesta
    pregunta = limpiar_texto(pregunta)
    respuesta = limpia
