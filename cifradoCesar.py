import string
from random import randint

# Función de cifrado César
def caesarCipher(n, texto, alfabeto):
    size = len(alfabeto)
    cifrado = {} 
    for i in range(size):
        cifrado[alfabeto[i]] = alfabeto[(i + n) % size]

    encriptado = ''.join([cifrado.get(char, char) for char in texto])
    return encriptado, cifrado

alfabeto = string.ascii_uppercase + 'ÁÉÍÑÓÚ'
sizeAlph = len(alfabeto)

texto = "En el criptoanálisis, la técnica de análisis de frecuencias consiste en el aprovechamiento de estudios sobre la frecuencia de las letras o grupos de letras en los idiomas para poder establecer hipótesis para aprovecharlas para poder descifrar un texto cifrado sin tener la clave de descifrado (romper). Es un método típico para romper cifrados clásicos."
texto = texto.upper()

n = randint(1, sizeAlph)
textoCifrado, dictCifrado = caesarCipher(n, texto, alfabeto)

print("\nTexto cifrado:")
print(textoCifrado)

# Brute force attack!
print("\nDecifrado usando ataque de fuerza bruta:")
for i in range(1, sizeAlph):
    # Obtenemos el cifrado inverso y lo aplicamos para cada i.
    _, dictCifradoInverso = caesarCipher(i, textoCifrado, alfabeto) 
    textoDecifrado = ''.join([dictCifradoInverso.get(char, char) for char in textoCifrado])
    print(f"n = {i}: \n{textoDecifrado}")