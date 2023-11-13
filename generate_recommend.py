import json

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

def generar_recomendaciones(respuestas_usuario, peliculas):
    # Filtrar películas según géneros seleccionados
    peliculas_filtradas = [p for p in peliculas if any(genero in p["genero"] for genero in respuestas_usuario)]

    # Ordenar películas por puntuación de mayor a menor
    peliculas_ordenadas = sorted(peliculas_filtradas, key=lambda x: x["puntuacion"], reverse=True)

    # Tomar las 5 primeras películas (o menos si hay menos de 5)
    recomendaciones = peliculas_ordenadas[:5]

    return [pelicula["titulo"] for pelicula in recomendaciones]

# Ejemplo de uso
respuestas_usuario = ['Aventura', 'Drama', 'Terror']
peliculas = cargar_peliculas()
recomendaciones = generar_recomendaciones(respuestas_usuario, peliculas)

print("Recomendaciones para el usuario:")
print(recomendaciones)