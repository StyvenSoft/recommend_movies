import math

def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1[key] * vec2.get(key, 0) for key in vec1)
    magnitude_vec1 = math.sqrt(sum(val ** 2 for val in vec1.values()))
    magnitude_vec2 = math.sqrt(sum(val ** 2 for val in vec2.values()))
    return dot_product / (magnitude_vec1 * magnitude_vec2) if magnitude_vec1 * magnitude_vec2 != 0 else 0

def collaborative_filtering(user_ratings, all_ratings):
    similarities = {}
    for other_user, other_ratings in all_ratings.items():
        if other_user == user_ratings:
            continue
        similarities[other_user] = cosine_similarity(user_ratings, other_ratings)

    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    recommendations = {}
    for movie_id, rating in user_ratings.items():
        for other_user, similarity in sorted_similarities:
            if other_user in all_ratings and movie_id in all_ratings[other_user] and all_ratings[other_user][movie_id] > rating:
                recommendations[movie_id] = recommendations.get(movie_id, 0) + similarity * (all_ratings[other_user][movie_id] - rating)

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [movie_id for movie_id, score in sorted_recommendations]

# Ejemplo de uso
respuestas_usuario = ['Drama', 'Terror']

movies = [
    {
        "titulo": "Star Wars",
        "genero": "Ciencia",
        "puntuaciones": {
            "usuario1": 5,
            "usuario2": 4,
            "usuario3": 3
        }
    },
    {
        "titulo": "The Matrix",
        "genero": "Accion",
        "puntuaciones": {
            "usuario1": 4,
            "usuario2": 5,
            "usuario3": 3
        }
    },
    {
        "titulo": "Golden",
        "genero": "Accion",
        "puntuaciones": {
            "usuario1": 7,
            "usuario2": 8,
            "usuario3": 9
        }
    },
    {
        "titulo": "Momia",
        "genero": "Terror",
        "puntuaciones": {
            "usuario1": 1,
            "usuario2": 2,
            "usuario3": 1
        }
    },
    {
        "titulo": "Roja",
        "genero": "Terror",
        "puntuaciones": {
            "usuario1": 8,
            "usuario2": 9,
            "usuario3": 9
        }
    }
]

user_ratings = {}
for genre in respuestas_usuario:
    for movie in movies:
        if genre == movie["genero"]:
            for user, rating in movie["puntuaciones"].items():
                user_ratings[user] = user_ratings.get(user, {})
                user_ratings[user][movie["titulo"]] = rating

all_ratings = {user: ratings for user, ratings in zip(user_ratings.keys(), user_ratings.values())}

recomendaciones = collaborative_filtering(user_ratings["usuario1"], all_ratings)
print("Recomendaciones para el usuario:", recomendaciones)