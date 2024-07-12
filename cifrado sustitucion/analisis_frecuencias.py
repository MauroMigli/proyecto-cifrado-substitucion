import matplotlib.pyplot as plt
import cifrado_sustitucion as cifrado_1
import constantes as con

def orden(valor):
    return -1 * valor[1]

def agregar_letras(abecedario, letras_or, letras_cif, abecedario_nuevo, n):
    if n == 1:
        for pos, letra in enumerate(abecedario):
            if letra == letras_or:
                abecedario_nuevo[pos] = letras_cif
                break
    elif n == 2:
        listas = 0
        for pos, letra in enumerate(abecedario):
            if letra == letras_or[0]:
                abecedario_nuevo[pos] = letras_cif[0]
                listas += 1
            if letra == letras_or[1]:
                abecedario_nuevo[pos] = letras_cif[1]
                listas += 1
            if listas == 2:
                break


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
frecuencias_texto = [x for x in sorted(list(instancia.informacion()[0].items()), key = orden)]
# Frecuencias de una sola letra ordenadas de menor a mayor
frecuencias_normal = [x for x in sorted(list(con.frecuenciasIngles.items()), key = orden)]

# Se entrega los pares correspondientes de letra cifrada y letra normal
comprimido = list(zip(frecuencias_normal, frecuencias_texto))

# frecuencias_texto = [x[0] for x in sorted(list(instancia.informacion()[0].items()), key = orden)]
# # Frecuencias de una sola letra ordenadas de menor a mayor
# frecuencias_normal = [x[0] for x in sorted(list(con.frecuenciasIngles.items()), key = orden)]

# Frecuencias del texto cifrado ordenadas de menor a mayor
frecuencias_texto = [x for x in sorted(list(instancia.informacion()[1].items()), key = orden)]
# Frecuencias de una sola letra ordenadas de menor a mayor
frecuencias_normal = [x for x in sorted(list(con.frecuencias_2.items()), key = orden)]

# Se entrega los pares correspondientes de letra cifrada y letra normal
comprimido2 = list(zip(frecuencias_normal, frecuencias_texto))

# Frecuencias del texto cifrado ordenadas de menor a mayor
frecuencias_texto = [x[0] for x in sorted(list(instancia.informacion()[2].items()), key = orden)]
# Frecuencias de una sola letra ordenadas de menor a mayor
frecuencias_normal = [x[0] for x in sorted(list(con.frecuencias_3.items()), key = orden)]

# Se entrega los pares correspondientes de letra cifrada y letra normal
comprimido3 = list(zip(frecuencias_normal, frecuencias_texto))

iteraciones = 5
unigramas_escogidos = 0  # 26
bigramas_escogidos = 0  # 15
trigramas_escogidos = 0  # 11
indices_cifrados_1 = list(range(26))
indices_cifrados_2 = list(range(15))
indices_cifrados_3 = list(range(11))

letras_elegidas = []

desfase_uni = 0
desfase_bi = 0

auto = False

