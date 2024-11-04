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

def hay_3_vocales_distintas(palabra:str)->bool:
    lista_caracteres = descomponer_palabra(palabra)
    vocales = ["a","e","i","o","u"]
    contador = 0

    for i in range(len(vocales)):
        if pertenece1(lista_caracteres, vocales[i]):
            contador += 1
    if contador >= 3:
        return True
    else:
        return False
    
# print(hay_3_vocales_distintas("murcie"))
# print(hay_3_vocales_distintas("vocales"))
# print(hay_3_vocales_distintas("mariposa"))
# print(hay_3_vocales_distintas("anahi"))

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
# print(pos_secuencia_mas_larga([1,1,1,1,2,2,2,2,2,2]))

"""
1. problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
requiere: { T rue }
modifica: {s}
asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
es par, entonces s[i] = 0)}
}
"""

def CerosEnPosicionesPares(s:list[int])-> list[int]:
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0
            
    return s

#Aca por la especificacion tengo que devolver s, en este caso s es modificado porque es inout
#Basicamente que algo sea in significa que tengo que tener cuidado y al momento de devolverlo tiene que ser exactamente igual
#A como entro en la funcion

#print(CerosEnPosicionesPares([1,2,3,4,5,6,7,8]))

"""
2. problema CerosEnPosicionesPares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { T rue }
asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i es
par, entonces res[i] = 0)}
}
"""

def CerosEnPosicionesPares2(s:list[int])-> list[int]:
    resultado: list = []
    for i in range(len(s)):
        if i % 2 == 0:
            resultado.append(s[i])
        else:
            resultado.append(0)
    return resultado

def CerosEnPosicionesPares2Profes(s:list[int])-> list[int]:
    res:list[int] = s.copy()
    for i in range(0,len(s),2):
        res[i]=0
    return res 

#La diferencia es que aca estoy haciendo una copia de S, no estoy referenciando literalmente a S.
#Chequear esta diferencia utilizando el debugging!

#print(CerosEnPosicionesPares2([1,2,3,4,5,6,7,8]))

#La diferencia entre 2.1 y 2.2 es que en la 2.2 NO PUEDO modificar mi s porque es unicamente de entrada, cuando sale de la funcion
#Tiene que ser igual a como entro porque es in 

"""
3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
sino que borra la vocal y concatena a continuaci´on.
"""


def sin_vocales(palabra:str)-> str:
    vocales: list = ["a","e","i","o","u"]
    res: list = []
    for caracter in palabra:
        if not (caracter in vocales):
            res.append(caracter)

    palabra: str = ''
    for caracter in res:
        palabra += caracter
    return palabra

#print(sin_vocales("murcielago"))

"""
4. problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: {|res| = |s|}
asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘_’) ∨
(¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i] ) ) }
}
"""

def reemplazar_vocales(palabra:str)-> str:
    vocales: list = ["a","e","i","o","u"]
    res: list = []
    for caracter in palabra:
        if not (caracter in vocales):
            res.append(caracter)
        else:
            res.append('_')

    palabra: str = ''
    for caracter in res:
        palabra += caracter
    return palabra

#print(reemplazar_vocales("murcielago"))

"""
5. problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: {|res| = |s|}
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1]}
}
"""

def invertir_palabra(palabra = str) -> list:
    palabra_invertida = []
    i = len(palabra)
    while i > 0:
        palabra_invertida.append(palabra[i-1])
        i -= 1
    return palabra_invertida

def da_vuelta_str(palabra:str)-> str:
    palabra_invertida: str = ''
    for caracter in invertir_palabra(palabra):
        palabra_invertida += caracter
    return palabra_invertida

#print(da_vuelta_str("murcielago"))

"""
6. problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { True }
asegura: {(|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
(0 ≤ i, j < |res| ∧ i̸ = j) → res[i]̸ = res[j])}
}
"""

def eliminar_repetidos(palabra:str)-> str:
    lista_caracteres: list = []
    for caracter in palabra:
        lista_caracteres.append(caracter)

    print(lista_caracteres)
    for caracter in lista_caracteres:
        if caracter in lista_caracteres:
            lista_caracteres.pop()
    
    return lista_caracteres

#print(eliminar_repetidos("paaaaaaaaaatitos"))


#Ejercicio 3 Matrices.
"""
1. problema pertenece a cada uno version 1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
requiere: { True }
asegura: { |res| ≥ |s|}
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e))}
}
Nota: Reutilizar la funci´on pertenece() implementada previamente para listas
"""

def pertenece1 (s=list[int], z=int)-> bool:
    for elemento in s:
        if elemento == z:
            return True
    return False

def pertenece_matrices(s:list[list[int]],e:int, res:list[bool]):
    res.clear()
    for row in s:
        res.append(pertenece1(row,e))

# mi_respuesta= [False,True,False]
# s= [[1,2],[2,1,4],[8,8,1]]
# print(mi_respuesta)
# pertenece_matrices(s,1,mi_respuesta)
# print(mi_respuesta)

