import matplotlib.pyplot as plt
import cifrado_sustitucion as cifrado_1
import constantes as con 

def orden(valor):
    return -1 * valor[1]


instancia = cifrado_1.CifradoSustitucion("text.txt")
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

# Abecedario a generar 
abecedario_nuevo = ["" for _ in range(26)]

# Lista del abecedario
abecedario = [x for x in "abcdefghijklmnopqrstuvwxyz"]
# Frecuencias del texto cifrado ordenadas de menor a mayor 
frecuencias_texto = [x[0] for x in sorted(list(instancia.informacion()[0].items()), key = orden)]
# Frecuencias de una sola letra ordenadas de menor a mayor 
frecuencias_normal = [x[0] for x in sorted(list(con.frecuenciasIngles.items()), key = orden)]

# Se entrega los pares correspondientes de letra cifrada y letra normal
comprimido = list(zip(frecuencias_normal, frecuencias_texto))

# frecuencias_texto = [x[0] for x in sorted(list(instancia.informacion()[0].items()), key = orden)]
# # Frecuencias de una sola letra ordenadas de menor a mayor 
# frecuencias_normal = [x[0] for x in sorted(list(con.frecuenciasIngles.items()), key = orden)]

# Frecuencias del texto cifrado ordenadas de menor a mayor
frecuencias_texto = [x[0] for x in sorted(list(instancia.informacion()[1].items()), key = orden)]
# Frecuencias de una sola letra ordenadas de menor a mayor
frecuencias_normal = [x[0] for x in sorted(list(con.frecuencias_2.items()), key = orden)]

# Se entrega los pares correspondientes de letra cifrada y letra normal
comprimido2 = list(zip(frecuencias_normal, frecuencias_texto))

# Frecuencias del texto cifrado ordenadas de menor a mayor
frecuencias_texto = [x[0] for x in sorted(list(instancia.informacion()[2].items()), key = orden)]
# Frecuencias de una sola letra ordenadas de menor a mayor
frecuencias_normal = [x[0] for x in sorted(list(con.frecuencias_3.items()), key = orden)]

# Se entrega los pares correspondientes de letra cifrada y letra normal
comprimido3 = list(zip(frecuencias_normal, frecuencias_texto))

print(comprimido3)

iteraciones = 10
unigramas_escogidos = 0  # 26
bigramas_escogidos = 0  # 15
trigramas_escogidos = 0  # 11
indices_cifrados_1 = list(range(26))
indices_cifrados_2 = list(range(15))
indices_cifrados_3 = list(range(11))

for i in range(iteraciones):
    if unigramas_escogidos < 26:
        original_1 = comprimido[i][0]
        cifrado_1 = comprimido[indices_cifrados_1[i]][1]  # Una letra cifrada

        if cifrado_1 in abecedario_nuevo:
            if i + 1 <= 25:
                # swap los índices posterior con este
                temp = indices_cifrados_1[i]
                indices_cifrados_1[i] = indices_cifrados_1[i + 1]
                indices_cifrados_1[i + 1] = temp
        else:
            unigramas_escogidos += 1
            for pos, letra in enumerate(abecedario):
                if letra == original_1:
                    abecedario_nuevo[pos] = cifrado_1
                    break

    if bigramas_escogidos < 15:
        original_2 = comprimido2[i][0]
        cifrado_2 = comprimido2[indices_cifrados_2[i]][1]
        letra1 = cifrado_2[0]
        letra2 = cifrado_2[1]

        if (letra1 in abecedario_nuevo) or (letra2 in abecedario_nuevo):
            if i + 1 <= 25:
                temp = indices_cifrados_2[i]
                indices_cifrados_2[i] = indices_cifrados_2[i + 1]
                indices_cifrados_2[i + 1] = temp
        else:
            bigramas_escogidos += 1
            for pos, letra in enumerate(abecedario):
                letra1, letra2 = cifrado_2
                if letra == letra1:
                    abecedario_nuevo[pos] = letra1
                if letra == letra2:
                    abecedario_nuevo[pos] = letra2

    if trigramas_escogidos < 11:
        original_3 = comprimido3[i][0]
        cifrado_3 = comprimido3[indices_cifrados_3[i]][1]
        letra1 = cifrado_3[0]
        letra2 = cifrado_3[1]
        letra3 = cifrado_3[2]

        if (letra1 in abecedario_nuevo) or (letra2 in abecedario_nuevo) or (letra3 in abecedario_nuevo):
            if i + 1 <= 25:
                temp = indices_cifrados_3[i]
                indices_cifrados_3[i] = indices_cifrados_3[i + 1]
                indices_cifrados_3[i + 1] = temp
        else:
            trigramas_escogidos += 1
            for pos, letra in enumerate(abecedario):
                letra1, letra2, letra3 = cifrado_3
                if letra == letra1:
                    abecedario_nuevo[pos] = letra1
                if letra == letra2:
                    abecedario_nuevo[pos] = letra2
                if letra == letra3:
                    abecedario_nuevo[pos] = letra3

print(abecedario_nuevo)



# # Por cada tupla se empieza a generar el nuevo abecedario en la variable abecedario_nuevo
# for tupla in comprimido:
#     posicion = 0
#     for i in range(len(con.abecedario)):
#         if con.abecedario[i] == tupla[0]:
#             posicion = i
#
#     abecedario_nuevo[posicion] = tupla[1]
#
# print(abecedario_nuevo)
#
# # Se decifra
# instancia.decifrar("".join(abecedario_nuevo))
# # lista de todos los posibles bigramas y frecuencias
# alfabeto = 'abcdefghijklmnopqrstuvwxyz'
# bigrama = {}
# for primera_letra in alfabeto:
#     for segunda_letra in alfabeto:
#         letra = primera_letra + segunda_letra
#         bigrama[letra] = 0
#
# # Se revisa los bigramas posibles dentro del texto
# textocifrado =  instancia.texto
# cantidaddebigramas = 0
# for i in range(len(textocifrado)-1):
#     palabra = textocifrado[i]+textocifrado[i+1]
#     if palabra in bigrama:
#         bigrama[palabra] += 1
#         cantidaddebigramas += 1
# for i in bigrama:
#     bigrama[i] = bigrama[i]/cantidaddebigramas
# bigrama = sorted(bigrama.items(), key=lambda kv: kv[1],reverse= True)
# bigrama = bigrama[:11]
#
# #Frecuencia del trigrama en la palabra cifrada
# trigrama = {}
# for primera_letra in alfabeto:
#     for segunda_letra in alfabeto:
#         for tercera_letra in alfabeto:
#             letra = primera_letra + segunda_letra + tercera_letra
#             trigrama[letra] = 0
#
# # Se revisa los trigramas posibles dentro del texto cifrado
# cantidaddetrigrama = 0
#
# for i in range(len(textocifrado)-2):
#     palabra = textocifrado[i]+textocifrado[i+1] + textocifrado[i+2]
#     if palabra in trigrama:
#         trigrama[palabra] += 1
#         cantidaddetrigrama += 1
# for i in trigrama:
#     trigrama[i] = trigrama[i]/cantidaddebigramas
# trigrama = sorted(trigrama.items(), key=lambda kv: kv[1],reverse= True)
# trigrama = trigrama[:11]
#