for i in range(iteraciones):
    if unigramas_escogidos < 26 and unigramas_escogidos + desfase_uni < 26:
        letra_or, frecuencia_or = comprimido[unigramas_escogidos][0]
        letra_cif, frecuencia_cif = comprimido[unigramas_escogidos + desfase_uni][1]  # Una letra cifrada
        repetido = False

        for pos, tupla in enumerate(letras_elegidas):
            letras_repetidas = tupla[0][0]
            n = len(letras_repetidas)
            if n == 1:
                if letras_repetidas == letra_or:  # Se rompe en el último índice ojo
                    repetido = True
                    print("Ha habido un conflicto con este unigrama! Elige una de estas dos opciones, revisa primero:")
                    instancia.subrayar(letra_cif, tupla[1][0])
                    # instancia.subrayar("".join(abecedario_nuevo), letra_or, letra_repetida)  # Solo ejecutar este si ya agregamos que cambiara parcialmente
                    print("En verde lo correcto y en amarillo las letras que se comparten")
                    print(f"Apreta 0 para elegir (rojo) {letra_or} con una frecuencia de {(frecuencia_or * 100):.1f}% en el inglés -> cifrado en {letra_cif} de {(frecuencia_cif * 100):.1f}% en el texto (Puesto {unigramas_escogidos + desfase_uni})")
                    print(f"Apreta 1 para mantener (azul) {letras_repetidas} con una frecuencia de {(tupla[0][1] * 100):.1f}% en el inglés -> cifrado en {tupla[1][0]} de {(tupla[1][1] * 100):.1f}% en el texto (Puesto {tupla[2]})")

                    eleccion = 1
                    if not auto:
                        eleccion = int(input())
                    else:
                        maximo = max(frecuencia_cif, tupla[1][1])
                        if maximo == frecuencia_cif:
                            eleccion = 0
                        else:
                            eleccion = 1

                    if eleccion == 0:
                        agregar_letras(abecedario, letra_or, letra_cif, abecedario_nuevo, 1)
                        letras_elegidas[pos] = ((letra_or, frecuencia_or), (letra_cif, frecuencia_cif), unigramas_escogidos + desfase_uni)
                        unigramas_escogidos += 1
                    else:
                        desfase_uni += 1
            elif n == 2:
                letra_repetida_1, letra_repetida_2 = tupla[0][0]
                if (letra_repetida_1 == letra_or) or (letra_repetida_2 == letra_or):
                    repetido = True
                    print("Ha habido un conflicto con este bigrama! Elige una de estas dos opciones, revisa primero:")
                    instancia.subrayar(letra_cif, tupla[1][0])
                    # instancia.subrayar("".join(abecedario_nuevo), letra_or, letras_cif)  # Solo ejecutar este si ya agregamos que cambiara parcialmente
                    print("En verde lo correcto y en amarillo las letras que se comparten")
                    print(f"Apreta 0 para elegir (rojo) {letra_or} con una frecuencia de {(frecuencia_or * 100):.1f}% en el inglés -> cifrado en {letra_cif} de {(frecuencia_cif * 100):.1f}% en el texto (Puesto {unigramas_escogidos + desfase_uni})")
                    print(f"Apreta 1 para mantener (azul) {tupla[0][0]} con una frecuencia de {(tupla[0][1] * 100):.1f}% en el inglés -> cifrado en {tupla[1][0]} de {(tupla[1][1] * 100):.1f}% en el texto (Puesto {tupla[2]})")

                    eleccion = 1
                    if not auto:
                        eleccion = int(input())
                    else:
                        maximo = max(frecuencia_cif, tupla[1][1])
                        if maximo == frecuencia_cif:
                            eleccion = 0
                        else:
                            eleccion = 1

                    if eleccion == 0:
                        agregar_letras(abecedario, letra_or, letra_cif, abecedario_nuevo, 1)
                        letras_elegidas[pos] = ((letra_or, frecuencia_or), (letra_cif, frecuencia_cif), unigramas_escogidos + desfase_uni)
                        unigramas_escogidos += 1
                    else:
                        desfase_uni += 1
            continue
        if not repetido:
            agregar_letras(abecedario, letra_or, letra_cif, abecedario_nuevo, 1)
            letras_elegidas.append(((letra_or, frecuencia_or), (letra_cif, frecuencia_cif), unigramas_escogidos + desfase_uni))
            unigramas_escogidos += 1

    if bigramas_escogidos < 15 and bigramas_escogidos + desfase_bi < 15:
        letras_or, frecuencia_or = comprimido2[bigramas_escogidos][0]
        letras_cif, frecuencia_cif = comprimido2[bigramas_escogidos + desfase_bi][1]  # Dos letras cifradas
        repetido = False

        for pos, tupla in enumerate(letras_elegidas):
            letras_repetidas = tupla[0][0]
            n = len(letras_repetidas)
            if n == 1:
                if letras_repetidas in letras_or:  # Se rompe en el último índice ojo
                    repetido = True
                    print("Ha habido un conflicto con este bigrama! Elige una de estas dos opciones, revisa primero:")
                    instancia.subrayar(letras_cif, tupla[1][0])
                    # instancia.subrayar("".join(abecedario_nuevo), letra_or, letra_repetida)  # Solo ejecutar este si ya agregamos que cambiara parcialmente
                    print("En verde lo correcto y en amarillo las letras que se comparten")
                    print(f"Apreta 0 para elegir (rojo) {letras_or} con una frecuencia de {(frecuencia_or * 100):.1f}% en el inglés -> cifrado en {letras_cif} de {(frecuencia_cif * 100):.1f}% en el texto (Puesto {bigramas_escogidos + desfase_bi})")
                    print(f"Apreta 1 para mantener (azul) {letras_repetidas} con una frecuencia de {(tupla[0][1] * 100):.1f}% en el inglés -> cifrado en {tupla[1][0]} de {(tupla[1][1] * 100):.1f}% en el texto (Puesto {tupla[2]})")

                    eleccion = 1
                    if not auto:
                        eleccion = int(input())
                    else:
                        maximo = max(frecuencia_cif, tupla[1][1])
                        if maximo == frecuencia_cif:
                            eleccion = 0
                        else:
                            eleccion = 1

                    if eleccion == 0:
                        agregar_letras(abecedario, letras_or, letras_cif, abecedario_nuevo, 2)
                        letras_elegidas[pos] = ((letras_or, frecuencia_or), (letras_cif, frecuencia_cif), bigramas_escogidos + desfase_bi)
                        bigramas_escogidos += 1
                    else:
                        desfase_bi += 1
            elif n == 2:
                letra_repetida_1, letra_repetida_2 = tupla[0][0]
                if (letra_repetida_1 in letras_or) or (letra_repetida_2 in letras_or):
                    repetido = True
                    print("Ha habido un conflicto con este bigrama! Elige una de estas dos opciones, revisa primero:")
                    instancia.subrayar(letras_cif, tupla[1][0])
                    # instancia.subrayar("".join(abecedario_nuevo), letras_or, letras_cif)  # Solo ejecutar este si ya agregamos que cambiara parcialmente
                    print("En verde lo correcto y en amarillo las letras que se comparten")
                    print(f"Apreta 0 para elegir (rojo) {letras_or} con una frecuencia de {(frecuencia_or * 100):.1f}% en el inglés -> cifrado en {letras_cif} de {(frecuencia_cif * 100):.1f}% en el texto (Puesto {bigramas_escogidos + desfase_bi})")
                    print(f"Apreta 1 para mantener (azul) {tupla[0][0]} con una frecuencia de {(tupla[0][1] * 100):.1f}% en el inglés -> cifrado en {tupla[1][0]} de {(tupla[1][1] * 100):.1f}% en el texto (Puesto {tupla[2]})")

                    eleccion = 1
                    if not auto:
                        eleccion = int(input())
                    else:
                        maximo = max(frecuencia_cif, tupla[1][1])
                        if maximo == frecuencia_cif:
                            eleccion = 0
                        else:
                            eleccion = 1

                    if eleccion == 0:
                        agregar_letras(abecedario, letras_or, letras_cif, abecedario_nuevo, 2)
                        letras_elegidas[pos] = ((letras_or, frecuencia_or), (letras_cif, frecuencia_cif), bigramas_escogidos + desfase_bi)
                        bigramas_escogidos += 1
                    else:
                        desfase_bi += 1
            continue
        if not repetido:
            agregar_letras(abecedario, letras_or, letras_cif, abecedario_nuevo, 2)
            letras_elegidas.append(((letras_or, frecuencia_or), (letras_cif, frecuencia_cif), bigramas_escogidos + desfase_bi))
            bigramas_escogidos += 1

    #
    # if trigramas_escogidos < 11:
    #     original_3 = comprimido3[trigramas_escogidos][0]
    #     cifrado_3 = comprimido3[indices_cifrados_3[trigramas_escogidos]][1]
    #     letra1 = cifrado_3[0]
    #     letra2 = cifrado_3[1]
    #     letra3 = cifrado_3[2]
    #
    #     if (letra1 in abecedario_nuevo) or (letra2 in abecedario_nuevo) or (letra3 in abecedario_nuevo):
    #         if trigramas_escogidos + 1 <= 25:
    #             temp = indices_cifrados_3[trigramas_escogidos]
    #             indices_cifrados_3[trigramas_escogidos] = indices_cifrados_3[trigramas_escogidos + 1]
    #             indices_cifrados_3[trigramas_escogidos + 1] = temp
    #     else:
    #         trigramas_escogidos += 1
    #         for pos, letra in enumerate(abecedario):
    #             letra1, letra2, letra3 = cifrado_3
    #             if letra == letra1:
    #                 abecedario_nuevo[pos] = letra1
    #             if letra == letra2:
    #                 abecedario_nuevo[pos] = letra2
    #             if letra == letra3:
    #                 abecedario_nuevo[pos] = letra3

print(abecedario_nuevo)
instancia.decifrar("".join(abecedario_nuevo))



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
