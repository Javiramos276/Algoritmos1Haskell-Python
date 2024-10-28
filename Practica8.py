"""
1. Pilas
Ejercicio 1. Implementar una funci´on generar nros al azar(in cantidad : int, in desde : int, in hasta : int) → Pila[int]
que genere una pila de cantidad de n´umeros enteros al azar en el rango [desde, hasta].
Pueden usar la funci´on random.randint(< desde >, < hasta >) y la clase LifoQueue() que es un ejemplo de una implemen-
taci´on b´asica:
from queue import LifoQueue as Pila
p = Pila ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # vacia ?
"""
from queue import LifoQueue as Pila
import random
from queue import Queue as Cola


def generar_nros_al_azar(cantidad:int, desde:int, hasta:int)-> Pila[int]:
    p = Pila ()
    i = 0

    while i <= cantidad:
        numeros = random.randint(desde,hasta)
        p.put(numeros)
        i += 1

    while not p.empty():
       print(p.get()) 

    return p

#print(generar_nros_al_azar(8,1,10))
"""
Ejercicio 2. Implementar una funci´on cantidad elementos(in p : Pila) → int que, dada una pila, cuente y devuelva la can-
tidad de elementos que contiene. No se puede utilizar la funci´on LifoQueue.qsize(). Si se usa get() para recorrer la pila, esto
modifica el par´ametro de entrada. Y como la especificaci´on dice que es de tipo in hay que restaurarla
"""

#No olvidarse que cuando la pila es de tipo in hay que regenerarla!!!

def cantidad_elementos(p:Pila)-> int:
    contador = 0
    pila_aux = Pila()

    #Obtenemos la cantidad de elementos, vaciamos la pila p que entro como parametro in
    while not p.empty():
        elemento_pila = p.get()
        contador += 1
        pila_aux.put(elemento_pila)

    #Utilizamos la pila auxiliar para restaurar la pila original y luego accedemos a ella por fuera de la funcion
    #Con un bucle while
    while not pila_aux.empty():
        p.put(pila_aux.get())

    return contador

#
#pila = Pila()
#pila.put(1)
#pila.put(2)
#pila.put(14)
#pila.put(19)
#print(cantidad_elementos(pila))
#
#while not pila.empty():
#    print(pila.get())

"""
Ejercicio 3. Dada una pila de enteros, implementar una funci´on buscar el maximo(in p : Pila[int]) → int que devuelva el
m´aximo elemento.
"""

def maximo(s=list[int]) -> int:
    maximo_valor = s[0]
    i = 0  

    while i < len(s) - 1:
        if s[i + 1] > maximo_valor:  
            maximo_valor = s[i + 1]  
        i += 1  
    
    return maximo_valor

def buscar_el_maximo(p: Pila)-> int:
    pila_aux = Pila()
    lista_numeros = []

    #Obtenemos los elementos de la pila y los agregamos a la lista
    while not p.empty():
        elemento = p.get() 
        lista_numeros.append(elemento)
        pila_aux.put(elemento)    
        
    #Restauramos la pila original
    while not pila_aux.empty():
        p.put(pila_aux.get())

    return maximo(lista_numeros)

#pila = Pila()
#pila.put(3)
#pila.put(8)
#pila.put(-1)
#pila.put(2)
#
#print(f'el maximo es: ', buscar_el_maximo(pila))
#
#while not pila.empty():
#    print(pila.get())

"""
Resolucion hecha por los profesores
"""
def buscar_el_maximo_profes(p:Pila)-> int:
    contenedor : Pila[int] = Pila()
    primerElemento = p.get()
    maximo = primerElemento
    contenedor.put(maximo)

    while not p.empty():
        elementoActual = p.get()
        if maximo < elementoActual:
            maximo = elementoActual
        contenedor.put(elementoActual)

    #Vaciamos el contenedor y llenamos la pila original
    while not contenedor.empty():
        p.put(contenedor.get())

    return maximo
"""
Ejercicio 4. Dada una pila de tuplas de string x enteros, implementar una funci´on buscar nota maxima(in p : Pila[tuple[str, int]]) → que devuelva la tupla donde aparece la m´axima nota (segunda componente de la tupla). La pila no est´a vac´ıa, no hay valores en
las segundas posiciones repetidas en la pila
"""

def buscar_nota_maxima(p: Pila(tuple[str,int])) -> tuple([str,int]):
    pila_aux = Pila()
    primerElemento: tuple = p.get()
    maximo: int = primerElemento[1]
    pila_aux.put(maximo)

    while not p.empty():
        elementoActual = p.get()
        if maximo < elementoActual:
            maximo = elementoActual
        pila_aux.put(elementoActual)

    #Vaciamos el contenedor y llenamos la pila original
    while not pila_aux.empty():
        p.put(pila_aux.get())

"""
Ejercicio 13. Bingo: un cart´on de bingo contiene 12 n´umeros al azar en el rango [0, 99].
1. implementar una funci´on armar secuencia de bingo() → Cola[int] que genere una cola con los n´umeros del 0 al 99
ordenados al azar.
2. implementar una funci´on jugar carton de bingo(in carton : list[int], in bolillero : Cola[int]) → int que toma un
cart´on de Bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la cantidad de
jugadas de ese bolillero que se necesitan para ganar
"""

def armar_secuencia_bingo()-> Cola[int]:
    lista = []
    contenedor = Cola()
    #Creamos una lista con 100 valores
    for i in range(0,100):
        lista.append(i)

    random.shuffle(lista) #a random.shuffle se le pasa una lista de y retorna dicha lista con los valores desordenados
    for numero in lista:
        contenedor.put(numero)

    return contenedor

contenedor = armar_secuencia_bingo()
while not contenedor.empty():
    contenedor.get()

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    bingo : int = 0
    jugadas: int = 0
    contenedor: Cola[int] = Cola()

    while bingo < len(carton):
        jugadas += 1
        bolita_actual = bolillero.get()
        contenedor.put(bolita_actual)
        if bolita_actual in carton:
            bingo += 1

    #Saque todas las bolitas del bolillero
    while not bolillero.empty():
        contenedor.put(bolillero.get())

    #Pongo todas las bolitas del contenedor en el bolillero
    while not contenedor.empty():
        bolillero.put(contenedor.get())

    return jugadas


"""
Ejercicio 17. Dada una secuencia de tuplas, donde cada tupla tiene en la primera componente el nombre de un estudiante,
y en la esgunda componenete la nota que sac´o en un examen; se pide devolver un diccionario con los promedios de todos los
estudiantes. La clave del diccionario debe ser el nombre del estudiante, y el valor el promedio de todos sus ex´amenes.
calcular promedio por estudiante(notas : list[tuple[str, float]]) → dict[str, float]
"""

