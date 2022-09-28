# Ejercicio 1 de la ronda G de KickStar 2019, 10pts, 15pts.

# Obtenemos el numero de casos de prueba
from asyncore import read


test_cases  =  int ( input ())

for case in range(test_cases):
    book_pages, bad_pages, readers = map(int, input().split()) # Obtenemos los datos de entrada numero de paginas, paginas malas y lectores
    bad_pages_list = list(map(int, input().split())) # Obtenemos la lista de paginas malas
    readers_iter_list = list(map(int, input().split())) # Obtenemos la lista de saltos que hace cada lector
    
    total_pages_readed = 0 # Inicializamos el numero de paginas leidas
    
    for reader in readers_iter_list:
        
        pages_readed = 0 # Inicializamos el numero de paginas leidas por el lector
        new_page = reader # Inicializamos la pagina que va a leer el lector
        
        # Vamos a iterar solo las paginas que va a leer el lector y no son malas
        while new_page <= book_pages:
            if new_page not in bad_pages_list:
                pages_readed += 1 # Aumentamos el numero de paginas leidas
            
            new_page += reader # Calculamos la nueva pagina a leer
        
        total_pages_readed += pages_readed # Sumamos las paginas leidas por el lector al total de paginas leidas
    
    print("Case #{}: {}".format(case+1, total_pages_readed)) # Imprimimos el resultado por caso de prueba