#La respuesta que tengo que dar es esto, no hay return porque en la especificacion no dice nada de retornar un valor.


"""
Ejercicio 6. Implementar las siguientes funciones sobre matrices (secuencias de secuencias):
1. problema es matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
requiere: { True }
asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|)}
}
"""

def esMatriz(s:list[list[int]])-> bool:
    #Basicamente la especificacion me dice que la longitud para s en la posicion i tiene que ser igual a la longitud de la primer lista que aparece
    if (len(s)> 0 and len(s[0]) >0):
        for fila in s:
            if not (len(s[0]) == len(fila)):
                return False
        else:
            return True
    else:
        return False

# print(esMatriz(s = [[1,2,3],[4,5,6],[7,8,9]]))
# print(esMatriz(s = [[1,2,3],[4,5,6,4],[7,8,9]]))
# print(esMatriz(s = [[],[4,5,6,4],[7,8,9]]))
# print(esMatriz(s = [[1],[4,5,6,4],[7,8,9]]))
# print(esMatriz(s = [[3,4],[4,5],[7,8,]]))

"""
2. problema filas ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
requiere: { esM atriz(m)}
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
}

"""

# res= [True,False,False]

def filas_ordenadas(m:list[list[int]], res:list[bool]):
    res.clear() # Aca estoy tomando por referencia a la lista res para modificarla dentro de esta funcion.
    for fila in m:
        if ordenados(fila):
            res.append(ordenados(fila))
"""
La especificacion de este problema me esta diciendo que la variable res que es de tipo out significa que no
debe retornar nada la funcion. Esto es que la variable res ya existe antes y luego al llamar a la funcion filas_ordenadas
la misma modifica la variable global res. Pero no la retorna como tal
"""

# print(res)
# print(filas_ordenadas(m=[[1,2,3],[4,5,6],[7,8,9]],res=res))
# print(res)

"""
problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
requiere: { esM atriz(m)}
requiere: { c < |m[0]|}
requiere: { c ≥ 0}
asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en
el mismo orden que aparecen}
}

"""

def columna(m:list[list[int]],c:int) -> list[int]:
    lista_columna : list[int] = [] 
    for fila in m:
        lista_columna.append(fila[c])
    return lista_columna

# print(columna(m=[[1,2,3],[4,5,6],[7,8,9]],c=2))


"""
4. problema columnas ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
requiere: { esM atriz(m)}
asegura: { Para toda columna c ∈ m → (res[c] = true ↔ ordenados(columna(m, c))) }
}
Nota: Reutilizar la funci´on ordenados() implementada previamente para listas
"""

def columnas_ordenadas(m:list[list[int]]) -> list[bool]:
    lista_columnas:list[int] = []
    
    for fila in range(len (m)):
        lista_columnas.append(columna(m,fila))
    
    for i in range(len(lista_columnas)):
        if not (ordenados(lista_columnas[i])):
            return False
    else:
        return True
    

# print(columnas_ordenadas(m=[[4,7,9],[4,5,6],[8,9,10]]))
# print(columnas_ordenadas(m=[[1,2,3],[4,5,6],[7,8,9]]))
# print(columnas_ordenadas(m=[[1,4,8],[4,2,6],[7,8,9]]))
# print(columnas_ordenadas(m=[[8,1,2],[4,5,6],[7,8,9]]))

"""
5. problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
requiere: { esM atriz(m)}
asegura: {Devuelve mt
(o sea la matriz transpuesta)}
}
Nota: Usar columna() para ir obteniendo todas las columnas de la matriz
"""

def transponer(m:list[list[int]])-> list[list[int]]:
    matriz_transpuesta: list[list[int]] = []
    for fila in range(len (m)):
        matriz_transpuesta.append(columna(m,fila))

    return matriz_transpuesta


# print(transponer(m=[[1,2,3],[4,5,6],[7,8,9]]))
# print(transponer(m=[[1,0,3],[6,9,6],[10,2,1]]))
# print(transponer(m=[[1,0],[6,9],[10,1]])) #Tira error porque no respeta la especificacion de columna requiere: { c < |m[0]|}

"""
6. Ta-Te-Ti Tradicional:
problema quien gana tateti (in m:seq⟨seq⟨Char⟩⟩) : Z {
requiere: {esMatriz(m)}
requiere: {|m| = 3}
requiere: {|m[0]| = 3}
requiere: {En la matriz si hay 3 X alineadas verticalmente =⇒ no hay 3 O alineadas verticalmente}
requiere: {En la matriz si hay 3 O alineadas verticalmente =⇒ no hay 3 X alineadas verticalmente}
requiere: {En la matriz si hay 3 X alineadas horizontalmente =⇒ no hay 3 O alineadas horizontalmente}
requiere: {En la matriz si hay 3 O alineadas horizontalmente =⇒ no hay 3 X alineadas horizontalmente}
requiere: {(Para todo i,j ∈ {0, 1, 2}) (m[i][j] = X∨ m[i][j] = O∨ m[i][j] = ” ”)}
asegura: {Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0}
asegura: {Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1}
asegura: {Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2}
}

"""

