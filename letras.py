# Desafío - Letras
# Patricio Cortés
# G18
# 04-09-2021

# Importa librerias
import string

# definir funcion "gen"
def gen(num):
    abc = string.ascii_lowercase    # pasamos el abecedario a la variable "abc"
    concatenador = ""               # guarda las letras del abecedario
    contador = 0                    # cuenta las letras que llevamos concatenadas
    
    # comienza iteraciones
    for i in abc:
        if contador < num:      # compara si aun debemos seguir concatenando letras
            concatenador += i   # aquí se hace la magia :)
        contador += 1           # aumenta la cuenta
    return concatenador         # devuelve las letras concatenadas

# ******************
# programa principal
# ******************
# Usuario ingresa el número de letras a generar del abecedario
num_letras = int(input("Ingrese el número de letras del abecedario a generar:\n"))

letras = gen(num_letras)
print(letras)

# Fin del Programa