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
# lista de todos los posibles bigramas y frecuencias
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
bigrama = {}
for primera_letra in alfabeto:
    for segunda_letra in alfabeto:
        letra = primera_letra + segunda_letra
        bigrama[letra] = 0 

textocifrado =  instancia.texto
cantidaddebigramas = 0
for i in range(len(textocifrado)-1):
    palabra = textocifrado[i]+textocifrado[i+1]
    if palabra in bigrama:
        bigrama[palabra] += 1
        cantidaddebigramas += 1
for i in bigrama:
    bigrama[i] = bigrama[i]/cantidaddebigramas
bigrama = sorted(bigrama.items(), key=lambda kv: kv[1],reverse= True)
bigrama = bigrama[:11]

#Frecuencia del trigrama en la palabra cifrada
trigrama = {}
for primera_letra in alfabeto:
    for segunda_letra in alfabeto:
        for tercera_letra in alfabeto:
            letra = primera_letra + segunda_letra + tercera_letra
            trigrama[letra] = 0 


cantidaddetrigrama = 0

for i in range(len(textocifrado)-2):
    palabra = textocifrado[i]+textocifrado[i+1] + textocifrado[i+2]
    if palabra in trigrama:
        trigrama[palabra] += 1
        cantidaddetrigrama += 1
for i in trigrama:
    trigrama[i] = trigrama[i]/cantidaddebigramas
trigrama = sorted(trigrama.items(), key=lambda kv: kv[1],reverse= True)
trigrama = trigrama[:11]

