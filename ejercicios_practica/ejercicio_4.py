# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones y módulos
import random

# --------------------------------
# Aquí dentro definir la función lista_aleatoria

def lista_aleatoria(inicio, fin, cantidad):
    lista=[]
    for i in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        lista.append(numero)
    return lista
# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 0
    fin = 10
    cantidad = 5

    # Alumno: Crear la función "lista_aleatoria"

    # Para este ejercicio utilizaremos el módulo random
    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    '''
    numero = random.randrange(inicio, fin+1)
    '''
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    # Realice una funcion llamada "lista_aleatoria" la cual
    # reciba como parámetro el rango de aceptación de la lista
    # "inicio y fin" y la cantidad de elementos que deseamos que
    # contenga la lista, es decir, la cantidad de elementos random a generar.

    # def lista_aleatoria (inicio, fin, cantidad)

    # Para ello dentro de la función deberá realizar un bucle que repita "cantidad"
    # veces esta operacion:
    # numero = random.randrange(inicio, fin+1)

    # Cada valor generado lo debe guardar en una lista, recuerde:
    # 1) Iniciar y crear esa lista vacia.
    # 2) Para agregar nuevos elementos en la lista utiliza "append"

    # Finalmente dicha función debe retornar la lista de elementos random generados.

    # Luego de crear la función invocarla en este lugar:

    # mi_lista_aleatoria = lista_aleatoria(inicio, fin, cantidad)
    mi_lista_aleatoria = lista_aleatoria(inicio, fin, cantidad)
    # Imprimir en pantalla "mi_lista_aleatoria" que tendrá
    # los valores retornado por la función lista_aleatoria:

    # print(mi_lista_aleatoria)
    print("mi_lista_aleatoria" , mi_lista_aleatoria)
    print("terminamos")