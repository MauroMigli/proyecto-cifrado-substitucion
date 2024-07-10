"""
Archivo encargado de crear el cifrado 
"""
from collections import Counter
import random 
import constantes as con 

class CifradoSustitucion:
    def __init__(self, ruta):
        archivo = open(ruta,encoding="utf-8")
        data = archivo.readlines()
        archivo.close()

        for i in range(len(data)):
            data[i] = data[i].replace("\n", " ")
            data[i] = data[i].lower()
            data[i] = data[i].replace("á", "a")
            data[i] = data[i].replace("é", "e")
            data[i] = data[i].replace("í", "i")
            data[i] = data[i].replace("ó", "o")
            data[i] = data[i].replace("ú", "u")

        self.esta_cifrado = False
        
        self.texto = "".join(data)

    def cifrar(self):
        if not self.esta_cifrado:
            cifrado = ""
            indices = con.indices
            random.shuffle(indices)

            for letra in self.texto:
                if letra in con.abecedario:
                    cifrado += con.abecedario[indices[con.indices_abecedario[letra]]]
                else:
                    cifrado += letra

            self.texto = cifrado
            self.esta_cifrado = True
            print("Texto cifrado!:", self.texto)
        else:
            print("El texto ya está cifrado...")

    def informacion(self):
        frecuencias = dict(Counter(letra for letra in self.texto if letra != " " and letra != "." and letra != ","))
        largo = len(self.texto.replace(" ", ""))
        print("Aqui van las frecuencias...")
        for letra in con.abecedario:
            frecuencias[letra] = frecuencias[letra] / largo
            print(frecuencias[letra])
        
        return frecuencias
    

    def decifrar(self, abecedario):
        decifrado = ""
        for letra in self.texto:
            if letra in con.abecedario:
                contador = 0
                for i in range(len(abecedario)):
                    if abecedario[i] == letra:
                        contador = i
                decifrado += con.abecedario[contador]
            else:
                decifrado += letra

        self.texto = decifrado
        print("texto nuevo:", self.texto)

if __name__ == "__main__":
    instancia = CifradoSustitucion("cifrado sustitucion/text.txt")

    print(instancia.texto)
    instancia.cifrar()
    instancia.decifrar()