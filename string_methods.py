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
    lineaUno = str(multilinea[0:7])
    lineaDos = str(multilinea[12:19])
    lineaTres = str(multilinea[24:32])

    print("Strip: ", nombre.strip())
    print("Lstrip: ", nombre.lstrip())
    print("Rstrip", nombre.rstrip())
    print("Upper: ", frase.upper())
    print("Lower: ", frase.lower())
    print("Title: ", frase.title())
    print("Find: ", frase.find("gran"))
    print("Replace: ", frase.replace("programacion", "desarrollo"))
    print("count: ", frase.count("a"))
    print("Contiene Python: ", "Python" in frase)
    print("Contiene Java: ", "java" in frase)
    print("Slice: ", frase[0:6])
    print("Paso: ", "Python"[0::2])
    print("Reverso: ", "Python"[::-1])
    print(f"Formato:{nombre}sabe Python")
    print(lineaUno)
    print(lineaDos)
    print(lineaTres)

string_methods()
