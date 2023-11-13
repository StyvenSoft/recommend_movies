
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
print(f"Bienvenido, {nombre_usuario}!")