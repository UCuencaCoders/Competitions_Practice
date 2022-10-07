# Solicion Word Ordening de CSAcademy V1

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" #Alfabeto original
new_alphabet = input() #Cargamos el alfabeto nuevo
new_alphabet = new_alphabet + new_alphabet.upper() #Agregamos el alfabeto en mayusculas

word_list = [] #Lista de palabras

for i in range(int(input())): #Cargamos la cantidad de palabras
    word = input() #Cargamos la palabra
    new_word = "" #Creamos una variable para la nueva palabra
    for char in word: #Recorremos cada caracter de la palabra
        new_word += alphabet[new_alphabet.index(char)] #Agregamos el caracter del alfabeto original
    
    word_list.append(new_word) #Agregamos la palabra a la lista

word_list.sort() #Ordenamos la lista

for word in word_list: #Recorremos la lista
    new_word = "" #Creamos una variable para la nueva palabra
    for char in word: #Recorremos cada caracter de la palabra
        new_word += new_alphabet[alphabet.index(char)] #Agregamos el caracter del alfabeto nuevo
    print(new_word) #Imprimimos la palabra

# Codigo perfecto 100/100 en CSAcademy