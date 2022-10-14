## Funciones
def conv(string):
    return bool(int(string))

## Main
array = list(map(conv, input()))
print(array)

exchanger = array[-1]
array = array[array.index(True):-1]
print(array)

total = 0
point = 0
first = array.index(True, 1)

on_list = [i for i in range(len(array)) if array[i]]

print(on_list)

for index in on_list:
    pass
