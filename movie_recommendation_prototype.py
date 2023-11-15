import json
import math

# Definir preguntas y géneros
preguntas_generos = {
    "Pregunta1": {"pregunta": "1. ¿Disfrutas de escenas de lucha y persecuciones emocionantes en las películas?", "genero": "Accion"},
    "Pregunta2": {"pregunta": "2. ¿Te gustan las historias que involucran exploración y descubrimiento de lugares desconocidos?", "genero": "Aventura"},
    "Pregunta3": {"pregunta": "3. ¿Te interesa la tecnología futurista y los conceptos científicos en las películas?", "genero": "Ciencia"},
    "Pregunta4": {"pregunta": "4. ¿Prefieres películas que te hagan reír y alivien el estrés?", "genero": "Comedia"},
    "Pregunta5": {"pregunta": "5. ¿Te emocionan las historias profundas y emotivas sobre la vida y las relaciones?", "genero": "Drama"},
    "Pregunta6": {"pregunta": "6. ¿Disfrutas de mundos imaginarios, criaturas mágicas y elementos fantásticos?", "genero": "Fantasia"},
    "Pregunta7": {"pregunta": "7. ¿Te gusta la tensión y la intriga que se desarrolla a lo largo de una película?", "genero": "Suspenso"},
    "Pregunta8": {"pregunta": "8. ¿Te emociona la sensación de miedo y los elementos sobrenaturales en las películas?", "genero": "Terror"}
}

with open('movies.json', 'r') as file:
    movies_data = json.load(file)

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

def cosine_similarity(vec1, vec2):
    common_movies = set(vec1) & set(vec2)
    dot_product = sum(vec1[i] * vec2[i] for i in range(len(vec1)) if i in common_movies)
    magnitude_vec1 = math.sqrt(sum(val ** 2 for val in vec1))
    magnitude_vec2 = math.sqrt(sum(val ** 2 for val in vec2))
    return dot_product / (magnitude_vec1 * magnitude_vec2) if magnitude_vec1 != 0 and magnitude_vec2 != 0 else 0
    

def collaborative_filtering(user_ratings, all_ratings):
    similarities = {}
    for other_user, other_ratings in all_ratings.items():
        if other_user == user_ratings:
            continue
        #consinee_result = cosine_similarity(user_ratings, other_ratings)
        #print(consinee_result)
        #print(other_user)
        #print(user_ratings)
        similarities[other_user] = cosine_similarity(list(user_ratings.values()), list(other_ratings.values()))

    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_similarities)

    recommendations = {}
    for movie_id, rating in user_ratings.items():
        for other_user, similarity in sorted_similarities:
            if other_user in all_ratings and movie_id in all_ratings[other_user] and all_ratings[other_user][movie_id] > rating:
                recommendations[movie_id] = recommendations.get(movie_id, 0) + similarity * (all_ratings[other_user][movie_id] - rating)

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    result_movies = [movie_id for movie_id, score in sorted_recommendations]
    #print(result_movies)
    return result_movies

def generar_recomendaciones(respuestas_usuario, peliculas):
    # Obtener las puntuaciones del usuario
    user_ratings = {}
    #print(respuestas_usuario)
    #print(peliculas)
    for genre in respuestas_usuario:
        for movie in peliculas["peliculas"]:
            if genre in movie["genero"]:
                user_ratings[movie["id"]] = user_ratings.get(movie["id"], [])
                user_ratings[movie["id"]].append(movie["puntuaciones"]["usuario1"])  # Puedes ajustar el nombre del usuario según sea necesario

    # Aplicar el algoritmo de filtrado colaborativo
    result_moviess = {movie["id"]: {user: movie["puntuaciones"][user] for user in movie["puntuaciones"]} for movie in peliculas["peliculas"]}
    #print(result_moviess)
    recommendations = collaborative_filtering(user_ratings, result_moviess)
    #print(recommendations)
    # Obtener los títulos de las películas recomendadas
    recommended_movies = [movie["titulo"] for movie in peliculas["peliculas"] if movie["id"] in recommendations]

    return recommended_movies


print(f"\nResultado para el usuario: {nombre_usuario}!")

print(respuestas_usuario)
recomendaciones = generar_recomendaciones(respuestas_usuario, movies_data)
print("Géneros recomendados según tus respuestas:")
print(recomendaciones)