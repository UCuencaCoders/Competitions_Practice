# Ejercicio 1 de la ronda G de KickStar 2019, 10pts, 15pts.
# V2 realizada de forma matematica

# Obtenemos el numero de casos de prueba
test_cases  =  int ( input ())

for case in range(test_cases):
    book_pages, bad_pages, readers = map(int, input().split()) # Obtenemos los datos de entrada numero de paginas, paginas malas y lectores
    bad_pages_list = list(map(int, input().split())) # Obtenemos la lista de paginas malas
    readers_iter_list = list(map(int, input().split())) # Obtenemos la lista de saltos que hace cada lector
    
    total_pages_readed = 0 # Inicializamos el numero de paginas leidas
    