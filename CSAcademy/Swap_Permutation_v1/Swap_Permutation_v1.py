# N : Largo del vector de permutacion
# La lista esta en orden ascendente, de 1 hasta N.
# M : Largo del vector de intercambios
# M es una lista de tuplas de 2 con los indices a intercambiar
# K : indice donde se debe encontrar el valor de 1

# Objetivo: Remover una de las tuplas de la lista de M, y realizar los cambios de M en orden,
# donde el indice K sea el valor 1
# Output: Imprimir el indice contando desde 1 de la tupla que se removio

#------------------------------------------------------------
#Creamos una funcion para intercambiar el valor de los valores en N
def swap(N_list, index_1, index_2):
    N_list[index_1], N_list[index_2] = N_list[index_2], N_list[index_1]

#------------------------------------------------------------
# --- MAIN ---

#Obtenemos los datos
N, M, K = map(int, input().split())
M_list = []

for i in range(M):
    M_list.append(tuple(map(int, input().split())))

#Creamos la lista N Creciente
N_list = list(range(1, N+1))

#Realizamos los cambios para encontrar el valor 1 en el indice K

discard = 1  #Variable para almacenar el indice de la tupla que se removio

for i in range(M):
    pass



