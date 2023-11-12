import math

ratings = {
    'A': {'Star Wars': 5, 'The Matrix': 4, 'Inception': 5, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'B': {'Star Wars': 4, 'The Matrix': 4, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'C': {'Star Wars': 5, 'The Matrix': 3, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'D': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 5, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 4},
    'E': {'Star Wars': 3, 'The Matrix': 4, 'Inception': 5, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'F': {'Star Wars': 4, 'The Matrix': 4, 'Inception': 3, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 4, 'Acorralado': 5},
    'G': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 4, 'Moonlight': 3, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'H': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'I': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 4},
    'J': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 2, 'exorcista': 3, 'Acorralado': 5},
    'K': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'L': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 5, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 5, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'M': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 3, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'N': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 4},
    'O': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 4, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'P': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 3, 'Iron Man': 4, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 3, 'Selma': 5, 'exorcista': 3, 'Acorralado': 5},
    'Q': {'Star Wars': 5, 'The Matrix': 5, 'Inception': 4, 'Iron Man': 5, 'Moonlight': 5, 'Salvad': 5, 'Fitzcarraldo': 5, 'Roma': 4, 'Selma': 3, 'exorcista': 3, 'Acorralado': 5},
}

# Cálculo de similitud

def similarity(user1, user2):
    common_movies = set(ratings[user1].keys()) & set(ratings[user2].keys())
    #print(common_movies)
    if not common_movies:
        return 0  # Sin películas en común
    sum_sq_diff = sum((ratings[user1][movie] - ratings[user2][movie]) ** 2 for movie in common_movies)
    #print(sum_sq_diff)
    similarity_score = (1 / (1 + math.sqrt(sum_sq_diff))) * 100
    #print(result_similitud)
    return round(similarity_score, 1)  # Coeficiente de similitud en porcentaje

# Recomendación

def recommend_movies(user):
    totals = {}
    sim_sums = {}
    for other_user in ratings:
        if other_user == user:
            continue
        sim = similarity(user, other_user)
        #print(sim)
        print(f"Similitud entre {user} y {other_user}: {sim}")
        if sim <= 0:
            continue
        for movie in ratings[other_user]:
            if movie not in ratings[user] or ratings[user][movie] == 0:
                totals.setdefault(movie, 0)
                totals[movie] += ratings[other_user][movie] * sim
                sim_sums.setdefault(movie, 0)
                sim_sums[movie] += sim

    print("Totales:", totals)
    print("Sim Sums:", sim_sums)
    rankings = [(total / sim_sums[movie], movie) for movie, total in totals.items()]
    rankings.sort(reverse=True)
    recommendations = [movie for score, movie in rankings]
    return recommendations

# Ejemplo de uso
user_A_recommendations = recommend_movies('A')
print("AARecomendaciones para el usuario A:", user_A_recommendations)
