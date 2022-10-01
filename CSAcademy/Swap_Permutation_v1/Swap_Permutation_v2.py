# Version 2 del ejercicio Swap Permutation de CSAcademy
# Esta version busca reducir el coste de tiempo de ejecucion solo analizando la posicion de 1 en N_list
# sin hacer todo el procedimineto de movimientos, ya que no son necesarios para la resolucion del problema.

#------------------------------------------------------------
# Funciones

#------------------------------------------------------------
# --- MAIN ---

#Obtenemos los datos de entrada

N, M, K = map(int, input().split())
M_list = []

for i in range(M):
    input_1, input_2 = map(int, input().split())
    M_list.append(input_1)
    M_list.append(input_2)

#Guardamos la posicion de 1 en N_list
pos_original = 1
pos_restore = 1

#Realizamos los cambios para encontrar el valor 1 en el indice K solo en el valor de 1
for discard in range(M):
    
    used_indices = {} # Diccionario que guarda los indices usados en cada iteracion
    
    #bucle de cambio de posicion de 1 en N_list, sin saber la cantidad de cambios
    while True:
        if discard != 0:
            pass
        
        prox_pos = M_list.index(pos_original) # Buscamos la posicion de 1 en N_list
        
        if prox_pos % 2 != 0: prox_pos -= 1 # Si la posicion es impar, se resta 1 para obtener la posicion de la tupla
        prox_pos /= 2
        prox_pos += 1
        # asi obtenemos la posicion de la tupla en M_list
        
        if prox_pos != discard:
            pass