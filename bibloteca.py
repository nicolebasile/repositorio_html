import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    for libro in libros:
        cod = libro["cod"]
        cant_ej_ad = libro["cant_ej_ad"]
        cant_ej_pr = libro["cant_ej_pr"]
        titulo = libro["titulo"]
        autor = libro["autor"]

        if cant_ej_pr == 1:
            print(f"{titulo} de {autor} tiene {cant_ej_pr} ejemplar prestado")
        elif cant_ej_pr > 1:
            print(f"{titulo} de {autor} tiene {cant_ej_pr} ejemplares prestados")
        else:
            print(f"{titulo} de {autor} no tiene ejemplares prestados")

            
def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    #completar
    return None

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None