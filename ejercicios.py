from pprint import pprint
# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes.
string = 'Hola Mundo Henry este es mi string'


def quita_espacios(texto):
    # Lista Comprimida
    return [caracter for caracter in texto if caracter != ' ']


cadenaSinEspacios = quita_espacios(string)
print(cadenaSinEspacios)

# 2. contar en un diccionario cuanto se repiten los caracteres de un string.
caracteres = 'AAABBBBCCDEFFFFDFFFFBFF'

# Modo 1


def contar_caracteres(texto):
    return {letra: texto.count(letra) for letra in texto}


diccionario = contar_caracteres(cadenaSinEspacios)
print(diccionario)

# Modo2


def cuenta_caracteres(lista):
    char_dict = {}
    for char in lista:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


contados = cuenta_caracteres(cadenaSinEspacios)
pprint(contados, width=1)


# Ordendar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas
# [("a", 3),("b",2),("c",4),("d",4)]
dic_1 = {"a": 3, "b": 2, "c": 9, "d": 7, "e": 6}
dic_ordenado = dict(sorted(dic_1.items(), key=lambda x: x[1]))
print(dic_1)
print(dic_ordenado)
