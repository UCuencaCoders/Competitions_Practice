def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

def buscar(palabra, pos_x, pos_y, hor, ver):
    for i in range(1, len(palabra)):
        y = pos_y + (ver*i)
        x = pos_x + (hor*i)
        if palabra[i] != matriz[y][x]:
            return None
    return (y, x)

def iterador(palabra):
    for pos_y, fila in enumerate(matriz):
        for pos_x, letra in enumerate(fila):
            if letra == palabra[0]:
                
                ## 1 Comprobacion diagonal izquierda arriba
                if pos_y >= len(palabra)-1 and pos_x >= len(palabra)-1:
                    res = buscar(palabra, pos_x, pos_y, -1, -1)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
                
                ## 2 Comprobacion horizontal izquierda
                if pos_x >= len(palabra)-1:
                    res = buscar(palabra, pos_x, pos_y, -1, 0)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
                
                ## 3 Comprobacion vertical arriba
                if pos_y >= len(palabra)-1:
                    res = buscar(palabra, pos_x, pos_y, 0, -1)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
                
                ## 4 Comprobacion diagonal izquierda abajo
                if pos_y <= r-len(palabra) and pos_x >= len(palabra)-1:
                    res = buscar(palabra, pos_x, pos_y, -1, 1)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
                
                ## 5 Comprobacion vertical abajo
                if pos_y <= r-len(palabra):
                    res = buscar(palabra, pos_x, pos_y, 0, 1)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
                
                ## 6 Comprobacion diagonal derecha arriba
                if pos_y >= len(palabra)-1 and pos_x <= c-len(palabra):
                    res = buscar(palabra, pos_x, pos_y, 1, -1)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
                
                ## 7 Comprobacion horizontal derecha
                if pos_x <= c-len(palabra):
                    res = buscar(palabra, pos_x, pos_y, 1, 0)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
                
                ## 8 Comprobacion diagonal derecha abajo
                if pos_y <= r-len(palabra) and pos_x <= c-len(palabra):
                    res = buscar(palabra, pos_x, pos_y, 1, 1)
                    if type(res) is tuple: return [pos_y, pos_x, res[0], res[1]]
    return None

## Main

r = get_number() #rows filas
c = get_number() #columns
q = get_number() #numero de palabras

matriz = []

for i in range(r):
    matriz.append(input())

palabras = []

for i in range(q):
    palabras.append(input())

for palabra in palabras:
    res = iterador(palabra)
    if type(res) is list:
        print(res[0], res[1], res[2], res[3])
    else:
        print("-1")

