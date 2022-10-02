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
    
    dis_restore_1 = M_list[discard*2]
    dis_restore_2 = M_list[(discard*2)+1]
    M_list[discard*2], M_list[(discard*2)+1] = 0, 0
    
    if discard == 0:
        advance = 0
    else:
        advance = (discard - 1) * 2
    
    #bucle de cambio de posicion de 1 en N_list, sin saber la cantidad de cambios
    while True:
        
        try:
            prox_pos = M_list.index(pos_original, advance) # Buscamos la posicion de 1 en N_list, y su uso
        
            #- Realizamos el proximos swap
        
            if prox_pos % 2 == 0: # Si la posicion de 1 en M_list es par
                pos_original = M_list[prox_pos+1]
            else:
                pos_original = M_list[prox_pos-1]
            
            # Cambiamos el avance a la nueva posicion del index de 1 en M_list
            if prox_pos % 2 == 0:
                advance = prox_pos+2
            else:
                advance = prox_pos+1
            
            if advance <= discard*2:
                pos_restore = pos_original
        
        except ValueError:
            break # Si no hay mas cambios, final de la iteracion del descarte
    
    if pos_original == K:
        print(discard+1)
        break
    
    pos_original = pos_restore
    
    M_list[discard*2] = dis_restore_1
    M_list[(discard*2)+1] = dis_restore_2

# Funcionando correctamente en CSAcademy, puntaje 60/100, buena mejor, pero falla en 4 por tiempo