# N : Largo del vector de permutacion
# La lista esta en orden ascendente, de 1 hasta N.
# M : Largo del vector de intercambios
# M es una lista de tuplas de 2 con los indices a intercambiar
# K : indice donde se debe encontrar el valor de 1

# Objetivo: Remover una de las tuplas de la lista de M, y realizar los cambios de M en orden,
# donde el indice K sea el valor 1
# Output: Imprimir el indice contando desde 1 de la tupla que se removio

#------------------------------------------------------------
# Funciones

#------------------------------------------------------------
# --- MAIN ---

#Obtenemos los datos de entrada
N, M, K = map(int, input().split())
M_list = []

for i in range(M):
    M_list.append(tuple(map(int, input().split())))

#Creamos la lista N Creciente
N_list = list(range(1, N+1))

#Realizamos los cambios para encontrar el valor 1 en el indice K
restore_list = [] # Lista que guarda el estado de N_list en la posicion de descarte

for discard in range(M): # Bucle de busqueda, se descarta una tupla por cada iteracion
    
    for pos in range(discard-1, M): # Bucle de intercambio de valores en N_list sin contar la tupla descartada
        if pos == discard:
            restore_list = N_list.copy() # Guardamos el estado de N_list en la posicion de descarte
        elif pos >= 0:
            index_1 = M_list[pos][0] - 1
            index_2 = M_list[pos][1] - 1
            N_list[index_1], N_list[index_2] = N_list[index_2], N_list[index_1]
    
    if N_list[K-1] == 1: 
        print(discard+1) # Si el valor 1 esta en el indice K, se imprime el indice de la tupla descartada
        break # Se termina el bucle de busqueda
    else: 
        N_list = restore_list.copy() # Si no, se restaura el estado de N_list y se continua con la siguiente tupla


# Puntaje obtenido 30/100, desde el test case 4 para arriba me pasa el tiempo de ejecucion por 80ms.
