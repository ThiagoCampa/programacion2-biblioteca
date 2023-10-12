from cod_generator import generar
# Crear un diccionario para cada libro

libro1 = {'cod': '101', 'cant_ej_ad': 7, 'cant_ej_pr': 4, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': '102', 'cant_ej_ad': 9, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': '103', 'cant_ej_ad': 5, 'cant_ej_pr': 1, "titulo": "El código Da Vinci", "autor": "Dan Brown"}


#No utilizamos esta funcion, 
#y la reemplazamos por la funcion de registrar_nuevo_libro() dentro del archivo biblioteca.py

"""def nuevo_libro(libros): 
    codigo = generar(libros)
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares disponibles: "))
    cant_ej_pr = int(input("Ingrese la cantidad de ejemplares prestados: "))
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")

    libro = {
        'cod': codigo,
        'cant_ej_ad': cant_ej_ad,
        'cant_ej_pr': cant_ej_pr,
        'titulo': titulo,
        'autor': autor
    }
    
    libros.append(libro)
    
    print(f'El libro "{titulo}" ha sido agregado exitosamente.')
    return None"""

"""def generar_codigo():
    #completar
    return None""" 
    #No usamos esta funcion, 
    #ya que utilizamos la que viene por defecto en el archivo cod_generator.py