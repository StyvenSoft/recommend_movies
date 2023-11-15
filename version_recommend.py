import json

# Definir preguntas y géneros
preguntas_generos = {
    "Pregunta1": {"pregunta": "1. ¿Disfrutas de escenas de lucha y persecuciones emocionantes en las películas?", "genero": "Acción"},
    "Pregunta2": {"pregunta": "2. ¿Te gustan las historias que involucran exploración y descubrimiento de lugares desconocidos?", "genero": "Aventura"},
    "Pregunta3": {"pregunta": "3. ¿Te interesa la tecnología futurista y los conceptos científicos en las películas?", "genero": "Ciencia Ficción"},
    "Pregunta4": {"pregunta": "4. ¿Prefieres películas que te hagan reír y alivien el estrés?", "genero": "Comedia"},
    "Pregunta5": {"pregunta": "5. ¿Te emocionan las historias profundas y emotivas sobre la vida y las relaciones?", "genero": "Drama"},
    "Pregunta6": {"pregunta": "6. ¿Disfrutas de mundos imaginarios, criaturas mágicas y elementos fantásticos?", "genero": "Fantasía"},
    "Pregunta7": {"pregunta": "7. ¿Te gusta la tensión y la intriga que se desarrolla a lo largo de una película?", "genero": "Suspenso"},
    "Pregunta8": {"pregunta": "8. ¿Te emociona la sensación de miedo y los elementos sobrenaturales en las películas?", "genero": "Terror"}
}

def cargar_peliculas():
    # Estructura JSON de las películas
    movies_json = '''
    {
      "peliculas": [
        {
          "id": 1,
          "titulo": "Star Wars",
          "genero": ["Ciencia Ficción", "Aventura"],
          "puntuacion": 6
        },
        {
          "id": 2,
          "titulo": "The Matrix",
          "genero": ["Ciencia Ficción", "Acción"],
          "puntuacion": 4
        },
        {
          "id": 3,
          "titulo": "Inception",
          "genero": ["Comedia", "Acción"],
          "puntuacion": 8
        },
        {
          "id": 4,
          "titulo": "Iron Man",
          "genero": ["Ciencia Ficción", "Drama"],
          "puntuacion": 6
        },
        {
          "id": 5,
          "titulo": "Moonlight",
          "genero": ["Fantasía", "Acción"],
          "puntuacion": 5
        },
        {
          "id": 6,
          "titulo": "Salvad",
          "genero": ["Suspenso", "Drama"],
          "puntuacion": 7
        },
        {
          "id": 7,
          "titulo": "Fitzcarraldo",
          "genero": ["Aventura", "Comedia"],
          "puntuacion": 5
        },
        {
          "id": 8,
          "titulo": "Roma",
          "genero": ["Ciencia Ficción", "Terror"],
          "puntuacion": 3
        },
        {
          "id": 9,
          "titulo": "Colombia",
          "genero": ["Suspenso", "Drama"],
          "puntuacion": 4
        },
        {
          "id": 10,
          "titulo": "USA",
          "genero": ["Aventura", "Comedia"],
          "puntuacion": 4
        },
        {
          "id": 11,
          "titulo": "Francia",
          "genero": ["Ciencia Ficción", "Terror"],
          "puntuacion": 6
        }
      ]
    }
    '''

    # Cargar las películas desde el JSON
    return json.loads(movies_json)["peliculas"]

# Inicializar diccionario para almacenar las respuestas
respuestas = {}

def obtener_nombre_usuario():
    while True:
        nombre_usuario = input("Ingresa tu nombre: ").strip()  # Elimina espacios al inicio y al final

        # Validar si el nombre contiene solo letras
        if not nombre_usuario.isalpha():
            print("El nombre debe contener solo letras sin espacios. Por favor, inténtalo nuevamente.")
            continue

        return nombre_usuario

# Preguntar el nombre del usuario
nombre_usuario = obtener_nombre_usuario()

print(f"\nBienvenido, {nombre_usuario}! Responde un cuestionario de 8 preguntas:")

# Preguntar y registrar respuestas
for key, value in preguntas_generos.items():
    while True:
        respuesta = input(f"{value['pregunta']} (Calificación del 0 al 5): ")
        if respuesta.isdigit() and 0 <= int(respuesta) <= 5:
            respuestas[key] = int(respuesta)
            break
        else:
            print("Por favor, ingresa un número del 0 al 5.")

# Filtrar géneros según las respuestas con calificación 5
respuestas_usuario = [value["genero"] for key, value in preguntas_generos.items() if respuestas[key] == 5]

def generar_recomendaciones(respuestas_usuario, peliculas):
    # Filtrar películas según géneros seleccionados
    peliculas_filtradas = [p for p in peliculas if any(genero in p["genero"] for genero in respuestas_usuario)]

    # Ordenar películas por puntuación de mayor a menor
    peliculas_ordenadas = sorted(peliculas_filtradas, key=lambda x: x["puntuacion"], reverse=True)

    # Tomar las 5 primeras películas (o menos si hay menos de 5)
    recomendaciones = peliculas_ordenadas[:5]

    return [pelicula["titulo"] for pelicula in recomendaciones]


print(f"\nResultado para el usuario: {nombre_usuario}!")

print(respuestas_usuario)
peliculas = cargar_peliculas()
recomendaciones = generar_recomendaciones(respuestas_usuario, peliculas)
print("Películas recomendadas según tus respuestas:")
print(recomendaciones)