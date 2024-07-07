import numpy as np
import matplotlib.pyplot as plt

frecuenciaLetras = {
    'A': 11.72, 'Á': 0.44, 'B': 1.49, 'C': 3.87, 'D': 4.67, 'E': 13.72, 'É': 0.36, 
    'F': 0.69, 'G': 1.00, 'H': 1.18, 'I': 5.28, 'Í': 0.70, 'J': 0.52, 'K': 0.11, 
    'L': 5.24, 'M': 3.08, 'N': 6.83, 'Ñ': 0.17, 'O': 8.44, 'Ó': 0.76, 'P': 2.89, 
    'Q': 1.11, 'R': 6.41, 'S': 7.20, 'T': 4.60, 'U': 4.55, 'Ü': 0.02, 'Ú': 0.12, 
    'V': 1.05, 'W': 0.04, 'X': 0.14, 'Y': 1.09, 'Z': 0.47
}

letras = list(frecuenciaLetras.keys())
frecuencias = np.array(list(frecuenciaLetras.values())) 

plt.figure(figsize=(10, 6))
plt.bar(letras, frecuencias, color='skyblue')

plt.title('Letter Frequencies')
plt.xlabel('Letters')
plt.ylabel('Frequency (%)')


text = "En el criptoanálisis, la técnica de análisis de frecuencias consiste en el aprovechamiento de estudios sobre la frecuencia de las letras o grupos de letras en los idiomas para poder establecer hipótesis para aprovecharlas para poder descifrar un texto cifrado sin tener la clave de descifrado (romper). Es un método típico para romper cifrados clásicos."
text = text.upper()
