# Importar la función de similitud del coseno desde scipy
from scipy.spatial.distance import cosine
import json

# Definir preguntas y géneros
preguntas_generos = {
    "Pregunta1": {
        "pregunta": "1. ¿Disfrutas de escenas de lucha y persecuciones emocionantes en las películas?",
        "genero": "Accion"
        },
    "Pregunta2": {
        "pregunta": "2. ¿Te gustan las historias que involucran exploración y descubrimiento de lugares desconocidos?",
        "genero": "Aventura"
        },
    "Pregunta3": {
        "pregunta": "3. ¿Te interesa la tecnología futurista y los conceptos científicos en las películas?", 
        "genero": "Ciencia Ficcion"
        },
    "Pregunta4": {
        "pregunta": "4. ¿Prefieres películas que te hagan reír y alivien el estrés?",
        "genero": "Comedia"
        },
    "Pregunta5": {
        "pregunta": "5. ¿Te emocionan las historias profundas y emotivas sobre la vida y las relaciones?",
        "genero": "Drama"
        },
    "Pregunta6": {
        "pregunta": "6. ¿Disfrutas de mundos imaginarios, criaturas mágicas y elementos fantásticos?",
        "genero": "Fantasia"
        },
    "Pregunta7": {
        "pregunta": "7. ¿Te gusta la tensión y la intriga que se desarrolla a lo largo de una película?",
        "genero": "Suspenso"
        },
    "Pregunta8": {
        "pregunta": "8. ¿Te emociona la sensación de miedo y los elementos sobrenaturales en las películas?",
        "genero": "Terror"
        }
}

# Cargar las películas desde el archivo JSON
with open('new_movies.json', 'r') as file:
    movies = json.load(file)

# Inicializar diccionario para almacenar las respuestas
respuestas = {}
print("Prototipo: Sistema de recomendación de películas basado en gustos.\n")

# Definir función para obtener el nombre del usuario
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

# Solicitar respuestas a las preguntas y almacenarlas en respuestas
print(f"\nPor favor, {nombre_usuario}. Responde el siguiente cuestionario de 8 preguntas:")
print(f"Realiza la calificación segun tus gustos del 0 al 5, donde 0 significa nada agradable, 5 muy agradable:\n")

# Preguntar y registrar respuestas
for key, value in preguntas_generos.items():
    while True:
        respuesta = input(f"{value['pregunta']} : ")
        if respuesta.isdigit() and 0 <= int(respuesta) <= 5:
            respuestas[key] = int(respuesta)
            break
        else:
            print("Por favor, ingresa un número del 0 al 5.")

# Filtrar géneros según las respuestas con calificación > 4
respuestas_usuario = [value["genero"] for key, value in preguntas_generos.items() if respuestas[key] >= 4]

# Definir la función de similitud coseno entre dos vectores
def cosine_similarity(vec1, vec2):
    # Obtener las claves comunes entre los dos vectores
    common_keys = set(vec1.keys()) & set(vec2.keys())
    vec1_values = [vec1[key] for key in common_keys]
    vec2_values = [vec2[key] for key in common_keys]

    # Calcular la similitud del coseno usando scipy
    similarity = 1 - cosine(vec1_values, vec2_values)
    return similarity

# Definir la función de filtrado colaborativo
def collaborative_filtering(user_ratings, all_ratings):
    # Calcular las similitudes entre el usuario actual y otros usuarios
    similarities = {}
    for other_user, other_ratings in all_ratings.items():
        if other_user == user_ratings:
            continue
        similarities[other_user] = cosine_similarity(user_ratings, other_ratings)

    # Ordenar las similitudes en orden descendente
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    # Inicializar las recomendaciones
    recommendations = {}
    # Iterar sobre las películas y calcular las recomendaciones
    for movie_id, rating in user_ratings.items():
        for other_user, similarity in sorted_similarities:
            if other_user in all_ratings and movie_id in all_ratings[other_user] and all_ratings[other_user][movie_id] > rating:
                recommendations[movie_id] = recommendations.get(movie_id, 0) + similarity * (all_ratings[other_user][movie_id] - rating)

    # Ordenar las recomendaciones en orden descendente
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    # Devolver las películas recomendadas
    return [movie_id for movie_id, score in sorted_recommendations]

# Función para crear el diccionario de puntuaciones del usuario
def diccionario_puntuaciones(respuestas_usuario, movies):
    # Inicializar el diccionario de puntuaciones del usuario
    user_ratings = {}
    
    # Llenar el diccionario con las puntuaciones del usuario actual
    for genre in respuestas_usuario:
        for movie in movies:
            if genre == movie["genero"]:
                for user, rating in movie["puntuaciones"].items():
                    user_ratings[user] = user_ratings.get(user, {})
                    user_ratings[user][movie["titulo"]] = rating

    return user_ratings

# Crear el diccionario de puntuaciones del usuario
user_ratings = diccionario_puntuaciones(respuestas_usuario, movies)

# Crear un diccionario con todas las puntuaciones de todos los usuarios
all_ratings = {user: ratings for user, ratings in zip(user_ratings.keys(), user_ratings.values())}

# Imprimir géneros de películas preferidos para el usuario
print(f"\nGenero de peliculas preferidos para : {nombre_usuario}")
print(respuestas_usuario)

# Obtener y mostrar las recomendaciones
recomendaciones = collaborative_filtering(user_ratings["usuario1"], all_ratings)
# Imprimir las recomendaciones
print("\nPelículas recomendadas según tus respuestas:")
print(recomendaciones)