import matplotlib.pyplot as plt
import cifrado_sustitucion as cifrado

instancia = cifrado.CifradoSustitucion("cifrado sustitucion/text.txt")
instancia.cifrar()
instancia.decifrar()

letras = list(instancia.frecuencias.keys())
frecuencia = list(instancia.frecuencias.values())
letrasFrecuencia = list(zip(letras, frecuencia))
letrasFrecuencia.sort(key=lambda x: -x[1])

print(letrasFrecuencia)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar([x[0] for x in letrasFrecuencia], [x[1] for x in letrasFrecuencia], color='skyblue')

# Adding title and labels
plt.title('Counter Data Plot')
plt.xlabel('Labels')
plt.ylabel('Counts')

# Display the plot
plt.show()