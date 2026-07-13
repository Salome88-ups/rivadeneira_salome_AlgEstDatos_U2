def registrar_libro(catalogo):
    codigo = input("Código del libro: ")

    if codigo in catalogo:
        print("Ese código ya existe.")
        return

    titulo = input("Título: ")
    autor = input("Autor: ")

    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor
    }

    print("Libro registrado correctamente.")


def buscar_libro(catalogo):
    codigo = input("Código a buscar: ")

    if codigo in catalogo:
        libro = catalogo[codigo]
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
    else:
        print("Libro no encontrado.")


def mostrar_catalogo(catalogo):
    if not catalogo:
        print("No existen libros.")
        return

    print("\nCATÁLOGO ORDENADO")

    for codigo in sorted(catalogo):
        libro = catalogo[codigo]
        print(f"{codigo} - {libro['titulo']} - {libro['autor']}")


def registrar_socio(socios):
    identificador = input("ID del socio: ")

    if identificador in socios:
        print("El socio ya está registrado.")
    else:
        socios.add(identificador)
        print("Socio registrado.")


def registrar_prestamo(socios, novela, ciencia):
    identificador = input("ID del socio: ")

    if identificador not in socios:
        print("El socio no existe.")
        return

    genero = input("Género (novela/ciencia): ").lower()

    if genero == "novela":
        novela.add(identificador)
        print("Préstamo registrado.")

    elif genero == "ciencia":
        ciencia.add(identificador)
        print("Préstamo registrado.")

    else:
        print("Género inválido.")


def analizar_prestamos(novela, ciencia):
    print("\nANÁLISIS")

    print("Socios que leen ambos géneros:")
    print(novela & ciencia)

    print("\nSolo novela:")
    print(novela - ciencia)

    print("\nTotal de socios distintos:")
    print(novela | ciencia)