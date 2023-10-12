import libro as l
from cod_generator import generar

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def gestionar_prestamo():#Funcion 1
    codigo = input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo:
            if libro['cant_ej_ad'] - libro['cant_ej_pr'] <= 0:
                print("No quedan ejemplares disponibles para prestar.\n")
            else:
                print(f"Autor: {libro['autor']}")
                print(f"Título: {libro['titulo']}")
                print(f"Ejemplares disponibles: {libro['cant_ej_ad'] - libro['cant_ej_pr']}")
                confirmar = input("¿Desea confirmar el préstamo? (S/N): \n")
                if confirmar.lower() == "s": #Devuelve los caracteres de las cadenas en minuscula
                    libro['cant_ej_pr'] += 1
                    print("Préstamo confirmado. Disfrute su lectura.\n")
            return
    print("El libro no existe.\n")

def generar_devolucion():#funcion 2
    codigo = input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo:
            if libro['cant_ej_pr'] <= 0:
                print("No hay ejemplares prestados de este libro.\n")
            else:
                print(f"Autor: {libro['autor']}")
                print(f"Título: {libro['titulo']}")
                confirmar = input("¿Desea confirmar la devolución? (S/N): \n")
                if confirmar.lower() == "s": #Devuelve los caracteres de las cadenas en minuscula
                    libro['cant_ej_pr'] -= 1
                    print("Devolución confirmada. Gracias por devolver el libro.\n")
            return
    print("El libro no existe o no tiene ejemplares prestados.\n")
                
def registrar_nuevo_libro(): #funcion 3
    codigo = generar()
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: \n"))
    cant_ej_pr = 0  # Inicialmente, no hay ejemplares prestados

    libro = {
        'cod': codigo,
        'titulo': titulo,
        'autor': autor,
        'cant_ej_ad': cant_ej_ad,
        'cant_ej_pr': cant_ej_pr
    }

    libros.append(libro)
    print(f"Libro registrado con éxito. Código del libro: {codigo}\n")

def eliminar_ejemplar_libro(): #funcion 4
    codigo = input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo:
            cant_ej_ad = libro['cant_ej_ad']
            if cant_ej_ad > 0:
                cant_ej_ad -= 1
                libro['cant_ej_ad'] = cant_ej_ad
                print("Ejemplar eliminado exitosamente.\n")
            else:
                print("No hay ejemplares disponibles para eliminar.\n")
            return
    print("El libro no existe.\n")

def mostrar_ejemplares_prestados(): #funcion 5
    print("\nEjemplares prestados:\n")
    for libro in libros:
        if libro['cant_ej_pr'] > 0:
            print(f"Título: {libro['titulo']}")
            print(f"Ejemplares prestados: {libro['cant_ej_pr']}\n")
        if  libro['cant_ej_pr'] == 0:
            print("Estos libros no cuentan con ejemplares prestados:")
            print(f"Título: {libro['titulo']}")
            print(f"Ejemplares prestados: {libro['cant_ej_pr']}\n")