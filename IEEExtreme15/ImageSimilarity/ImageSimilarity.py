# Lectores del Sistema
from calendar import c
from numpy import imag


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

#Funciones

def imprimir(imagen):
    for fila in imagen:
        aux = ''
        for valor in fila:
            aux += str(valor)+" "
        print(aux)

def transponer(imagen):
    return list(zip(*imagen))

def flip_vertical(imagen):
    return list(reversed(imagen))

def flip_horizontal(imagen):
    return transponer(flip_vertical(transponer(imagen)))

def reducir(imagen, r, c):
    transpuesta = transponer(imagen)
    valores = []
    
    # Extremos de las filas
    for i in range(r):
        if '#' in imagen[i]:
            valores.append(i)
            break
    
    flip = flip_vertical(imagen)
    
    for i in range(r):
        if '#' in flip[i]:
            valores.append(r-i)
            break
    
    # Extremos de las columnas
    for i in range(c):
        if '#' in transpuesta[i]:
            valores.append(i)
            break
    
    flip = flip_vertical(transpuesta)
    
    for i in range(c):
        if '#' in flip[i]:
            valores.append(c-i)
            break
    
    imagen_res = transponer(transpuesta[valores[2]:valores[3]])[valores[0]:valores[1]]
    
    return (imagen_res, valores[1]-valores[0], valores[3]-valores[2])


def compara(imagen_1, imagen_2, r_1, c_1, r_2, c_2):
    
    imagen_1, r_1, c_1 = reducir(imagen_1, r_1, c_1)
    imagen_2, r_2, c_2 = reducir(imagen_2, r_2, c_2)
    
    print(r_1, c_1)
    imprimir(imagen_1)
    print(r_2, c_2)
    imprimir(imagen_2)

def main():
    n = get_number()
    
    for i in range(n):
        r_1 = get_number()
        c_1 = get_number()
        
        imagen_1 = []
        for j in range(r_1):
            imagen_1.append(list(input()))
        
        r_2 = get_number()
        c_2 = get_number()
        
        imagen_2 = []
        for j in range(r_2):
            imagen_2.append(list(input()))
        
        compara(imagen_1, imagen_2, r_1, c_1, r_2, c_2)

# Ejecuta
main()