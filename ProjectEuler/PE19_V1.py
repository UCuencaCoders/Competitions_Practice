from datetime import date, timedelta

t = int(input())

mesExtra = [1,4,4,0,2,5,0,3,6,1,4,6]
dias = [6,7,1,2,3,4,5]

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

def diaSemana(anio,mes,dia):
    suma = (anio-1900) + mesExtra[mes-1] + dia +((anio-1900)/4)
    return dias[int(suma%7)];

def mueveDia(fecha: list,extra):
    mes31 = [1,3,5,7,8,10,12]
    mes30 = [4,6,9,11]
    
    dias: int
    if fecha[1] in mes31:
        dias = 31
    elif fecha[1] in mes30:
        dias = 30
    else:
        siglo = int(fecha[0] / 100)
        siglo *= 100
        if (fecha[0] % 400 == 0) and (fecha[0] % 100 == 0):
            dias = 29
        elif (fecha[0] % 4 ==0) and (fecha[0] % 100 != 0):
            dias = 29
        else:
            dias = 28
    
    fecha[2] += extra
    if fecha[2] > dias:
        fecha[2] -= dias
        fecha[1] += 1
        if fecha[1] > 12:
            fecha[1] -= 12
            fecha[0] += 1
    
    return fecha

def comDia(fecha_1: list, fecha_2: list):
    if fecha_1[0] < fecha_2[0]:
        return True
    elif fecha_1[1] < fecha_2[1]:
        return True
    elif fecha_1[2] <= fecha_2[2]:
        return True
    return False

for _ in range(1):
    first = list(map(int, input().split()))
    last = list(map(int, input().split()))
    dia = diaSemana(*first)
    first = mueveDia(first, 7-dia)
    
    total = 0
    while comDia(first,last):
        if first[2] == 1:
            print(first, end=", ")
            total += 1
        first = mueveDia(first,7)
    
    print(total)