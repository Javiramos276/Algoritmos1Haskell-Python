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
Ejercicio 5. Implementar una funci´on esta bien balanceada(in s : str) → bool que dado un string con una formula aritm´etica
sobre los enteros, diga si los par´entesis est´an bien balanceados. Las f´ormulas pueden formarse con:
los n´umeros enteros
las operaciones b´asicas +, −, x y /
par´entesis
espacios
Entonces las siguientes son formulas aritm´eticas con sus par´entesis bien balanceados:
1 + ( 2 x 3 − ( 2 0 / 5 ) )
10 ∗ ( 1 + ( 2 ∗ ( −1)))
Y la siguiente es una formula que no tiene los par´entesis bien balanceados:
1 + ) 2 x 3 ( ( )
"""

def esta_bien_banalceada(s:str)-> bool:
    for caracter in s:
        print(caracter)

# print(esta_bien_banalceada("1 + (2 x 3)"))


"""
Ejercicio 6.
"""

def pertenece(caracter:str, lista:list)-> bool:
    for letra in lista:
        if letra == caracter:
            return True
    return False


def evaluar(n:float,operando:str,m:float)-> float:
    if operando == "+":
        return n+m
    elif operando == "-":
        return n-m
    elif operando == "*":
        return n*m
    elif operando == "/":
        return n/m


def evaluar_expresion(s:str)-> float:
    pila_operandos: Pila(float) = Pila() #Los operandos son los numeros
    pila_operadores: Pila(str) = Pila() #Son las operaciones (+,-,*,/)
    pila_resultado: Pila(float) = Pila()
    lista_operandos = ["+","-","*","/"]

    for caracter in s:
        if (not pertenece(caracter,lista_operandos) and (caracter != " ")):
            pila_operandos.put(caracter)
        elif caracter != " ":
            pila_operadores.put(caracter)

    while not pila_operadores.empty():
        while not pila_operandos.empty():
            operando1 = float(pila_operandos.get())
            operador = pila_operadores.get()
            operando2 = float(pila_operandos.get())
            res = evaluar(operando1,operador,operando2)
            pila_resultado.put(res)


    print(pila_operandos.queue)
    print(pila_operadores.queue)
    print(pila_resultado.queue)
    return True
    

# evaluar_expresion("3 4 + 5 *")

"""
Ejercicio 7. Implementar una funci´on que dadas dos pilas de igual longitud devuelve una nueva pila con los elementos intercalados. intercalar(p1:Pila, p2:Pila)->Pila. El tope de la pila resultado ser´a el tope de la p2. Nota: Ojo que hay que
recorrer dos veces para que queden en el orden apropiado al final.
"""


def intercalar_pilas(p1:Pila,p2:Pila)-> Pila:
    pila_aux1: Pila= Pila()
    pila_aux2: Pila= Pila()
    pila_res: Pila = Pila()

    #Invertimos la pila p1 y la pila p2
    while not p1.empty():
        pila_aux1.put(p1.get())
        pila_aux2.put(p2.get())

    # Para cada elemento dentro de las pilas, los obtenemos y lo retornamos en la pila resultado
    while not pila_aux1.empty():
        pila_res.put(pila_aux1.get())
        pila_res.put(pila_aux2.get())


    return pila_res

# pila = Pila()
# pila.put(1)
# pila.put(2)
# pila.put(3)
# pila.put(4)
# pila.put(5)
# pila2 = Pila()
# pila2.put(6)
# pila2.put(7)
# pila2.put(8)
# pila2.put(9)
# pila2.put(10)
# pila_res = intercalar_pilas(pila,pila2)
# print(pila_res.queue)

"""
Ejercicio 8. Implementar una funci´on generar nros al azar(in cantidad : int, in desde : int, in hasta : int) → Cola[int]
que genere una cola de cantidad de n´umeros enteros al azar en el rango [desde, hasta]. Pueden usar la funci´on random.randint(< desde >y la clase Queue() que es un ejemplo de una implementaci´on b´asica de una Cola:
"""

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int)-> Cola[int]:
    cola: Cola = Cola()

    for i in range(cantidad):
        numero = random.randint(desde,hasta)
        cola.put(numero)

    return cola

# cola = generar_nros_al_azar(100,2,28)
# print(cola.queue)

"""
Ejercicio 9. Implementar una funci´on cantidad elementos(in c : Cola) → int que, dada una cola, cuente y devuelva la cantidad de elementos que contiene. Comparar con la versi´on usando pila. No se puede utilizar la funci´on Queue.qsize().
"""

def cantidad_elementos_cola(c:Cola)-> int:
    cola_aux: Cola = Cola()
    contador: int = 0

    #Si la cola no esta vacia, llenamos una cola auxiliar para reconstruir la cola principal y sumamos 1 al contador
    while not c.empty():
        cola_aux.put(c.get())
        contador += 1
    
    #Reconstruimos la pila original
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return contador

# cola = Cola()
# cola.put(1)
# cola.put(2)
# cola.put(3)
# cola.put(4)
# contador = cantidad_elementos_cola(cola)
# print(contador)

"""
Ejercicio 10. Dada una cola de enteros, implementar una funci´on buscar el maximo(in c : Cola[int]) → int que devuelva el
m´aximo elemento. Comparar con la versi´on usando pila.
"""

def buscar_maximo_cola(c:Cola[int])-> int:
    cola_aux: Cola = Cola()
    maximo:int = c.get() # En principio, pensamos que el máximo es el primer elemento de nuestra cola
    cola_aux.put(maximo)

    while not c.empty():
        elemento = c.get()
        #Obtenemos el primer elemento de la cola y verificamos si es mayor a nuestro maximo y llenamos la cola aux para reconstruir nuestra cola
        if elemento > maximo:
            maximo = elemento
        cola_aux.put(elemento)

    #Reconstruimos la cola
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return maximo

# c = Cola()
# c.put(1)
# c.put(4)
# c.put(14)
# c.put(7)
# c.put(-2)
# maximo_de_la_cola = buscar_maximo_cola(c)
# print(maximo_de_la_cola)
# print(c.queue)

"""
Ejercicio 11. Dada una cola de tuplas de string x enteros, implementar una funci´on buscar nota minima(in c : Cola[str, int]) → int
que devuelva la tupla donde aparece la m´ınima nota (segunda componente de la tupla). La cola no est´a vac´ıa, no hay valores en
las segundas posiciones repetidas en la cola.
"""

def nota_minima_colas(c:Cola[str,int])-> int:
    cola_aux: Cola = Cola()
    primer_tupla = c.get()
    minimo = primer_tupla[1]
    cola_aux.put(primer_tupla)

    #Verificamos si la nota es la minima y llenamos la cola auxiliar
    while not c.empty():
        tupla = c.get()
        nota = tupla[1]
        if nota < minimo:
            minimo = nota
        cola_aux.put(tupla)

    #Recreamos la cola original
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return minimo

# c = Cola()
# c.put(("algebra",2))
# c.put(("ip",7))
# c.put(("ip2",1))
# c.put(("algoritmos3",8))
# c.put(("algebracomputacional",10))

# minimo = nota_minima_colas(c)
# print(minimo)
# print(c.queue)

"""
Ejercicio 12. Implementar una funci´on que dadas dos colas de igual longitud devuelve una nueva cola con los elementos
intercalados. intercalar(c1:Cola, c2:Cola)->Cola. El primer elemento de la cola resultado ser´a el primer elemento de la c1.
"""

def intercalar_colas(c1:Cola,c2:Cola) -> Cola:
    cola_res: Cola = Cola()
   
    # Para cada elemento dentro de las pilas, los obtenemos y lo retornamos en la pila resultado
    while not c1.empty():
        cola_res.put(c1.get())
        cola_res.put(c2.get())

    return cola_res

# c1 = Cola()
# c1.put(1)
# c1.put(2)
# c1.put(3)
# c1.put(4)
# c1.put(5)
# c2 = Cola()
# c2.put(6)
# c2.put(7)
# c2.put(8)
# c2.put(9)
# c2.put(10)

# cola_res = intercalar_colas(c1,c2)
# print(cola_res.queue)

"""
Ejercicio 13. Bingo: un cart´on de bingo contiene 12 n´umeros al azar en el rango [0, 99].
1. implementar una funci´on armar secuencia de bingo() → Cola[int] que genere una cola con los n´umeros del 0 al 99
ordenados al azar.
2. implementar una funci´on jugar carton de bingo(in carton : list[int], in bolillero : Cola[int]) → int que toma un
cart´on de Bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la cantidad de
jugadas de ese bolillero que se necesitan para ganar.
"""

def armar_sec_bingo()-> Cola[int]:
    bolillero: Cola[int] = Cola()
    lista: list = list()

    for i in range(1,100):
        lista.append(i)
    
    random.shuffle(lista) #a random.shuffle se le pasa una lista de y retorna dicha lista con los valores desordenados
    for numero in lista:
        bolillero.put(numero)

    return bolillero

def jugar_carton_de_bingo(carton:list[int], bolillero: Cola[int])-> int:
    numeros_del_carton:int = 12
    cantidad_de_bolas_lanzadas:int = 0
    bolillero_aux:Cola[int] = Cola()

    # Vamos sacando numeros el bolillero, si en algun momento coincide un numero con alguno del carton entonces nos queda 1 posibilidad menos
    while not bolillero.empty() and numeros_del_carton > 0:
        bolita = bolillero.get()
        if pertenece(bolita,carton):
            numeros_del_carton -= 1
        cantidad_de_bolas_lanzadas += 1
        bolillero_aux.put(bolita)

    #Reconstruimos el bolillero
    while not bolillero_aux.empty():
        bolillero.put(bolillero_aux.get())

    return cantidad_de_bolas_lanzadas

# bolillero = armar_sec_bingo()
# carton = [1,8,13,4,23,98,38,54,18,22,33,55]
# cantidad_de_bolas_lanzadas = jugar_carton_de_bingo(carton, bolillero) #Consultar si es una cuestion estadistica que la cantidad de jugadas siempre me da un numero bastaaaante grande
# print(cantidad_de_bolas_lanzadas)
# print(carton)
# print(bolillero.queue)

"""
Ejercicio 14. Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atenci´on
para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la mas urgente
y requiere atenci´on inmediata) junto con su nombre y la especialidad m´edica que le corresponde.
Implementar la funci´on n pacientes urgentes(in c : Cola[tuple[int, str, str]]) → int que devuelve la cantidad de pacientes de la cola que tienen prioridad en el rango [1, 3].
"""

def n_pacientes_urgentes(c:Cola[tuple[int,str,str]])-> int:
    cola_aux: Cola[tuple[int,str,str]] = Cola()

    cantidad_pacientes_urgentes = 0

    while not c.empty():
        paciente: tuple[int,str,str] = c.get()
        condicion_paciente = paciente[0]
        cola_aux.put(paciente)
        if condicion_paciente <= 3:
            cantidad_pacientes_urgentes += 1
    
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return cantidad_pacientes_urgentes

# c = Cola()
# c.put((7,"a","b"))
# c.put((2,"f","q"))
# c.put((6,"a","b"))
# c.put((8,"c","f"))
# c.put((1,"c","f"))
# c.put((1,"c","f"))
# c.put((3,"c","f"))
# cantidad_pacientes_urgentes = n_pacientes_urgentes(c)
# print(cantidad_pacientes_urgentes)
# print(c.queue)

"""
Ejercicio 15. La gerencia de un banco nos pide modelar la atenci´on de los clientes usando una cola donde se van registrando
los pedidos de atenci´on. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que est´a a la
entrada: Nombre y Apellido, DNI, tipo de cuenta (si es preferencial o no) y si tiene prioridad por ser adulto +65, embarazada o
con movilidad reducida (prioridad si o no).
La atenci´on a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
bancaria preferencial y por ´ultimo el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
1. Dar una especificaci´on para el problema planteado.
2. Implementar atencion a clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que dada la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.

"""

"""
1. La especificacion para este problema sería:

problema pedidos(clientes: Cola[Tuple[nombre: str, apellido: str, dni:int, es_preferencial: bool, es_prioridad: bool]])-> cola
    requiere: {clientes tenga todos los campos distinto de vacio}
    asegura: {La cola retornada se ordena por prioridad, bancaria preferencial y el resto.}
    asegura: {se respeta el orden de llegada para cada subgrupo}

"""

def clientes(c:Cola[tuple[str,int,bool,bool]])-> Cola[tuple[str,int,bool,bool]]:
    cola_aux: Cola[tuple[str,int,bool,bool]] = Cola()
    cola_prioritarios: Cola[tuple[str,int,bool,bool]] = Cola()
    cola_preferenciales: Cola[tuple[str,int,bool,bool]] = Cola()
    cola_clientes_comunes: Cola[tuple[str,int,bool,bool]] = Cola()
    cola_resultado: Cola[tuple[str,int,bool,bool]] = Cola()

    while not c.empty():
        cliente = c.get() #esto es una tupla de 4 elementos
        cola_aux.put(cliente)
        #Si el cliente es es prioridad lo agregamos primero a la cola ordenada
        if cliente[3]:
            cola_prioritarios.put(cliente)
        #Si el cliente tiene cuenta preferencial lo agregamos segundo a la cola ordenada
        elif cliente[4]:
            cola_preferenciales.put(cliente)
        #Para otro caso agregamos el resto
        else:
            cola_clientes_comunes.put(cliente)

    #Metemos los clientes prioritarios a los resultados.
    while not cola_prioritarios.empty():
        cola_resultado.put(cola_prioritarios.get())

    #Metemos los clientes prioritarios a los resultados.
    while not cola_preferenciales.empty():
        cola_resultado.put(cola_preferenciales.get())

    #Metemos los clientes prioritarios a los resultados.
    while not cola_clientes_comunes.empty():
        cola_resultado.put(cola_clientes_comunes.get())
    #Vuelvo a construir la cola con la que empece
    while not cola_aux.empty():
        c.put(cola_aux.get())

    return cola_resultado

# c = Cola()
# c.put(("javier","ramos",42193292,False,False))
# c.put(("Horacio","Ramos",15552395,True,False))
# c.put(("Alejandra","Corbetto",15552225,False,True))
# c.put(("Juan","Benitez",38292496,False,False))
# c.put(("Juan","Perez",38292496,True,False))
# c.put(("Juan","Ayala",42112321,False,True))
# cola_ordenada = clientes(c)

# while not cola_ordenada.empty():
#     print(cola_ordenada.get())

# print(f'la cola con la que empece es:', c.queue)

"""
3. Diccionarios.

Ejercicio 16. Leer un archivo de texto y agrupar la cantidad de palabras de acuerdo a su longitud. Implementar la funci´on
agrupar por longitud(in nombre archivo : str) → dict
que devuelve un diccionario {longitud en letras : cantidad de palabras}.
Ej el diccionario
{
1: 2 ,
2: 10 ,
5: 4
}
indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 4 palabras de longitud 5. Para este ejercicio
vamos a considerar palabras a todas aquellas secuencias de caracteres que no tengan espacios en blanco.

"""

def agrupar_por_longitud(nombre_archivo:str)-> dict:
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    longitud_letras:int = 0
    cantidad_de_palabras:int = 0
    contador:int = 0
    diccionario: dict = {}
    for caracter in contenido:
        if caracter != ' ':
            longitud_letras,contador += 1

        
        
    archivo.close()


agrupar_por_longitud("ej16.txt")