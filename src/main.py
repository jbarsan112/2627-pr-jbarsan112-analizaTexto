def analizar_texto(frase: str) -> tup[int, int]:
    """
    Analiza las vocales y palabras de una frase.
    :param: str frase = Frase del usuario.
    :return: tupla[numero_vocales, numero_palabras]
    """

    frase_minuscula = frase.lower()
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]
    contador_vocales = 0
    for letra in frase_minuscula:
        if letra in vocales:
            contador_vocales += 1

    contador_palabras = len(frase.split())

    return (contador_vocales, contador_palabras)

def main():
    """Funcion principal."""
    frase: str = input("Escribe una frase: ")

    #Llamar a la funcion
    texto_analizado = analizar_texto(frase)

    print(frase)
    print(f"Vocales: {texto_analizado[0]}")
    print(f"Palabras: {texto_analizado[1]}")
    

if __name__ == "__main__":
    main()