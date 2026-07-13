from utilidades import *

# Diccionario del catálogo
catalogo = {}

# Conjunto de socios
socios = set()

# Conjuntos para préstamos
prestamos_novela = set()
prestamos_ciencia = set()


while True:
    print("\n====== BIBLIOTECA ======")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Mostrar catálogo ordenado")
    print("4. Registrar socio")
    print("5. Registrar préstamo")
    print("6. Analizar préstamos")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_libro(catalogo)

    elif opcion == "2":
        buscar_libro(catalogo)

    elif opcion == "3":
        mostrar_catalogo(catalogo)

    elif opcion == "4":
        registrar_socio(socios)

    elif opcion == "5":
        registrar_prestamo(socios, prestamos_novela, prestamos_ciencia)

    elif opcion == "6":
        analizar_prestamos(prestamos_novela, prestamos_ciencia)

    elif opcion == "7":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida.")
