"""
1. problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e)}

Implementar al menos de 3 formas distintas este problema.
"""

def pertenece1 (s=list[int], z=int)-> bool:
    for elemento in s:
        if elemento == z:
            return True
    return False
        
def pertenece2 (s=list[int],z=int)-> bool:
    while (z not in s):
        return False
    return True

def pertenece3 (s=list[int],z=int)->bool:
    if z in s:
        return True
    else:
        return False

# print(pertenece3([2,3,1,2], 4))

"""
problema divide a todos (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: {e ̸= 0 }
asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}
}
"""

def divide_a_todos(s= list[int],e = int)-> bool:
    if e != 0:
        for numero in s:
            if ((numero % e) != 0):
                return False
        return True
    else:
        return False

# print(divide_a_todos([3,6,3,9],0))

"""
problema suma total (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { res es la suma de todos los elementos de s}
}
"""

def suma_total(s= list[int])-> int:
    total = 0
    for elemento in s:
        total += elemento
    return total

# print(suma_total([1,2,3,4,5,0,0,0]))

"""
problema maximo (in s:seq⟨Z⟩) : Z {
requiere: {|s| > 0 }
asegura: { res = al mayor de todos los n´umeros que aparece en s}
}

"""

def maximo(s=list[int]) -> int:
    maximo_valor = s[0]
    i = 0  

    while i < len(s) - 1:
        if s[i + 1] > maximo_valor:  
            maximo_valor = s[i + 1]  
        i += 1  
    
    return maximo_valor

# print(maximo([-4,-7,-2,0]))

"""
5. problema minimo (in s:seq⟨Z⟩) : Z {
requiere: {|s| > 0 }
asegura: { res = al menor de todos los n´umeros que aparece en s}
}

"""

def minimo(s= list[int]) -> int:
    num_minimo = s[0]
    i=0

    while i < len(s) - 1:
        if s[i+1] < num_minimo:
            num_minimo = s[i+1]
        i += 1

    return num_minimo

# print(minimo([1,5,2,-3]))

"""
6. problema ordenados (in s:seq⟨Z⟩) : Bool {
requiere: { T rue }
asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1]}
}

"""

def ordenados(s=list[int]) -> bool:
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            return False
    return True

# print(ordenados([5,9,10,25]))

"""
7. problema pos maximo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el mayor elemento
de s (si hay varios es la primera aparici´on)}
}
"""

def pos_maximo(s=list[int]) -> bool:
    if len(s) == 0:
        return -1
    else:
        maximo_valor = s[0]
        pos_maximo_valor = 0
        i = 0  

        while i < len(s) - 1:
            if s[i + 1] > maximo_valor:  
                maximo_valor = s[i + 1]
                pos_maximo_valor = i+1  
            i += 1  
    
    return pos_maximo_valor

# print(pos_maximo([2,4,6,6,6,6]))

"""
8. problema pos minimo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el menor elemento
de s (si hay varios es la ´ultima aparici´on)}
}
"""

def pos_minimo(s=list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        num_minimo = s[0]
        pos_minimo_valor = 0
        i = 0  

        while i < len(s) - 1:
            if s[i + 1] < num_minimo:  
                num_minimo = s[i + 1]
                pos_minimo_valor = i+1  
            i += 1  
    
    return pos_minimo_valor

# print(pos_minimo([1,5,-2,20]))

"""
9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
[“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
"""

def palabras_mayores_a_7(s = list[list[str]]) -> bool:
    for palabras in s:
        if len(palabras) > 7:
            return True
    return False

# print(palabras_mayores_a_7(["hola","mayora7palabras","pepe"]))

"""
10) Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
"""

def es_palindromo(palabra=str) -> bool:
    return descomponer_palabra(palabra) == invertir_palabra(palabra)

def descomponer_palabra(palabra=str) -> list:
    lista_caracteres = []
    for caracter in palabra:
        lista_caracteres.append(caracter)
    return lista_caracteres

def invertir_palabra(palabra = str) -> list:
    palabra_invertida = []
    i = len(palabra)
    while i > 0:
        palabra_invertida.append(palabra[i-1])
        i -= 1
    return palabra_invertida

# print(descomponer_palabra("arenera"))
# print(invertir_palabra("arenera"))
# print(es_palindromo("arenera"))

"""
11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 n´umeros iguales consecutivos, en cualquier posici´on y False en caso
contrario
"""

def hay_3_numeros_consecutivos_iguales(lista_numeros:list)-> bool:
    i = 0
    contador = 1
    while i < (len(lista_numeros) - 1):
        if lista_numeros[i] == lista_numeros[i+1]:
            contador += 1
            if contador == 3:
                return True
        else:
            contador = 1
        i += 1
    return False
      
# print(hay_3_numeros_consecutivos_iguales([1,2,3,2,2,3,1,1,1]))

"""
12. Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso
contrario
"""

def hay_3_letras_distintas(palabra:str)->bool:
    lista_caracteres = descomponer_palabra(palabra)
    vocales = ["a","e","i","o","u"]
    contador = 1

    for i in range(len(vocales)-1):
        if pertenece1(lista_caracteres, vocales[i]):
            contador += 1
        print(contador)
    if contador >= 3:
        return True
    else:
        return False
    
# print(hay_3_letras_distintas("murcie"))

"""
13. Recorrer una seq⟨Z⟩ y devolver la posici´on donde inicia la secuencia de n´umeros ordenada m´as larga. Si hay dos
subsecuencias de igual longitud devolver la posici´on donde empieza la primera. La secuencia de entrada es no vac´ıa.
"""

def pos_secuencia_mas_larga(numeros: list[int])-> int:
    lista_contadores: list = []
    lista_posiciones: list = [0]
    contador: int = 0

    for i in range(len(numeros) - 1):
        if numeros[i] < numeros[i+1]:
            contador += 1
        else:
            lista_contadores.append(contador)
            lista_posiciones.append(i+1)
            contador = 0
        
    lista_contadores.append(contador)

    return lista_posiciones[pos_maximo(lista_contadores)]

# print(pos_secuencia_mas_larga([1,2,3,4,2,3,4,5,6]))
# print(pos_secuencia_mas_larga([1,2,3]))
# print(pos_secuencia_mas_larga([1,2,3,0,10,12,13,44,55,66,-1,0,1,2,3,4,5,7,8,9]))
print(pos_secuencia_mas_larga([1,1,1,1,2,2,2,2,2,2]))