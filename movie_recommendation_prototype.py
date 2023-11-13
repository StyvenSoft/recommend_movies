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

# Ejemplo de uso
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
generos_recomendados = [value["genero"] for key, value in preguntas_generos.items() if respuestas[key] == 5]

print(f"\nBienvenido, {nombre_usuario}!")
print("Géneros recomendados según tus respuestas:")
print(generos_recomendados)