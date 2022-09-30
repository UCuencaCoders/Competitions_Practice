# Ejercicio 1 de la ronda G de KickStar 2019, 10pts, 15pts.
# V2 realizada de forma matematica

# Obtenemos el numero de casos de prueba
test_cases  =  int ( input ())

for case in range(test_cases):
    book_pages, bad_pages, readers = map(int, input().split()) # Obtenemos los datos de entrada numero de paginas, paginas malas y lectores
    bad_pages_list = list(map(int, input().split())) # Obtenemos la lista de paginas malas
    readers_iter_list = list(map(int, input().split())) # Obtenemos la lista de saltos que hace cada lector
    
    total_pages_readed = 0 # Inicializamos el numero de paginas leidas
    
    for reader in readers_iter_list:
        total_pages = book_pages // reader # Obtenemos el numero de paginas que va a leer el lector sin contar las malas
        bad_pages_not_readed = 0 # Inicializamos el numero de paginas malas que no va a leer el lector
        bad_pages_not_readed += len([x for x in bad_pages_list if x % reader == 0]) # Obtenemos el numero de paginas malas que no va a leer el lector
        total_pages -= bad_pages_not_readed # Restamos el numero de paginas malas que no va a leer el lector al total de paginas que va a leer el lector
        
        total_pages_readed += total_pages # Sumamos las paginas leidas por el lector al total de paginas leidas
    
    print("Case #{}: {}".format(case+1, total_pages_readed)) # Imprimimos el resultado por caso de prueba