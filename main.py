
# Crea una funcion que cree una lista de 100 numeros aleatorios del 1 al 1000
# y que los muestre por pantalla ordenados de menor a mayor
# Path: main.py
import random
def lista():
    lista = []
    for i in range(100):
        lista.append(random.randint(1,1000))
    lista.sort()
    print(lista)

# Ejemplo de uso
lista()
