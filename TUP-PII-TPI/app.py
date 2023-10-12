# Trabajo Práctico I - Programación II
#Integrantes: Thiago Campagnaro - Francesco Dagostino. 

import os
from bibloteca import generar_devolucion, gestionar_prestamo, eliminar_ejemplar_libro, mostrar_ejemplares_prestados, registrar_nuevo_libro

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\nIngrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            gestionar_prestamo()
        elif int(opt) == 2:
            generar_devolucion()
        elif int(opt) == 3:
            registrar_nuevo_libro()
        elif int(opt) == 4:
            eliminar_ejemplar_libro()
        elif int(opt) == 5:
            mostrar_ejemplares_prestados()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print()
    input("Presione cualquier tecla para continuar....\n") # Pausa
    
    print("Hasta luego!.")
    