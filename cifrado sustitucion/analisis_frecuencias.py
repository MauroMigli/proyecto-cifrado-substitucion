import matplotlib.pyplot as plt
import cifrado_sustitucion as cifrado
import constantes as con 

def orden(valor):
    return valor[1]


instancia = cifrado.CifradoSustitucion("cifrado sustitucion/text.txt")
instancia.cifrar()
# instancia.decifrar()
instancia.informacion()

# letras = list(instancia.frecuencias.keys())
# frecuencia = list(instancia.frecuencias.values())
# letrasFrecuencia = list(zip(letras, frecuencia))
# letrasFrecuencia.sort(key=lambda x: -x[1])

# print(letrasFrecuencia)

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.bar([x[0] for x in letrasFrecuencia], [x[1] for x in letrasFrecuencia], color='skyblue')

# # Adding title and labels
# plt.title('Counter Data Plot')
# plt.xlabel('Labels')
# plt.ylabel('Counts')

# # Display the plot
# plt.show()

abecedario_nuevo = ["" for _ in range(26)]

abecedario = [x for x in "abcdefghijklmnopqrstuvwxyz"]
frecuencias_texto = [x[0] for x in sorted(list(instancia.informacion().items()), key = orden)]
frecuencias_normal = [x[0] for x in sorted(list(con.frecuenciasIngles.items()), key = orden)]

comprimido = list(zip(frecuencias_normal, frecuencias_texto))
print(comprimido)

for tupla in comprimido:
    posicion = 0
    for i in range(len(con.abecedario)):
        if con.abecedario[i] == tupla[0]:
            posicion = i

    abecedario_nuevo[posicion] = tupla[1]

print(abecedario_nuevo)

instancia.decifrar("".join(abecedario_nuevo))
# lista de todos los posibles bigramas
bigramas = [x+y for x in "abcdefghijklmnopqrstuvwxyz" for y in "abcdefghijklmnopqrstuvwxyz"]