def pertenece_matrices_aux(s:list[list[str]],e:str) ->list[bool]:
    res = []
    for row in s:
        res.append(pertenece1(row,e))
    return res


def tateti(m:list[list[str]])-> int:

    #Caso 1: hay 3 "O" o 3 "X" alineadas horizontalmente o verticalmente
    #Tateti en diagonal
    for fila in m:
        print(f'la matriz es:',fila)

    if (m[0][0] == m[1][1] == m[2][2]) and m[0][0] == 'x':
        return 1
    elif (m[0][0] == m[1][1] == m[2][2]) and m[0][0] == 'o':
        return 0
        
    # Alineacion de filas
    for fila in m:
        if (pertenece_matrices_aux(fila,"x")) == [True,True,True]:
            return 1
        elif (pertenece_matrices_aux(fila,"o")) == [True,True,True]:
            return 0
        
    #Alineacion de columnas
    for col in transponer(m):
        if (pertenece_matrices_aux(col,"x")) == [True,True,True]:
            return 1
        elif (pertenece_matrices_aux(col,"o")) == [True,True,True]:
            return 0

    return 2


print(tateti([["x","x","o"],["o","x","o"],["x","o","o"]])) #Una fila es tateti res: deberia ser 0
# print(tateti([["x","x","o"],["x","x","o"],["x","o","x"]])) #Una columna es tateti (de x) debería ser 1
# print(tateti([["x","o","o"],["o","x","o"],["x","o","x"]])) #La diagonal de x es tateti res: deberia ser 1
# print(tateti([["o","x","x"],["x","o","x"],["o","x","o"]])) #La diagonal de o es tateti res: debería ser 0
# print(tateti([["o","x","x"],["x","o","o"],["o","x","x"]])) #La diagonal de o es tateti res: debería ser 2


"""
Ejercicio 7. Vamos a elaborar programas interactivos (usando la funci´on input() 3
) que nos permita solicitar al usuario
informaci´on cuando usamos las funciones.
1. Implementar una funci´on para construir una lista con los nombres de mis estudiantes. La funci´on solicitar´a al usuario
los nombres hasta que ingrese la palabra “listo”, o vac´ıo (el usuario aprieta ENTER sin escribir nada). Devuelve la
lista con todos los nombres ingresados.

"""

def ingresar_nombres():
    nombres:list = []
    valor_input = input("Ingrese los nombres de los estudiantes: ")

    while (valor_input != "listo" and valor_input != ""):
        nombres.append(valor_input)
        valor_input = input("Ingrese los nombres de los estudiantes: ")

    return nombres
    
# print(ingresar_nombres())

"""
2. Implementar una funci´on que devuelve una lista con el historial de un monedero electr´onico (por ejemplo la SUBE).
El usuario debe seleccionar en cada paso si quiere:
“C” = Cargar cr´editos,
“D” = Descontar cr´editos,
“X” = Finalizar la simulaci´on (terminar el programa).
En los casos de cargar y descontar cr´editos, el programa debe adem´as solicitar el monto para la operaci´on. Vamos a
asumir que el monedero comienza en cero. Para guardar la informaci´on grabaremos en el historial tuplas que representen
los casos de cargar (“C”, monto a cargar) y descontar cr´edito (“D”, monto a descontar).

"""

def monedero_electronico():
    valor_input = input("Ingrese su operacion:'C' = Cargar créditos,'D' = Descontar créditos,'X' = Finalizar la simulación (terminar el programa). ")
    monedero: list[(str,float)] = []

    while (valor_input == "C" or valor_input == "D"):
        if valor_input == "C":
            cargar_credito: tuple = input("Ingrese su carga en formato ('C',monto a cargar), pulsar X para finalizar: ")
            monedero.append(cargar_credito)
            valor_input = input("Si desea hacer otra carga digite C, si quiere descontar creditos digite D, digite X para finalizar: ")
        elif valor_input == "D":
            descontar_credito: tuple = input("Ingrese su descarga en formato ('D',monto a descargar), pulsar X para finalizar: ")
            monedero.append(descontar_credito)
            valor_input = input("Si desea hacer otra carga digite C, si quiere descontar creditos digite D, digite X para finalizar: ")
        
    return monedero

# print(monedero_electronico())

"""
3. Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo deber´a generar un n´umero
aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deber´a luego preguntarle al usuario si desea seguir sacando otra “carta”
o plantarse. En este ´ultimo caso el programa debe terminar. Los n´umeros aleatorios obtenidos deber´an sumarse seg´un
el n´umero obtenido salvo por las “figuras” (10, 11 y 12) que sumar´an medio punto cada una. El programa debe ir
acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la funci´on devuelve
el historial de “cartas” que hizo que el usuario gane o pierda. Para generar n´umeros pseudo-aleatorios entre 1 y 12
utilizaremos la funci´on random.randint(1,12). Al mismo tiempo, la funci´on random.choice() puede ser de gran
ayuda a la hora de repartir cartas.
"""