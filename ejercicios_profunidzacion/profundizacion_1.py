# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira la dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números.
Esa lista de datos se llamará dados_tirados

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió. Consultar los ejemplos
vistos en clase en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una lista aparte esos números más repetidos.
Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
Debe extrarlos de la lista, quedándole una lista separada
dados_guardados = [4,4,4]
Debe realizar un bucle para recorrer la lista de dados_tirados
y guardar los "4" en nuestra nueva lista dados_guardados
Utilie append para ir sumando a dados_guardados los valores

4) Debe volver a tira los dados, generar nuevos
números aleatorios.
Si en la lista "dados_guardados" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados. Puede usar la función
"len" para ver cuantos elementos hay en "dados_guardados"
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a quedarme con el "4" ya que es el número que estoy
buscando almacenar en la otra lista de "dados_guardados".
Sino salió el "4" vuelvo a tirar todos los dados (solo 2 dados en este caso)
Si salió un "4" me lo quedo y lo guardo en "dados_guardados".

5) Debe repetir este proceso hasta que en su lista de "dados
guardados" tenga "generala", es decir, 5 números iguales.
'''

import random
lista_temporal = []
lista_temporal_2 = []
lista_temporal_3 = []


lista_de_1 = []
lista_de_2 = []
lista_de_3 = []
lista_de_4 = []
lista_de_5 = []
lista_de_6 = []


lista_para_guardar = []
lista_guardada = []


dados_a_tirar = 0
# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice
def primera_tirada():
   
    for i in range(5):
        
        numrand = random.randrange(1, 7)
        
       
        lista_temporal.append(numrand)

    for x in lista_temporal:
        if x == 1:
            lista_de_1.append(x)
        elif x == 2:
            lista_de_2.append(x)
        elif x == 3:
            lista_de_3.append(x)
        elif x == 4:
            lista_de_4.append(x)
        elif x == 5:
            lista_de_5.append(x)
        elif x == 6:
            lista_de_6.append(x)

    print("1=", lista_de_1)
    print("2=", lista_de_2)
    print("3=", lista_de_3)
    print("4=", lista_de_4)
    print("5=", lista_de_5)
    print("6=", lista_de_6)
    
    lista_para_guardar = max(lista_de_1, lista_de_2, lista_de_3, lista_de_4, lista_de_5, lista_de_6, key=len)

    for i in lista_para_guardar:
        lista_guardada.append(i)


    return lista_guardada

def segunda_tirada():  
    
    dados_a_tirar = 5 - (len(lista_guardada))
    print("Dados a tirar", dados_a_tirar)

    for i in range(dados_a_tirar):

        numrand = random.randrange(1, 7)
        
        lista_temporal_2.append(numrand)

    print("En tu segundo tiro salio esto", lista_temporal_2)
    
    for i in lista_temporal_2:
        if i == num_necesitado:
            lista_guardada.append(i)
    
    return lista_guardada

def tercera_tirada():
        
    dados_a_tirar = 5 - (len(lista_guardada))
    print("Dados a tirar", dados_a_tirar)

    for i in range(dados_a_tirar):

        numrand = random.randrange(1, 7)
        
        lista_temporal_3.append(numrand)

    print("En tu tercer tiro salio esto", lista_temporal_3)
    
    for i in lista_temporal_3:
        if i == num_necesitado:
            lista_guardada.append(i)
    
    return lista_guardada

# --------------------------------

if __name__ == '__main__':
    print("¡El juego de la generala!")
    # A partir de aquí escriba el código que
    # invoca al as funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    print("Este es el resultado de tu primer tiro")
    primera_tirada()
    print("Te quedaste con estos dados")
    print (lista_guardada)
    
    num_necesitado = lista_guardada[0]
    print("Necesitas este numero", num_necesitado)

    if len(lista_guardada) == 5:
        print ("Ganaste en un tiro!!!")
   
    else:
        print("Vamos con el segundo tiro")
        segunda_tirada()
        print("Te quedaste con estos dados")
        print(lista_guardada)

        if len(lista_guardada) == 5:
            print("Hiciste la generala en tu segundo tiro!")
       
        else:
            tercera_tirada()
            print("Te quedaste con estos dados")
            print(lista_guardada)
            if len(lista_guardada) == 5:
                print("Hiciste la generala en tu tercer tiro!")
            
            else:
                print("No salio generala")
                print("Perdiste :(")
