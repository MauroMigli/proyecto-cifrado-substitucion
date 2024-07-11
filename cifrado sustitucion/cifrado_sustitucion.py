"""
Archivo encargado de crear el cifrado 
"""
from collections import Counter
import random 
import constantes as con 

class CifradoSustitucion:
    """
    Clase encargada de poder cifrar, entregar información y decifrar el texto
    """
    def __init__(self, ruta):
        # Se lee el archivo...
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

        # Si es que esta cifrado, entonces pasa a ser True 
        self.esta_cifrado = False
        # Contenido real del texto
        self.texto_secreto = "".join(data)
        # Contenido a cifrar del texto 
        self.texto = "".join(data)

    def cifrar(self):
        """
        Metodo encargado del cifrado del texto 
        """
        # Si es que no está cifrado...
        if not self.esta_cifrado:
            # En cifrado se guardará el texto a cifrar 
            cifrado = ""
            # Indices del abecedario nuevo
            indices = con.indices
            random.shuffle(indices)
            # Se genera el abecedario nuevo 
            self.abecedario_cifrado = {con.abecedario[i]: con.abecedario[indices[i]] for i in range(len(con.abecedario))}

            # Por cada caracter del texto a cifrar 
            for letra in self.texto:
                # Si es que pertenece al abecedario...
                if letra in con.abecedario:
                    # Se le asigna su transformación al nuevo abecedario
                    cifrado += con.abecedario[indices[con.indices_abecedario[letra]]]
                # En el caso contrario
                else:
                    # Se asigna el caracter tal cual
                    cifrado += letra

            # Se cambia el atributo self.texto y se levanta la flag para indicar que se encuentra cifrado
            self.texto = cifrado
            self.esta_cifrado = True
            print("Texto cifrado!:", self.texto)
        else:
            print("El texto ya está cifrado...")

    def informacion(self):
        # Frecuencias de una sola letra 
        frecuencias = dict(Counter(letra for letra in self.texto if letra in con.abecedario))
        largo = 0
        for i in self.texto:
            if i in con.abecedario:
                largo += 1
        for letra in con.abecedario:
            if letra in list(frecuencias.keys()):
                frecuencias[letra] = frecuencias[letra] / largo
            else:
                frecuencias[letra] = 0
        self.frecuencias = frecuencias

         # Se definen las frecuencias de 2-grams

        frecuencias_2 = dict(Counter(
            self.texto[i] + self.texto[i + 1] for i in range(len(self.texto) - 1) 
            if self.texto[i] in con.abecedario and self.texto[i + 1] in con.abecedario
            ))
        
        largo_2 = sum(frecuencias_2[llave] for llave in list(frecuencias_2.keys()))
        
        for llave in list(frecuencias_2.keys()):
            frecuencias_2[llave] = frecuencias_2[llave] / largo_2

        # Se definen las frecuencias de 3-grams

        frecuencias_3 = dict(Counter(
            self.texto[i] + self.texto[i + 1] + self.texto[i + 2] for i in range(len(self.texto) - 2) 
            if self.texto[i] in con.abecedario and self.texto[i + 1] in con.abecedario and self.texto[i + 2] in con.abecedario 
            ))
        
        largo_3 = sum(frecuencias_2[llave] for llave in list(frecuencias_3.keys()))

        for llave in list(frecuencias_3.keys()):
            frecuencias_3[llave] = frecuencias_3[llave] / largo_3

        # Se retorna una tupla de las frecuencias obtenidas para el analisis...
        return frecuencias, frecuencias_2, frecuencias_3
    

    def decifrar(self, abecedario):
        # Se decifra el codigo dado el abecedario
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

        print("texto nuevo:", self.texto)

        # Se revisan las fallas del abecedario con respecto al texto original
        contador_fallas = 0
        set_fallas = set()
        texto_final = ""
        for i in range(len(self.texto)):
            if self.texto_secreto[i] == decifrado[i]:
                texto_final += decifrado[i]
            else:
                if self.texto_secreto[i] not in set_fallas:
                    set_fallas.add(self.texto_secreto[i])
                    contador_fallas += 1
                    print("La letra", self.texto_secreto[i], "falla")
                texto_final += "_"
        print(texto_final)
        print("cantidad de errores", contador_fallas)

if __name__ == "__main__":
    instancia = CifradoSustitucion("text.txt")

    print(instancia.texto)
    instancia.cifrar()
    instancia.informacion()