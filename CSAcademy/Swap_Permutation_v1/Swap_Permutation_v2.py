# Version 2 del ejercicio Swap Permutation de CSAcademy
# Esta version busca reducir el coste de tiempo de ejecucion solo analizando la posicion de 1 en N_list
# sin hacer todo el procedimineto de movimientos, ya que no son necesarios para la resolucion del problema.

#------------------------------------------------------------
# Funciones

#------------------------------------------------------------
# --- MAIN ---

#Obtenemos los datos de entrada
from CSAcademy.Swap_Permutation_v1.Swap_Permutation_v1 import M_list


N, M, K = map(int, input().split())
M_list_1 = []
M_list_2 = []

for i in range(M):
    input_1, input_2 = map(int, input().split())
    M_list_1.append(input_1)
    M_list_2.append(input_2)

