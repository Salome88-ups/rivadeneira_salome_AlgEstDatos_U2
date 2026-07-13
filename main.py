while True:

    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Mostrar catálogo")
    print("4. Registrar socio")
    print("5. Registrar préstamo")
    print("6. Analizar préstamos")
    print("7. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        registrar_libro()

    elif opcion == "2":
        buscar_libro()

    elif opcion == "3":
        mostrar_catalogo()

    elif opcion == "4":
        registrar_socio()

    elif opcion == "5":
        registrar_prestamo()

    elif opcion == "6":
        analizar_prestamos()

    elif opcion == "7":
        break