def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    # 1. strip, lstrip, rstrip
    print("Strip:", nombre.strip())
    print("Lstrip:", nombre.lstrip())
    print("Rstrip:", nombre.rstrip())

    # 2. upper, lower, title
    print("Upper:", frase.upper())
    print("Lower:", frase.lower())
    print("Title:", frase.title())

    # 3. find
    print("Find:", frase.find("gran"))

    # 4. replace
    print("Replace:", frase.replace("programacion", "desarrollo"))

    # 5. count
    print("Count:", frase.count("a"))

    # 6. operador in
    print("Contiene Python:", "Python" in frase)
    print("Contiene Java:", "Java" in frase)

    # 7. slicing
    print("Slice:", frase[:6])

    # 8. slicing con paso
    print("Paso:", "Python"[::2])

    # 9. reverso
    print("Reverso:", "Python"[::-1])

    # 10. f-string
    print("Formato:", f"{nombre.strip()} sabe Python")

    # 11. multilinea (CORREGIDO para evitar espacios ocultos)
    for linea in multilinea.splitlines():
        print(linea.strip())

