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
    pila_aux.put(primerElemento)
    pila_res: Pila(tuple[str,int]) = Pila()
    


    while not p.empty():
        elementoActual = p.get()
        if maximo < elementoActual[1]:
            pila_res.put(elementoActual)
        pila_aux.put(elementoActual)

    #Vaciamos el contenedor y llenamos la pila original
    while not pila_aux.empty():
        p.put(pila_aux.get())

    tupla_resultado: tuple(str,int) = pila_res.get()

    return tupla_resultado

# pila = Pila()
# pila.put(("alumno1",8)) 
# pila.put(("alumno2",2))
# pila.put(("alumno3",1))
# pila.put(("alumno4",10))
# pila.put(("alumno5",3))
# pila.put(("alumno6",7))
# pila.put(("alumno8",9))
# tupla_res = buscar_nota_maxima(pila)
# print(tupla_res)

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
vamos a considerar palabras a todas aquellas secuencias de caracteres que no tengan espacios en blanco
"""
def pertenece(s=list[str], z=str)-> bool:
    for elemento in s:
        if elemento == z:
            return True
    return False

def separar_palabras(frase:str)->list:
    """
    Dada una frase cualquiera, separa cada palabra en una lista. Es el equivalente a lo que hace la funcion split de python
    """
    palabra_aux:str = ""
    lista_res:list = []
    for caracter in frase:
        if caracter != " ":
            palabra_aux += caracter
        else:
            if palabra_aux != "":
                lista_res.append(palabra_aux)
                palabra_aux = ""

    lista_res.append(palabra_aux)
    return lista_res


# lista_res = separar_palabras("hola    esta es   una frase")
# print(lista_res)

def agrupar_por_longitud(nombre_archivo:str)-> dict:
    archivo = open(nombre_archivo,"r")
    contenido = archivo.readlines()
    dict_res:dict = {}
    for linea in contenido:
        palabras = separar_palabras(linea)
        for palabra in palabras:
            if palabra != "\n" and len(palabra) in dict_res:
                dict_res[len(palabra)] += 1
            elif palabra != "\n":
                dict_res[len(palabra)] = 1

    archivo.close()
    return dict_res

# dict_rest = agrupar_por_longitud("ej16.txt")
# print(dict_rest)

def palabras(lineas:str) -> list[str]:
    return lineas.split()

def agrupar_por_longitud_profes(nombre_archivo:str)-> dict[int,int]:
    archivo = open(nombre_archivo,'r')
    lineas = archivo.readlines()
    dicc: dict[int,int] = {} 
    for linea in lineas:
        for palabra in palabras(linea):
            if len(palabra) in dicc:
                dicc[len(palabra)] += 1
            else:
                dicc[len(palabra)] = 1
    archivo.close()
    return dicc

#dict_res = agrupar_por_longitud_profes("ej16.txt")
#print(dict_res)

#print(contar_lineas("contar_lineas.txt"))
"""
Ejercicio 17. Dada una secuencia de tuplas, donde cada tupla tiene en la primera componente el nombre de un estudiante,
y en la esgunda componenete la nota que sac´o en un examen; se pide devolver un diccionario con los promedios de todos los
estudiantes. La clave del diccionario debe ser el nombre del estudiante, y el valor el promedio de todos sus ex´amenes.
calcular promedio por estudiante(notas : list[tuple[str, float]]) → dict[str, float]
"""

def eliminar_nombres_repetidos(lista:list)-> list:
    lista_resultado: list = []
    for nombre in lista:
        if pertenece(lista,nombre) and not pertenece(lista_resultado,nombre):
            lista_resultado.append(nombre)
    return lista_resultado

# lista_resultado = eliminar_nombres_repetidos(['javier', 'juani', 'javier', 'pepe', 'juani', 'javier', 'javier', 'juani', 'pepito', 'pepito'])


def promedio_por_estudiante(notas: list[tuple[str,float]])-> dict[str,float]:
    dict_res:dict ={}
    cantidad_de_notas:dict = {}
    for (nombre,nota) in notas:
        if nombre not in dict_res:
            dict_res[nombre] = nota
            cantidad_de_notas[nombre] = 1
        else:
            dict_res[nombre] += nota
            cantidad_de_notas[nombre] += 1
        
    for (nombre,nota) in cantidad_de_notas.items():
        dict_res[nombre] = dict_res[nombre]/cantidad_de_notas[nombre]
        
    return dict_res


# diccionario = promedio_por_estudiante([("javier",4),("juani",3),("javier",8),("pepe",10),("juani",6),("javier",9),("javier",8),
#                          ("juani",7),("pepito",2),("pepito",7)])

# print(diccionario)

"""
Ejercicio 18. Implementar la funci´on la palabra mas frecuente(in nombre archivo : str) → str que devuelve la palabra
que m´as veces aparece en un archivo de texto. Se aconseja utilizar un diccionario de palabras para resolver el problema
"""

def palabra_mas_frecuente(nombre_archivo:str)->str:
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    todas_las_palabras_dict:dict[str,int] = {}
    
    #Recorremos cada linea del parrafo
    for linea in lineas:
        #Separamos cada palabra
        todas_las_palabras = separar_palabras(linea)
        for palabra in todas_las_palabras:
            #Si la palabra no se encuentra en el diccionario la agregamos, si no le sumamos 1 a la existente
            if palabra not in todas_las_palabras_dict:
                todas_las_palabras_dict[palabra] = 1
            else:
                todas_las_palabras_dict[palabra] += 1

    maximo = 1
    res = ''
    #Iteramos en los elementos de todas las palabras y buscamos la palabras mas repetida.
    for palabra,apariciones in todas_las_palabras_dict.items():
        if palabra != "\n" and apariciones > maximo:
            maximo = apariciones
            res = palabra
            
    return res

def palabra_mas_frecuente_profes(nombre_archivo:str)-> str:
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    dicc: dict[str,int] = {}
    for linea in lineas:
        for palabra in palabras(linea):
            if palabra in dicc:
                dicc[palabra] += 1
            else:
                dicc[palabra] = 1
    archivo.close()

    res: str = ''
    maximo:int = 0
    for pal in dicc.keys():
        if dicc[pal] > maximo:
            m = dicc[pal]
            res = pal

    return res 


# palabra_mas_frecuente("ej18.txt")

"""
Ejercicio 19. Nos piden desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los
usuarios del sistema. El navegador debe permitir al usuario navegar hacia atr´as y hacia adelante en la historia de navegaci´on.

1. Crea un diccionario llamado historiales que almacenar´a el historial de navegaci´on para cada usuario. Las claves del
diccionario ser´an los nombres de usuario y los valores ser´an pilas.
2. Implementar visitar sitio(inout: historiales:dict[str, Pila[str]], in: usuario:str, in: sitio:str) que reciba el diccionario de historiales, el nombre de usuario y el sitio web visitado. La funci´on debe agregar el sitio web al historial
del usuario correspondiente.
3. Implementar navegar atras(inout: historiales: dict[str, Pila[str]], in: usuario:str) que permita al usuario
navegar hacia atr´as en la historia de navegaci´on. Primero debemos obtener el sitio anterior al actual, y luego poner este
como ´ultimo en la pila

"""

historiales:dict[str,Pila[str]] = {}

def visitar_sitio(historiales:dict[str,Pila[str]], usuario:str, sitio:str):
    pila:Pila[str] = Pila()
    pila.put(sitio)
    if usuario in historiales.keys():
        historiales[usuario] = pila
    else:
        historiales[usuario] = pila

# visitar_sitio(historiales,"javier","google.com")
# visitar_sitio(historiales,"juani","google.com")
# visitar_sitio(historiales,"javier","youtube.com")
# print(historiales)

"""
Ejercicio 20. Nos piden desarrollar un sistema de gesti´on de inventario para una tienda de ropa. Este sistema permite llevar
un registro de los productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y
calcular el valor total del inventario.
Para resolver este problema vamos a utilizar un diccionario llamado inventario que almacene informaci´on sobre los productos.
Cada elemento del diccionario debe tener el nombre del producto como clave y otro diccionario cuya clave sea un string que
indique un atributo del producto (’precio’,’cantidad’) y su valor sea un Float o un Int, dependiendo del atributo clave.
Agregar en las funciones los tipos de datos correspondientes.

1. Implementa una funci´on llamada agregar producto(inout inventario:dict[str, dict[str, float | int]], in nombre:sin precio:float, in cantidad:int) que permita agregar un nuevo producto al inventario. El nombre del producto debe
ser la clave del diccionario, y el valor debe ser otro diccionario con las claves “precio” y “cantidad”. Como requisito de esta
funci´on el producto a agregar no est´a en el inventario.

2. Implementa una funci´on llamada actualizar stock(inout inventario:dict[str, dict[str, float | int]], in nombre:sin cantidad:int) que permita actualizar la cantidad de un producto existente en el inventario.

3. Implementa una funci´on llamada actualizar precios(inout inventario:dict[str, dict[str, float | int]], in
nombre:str, in precio:float) que permita actualizar el precio de un producto existente en el inventario.

4. Implementa una funci´on llamada calcular valor inventario(in inventario:dict[str, dict[str, float | int]])
→ float que calcule el valor total del inventario multiplicando el precio por la cantidad de cada producto y sumando los
valores de todos los productos.
"""

def agregar_producto(inventario:dict[str,dict[str,float]],nombre: str, precio:float,cantidad:int):
    if nombre not in inventario.keys():
        inventario[nombre]= {"precio":precio, "cantidad":cantidad}

def actualizar_stock(inventario:dict[str,dict[str,float]],nombre: str,cantidad:int):
    if nombre in inventario.keys():
        inventario[nombre]["cantidad"] = cantidad

def actualizar_precios(inventario:dict[str,dict[str,float]],nombre: str, precio:float):
    if nombre in inventario.keys():
        inventario[nombre]["precio"] = precio

def valor_inventario(inventario:dict[str,dict[str,float]]):
    valor_total: float = 0
    for producto,dicc in inventario.items():
        valor_total += dicc["precio"]*dicc["cantidad"]

    return valor_total

# inventario:dict[str,dict[str,float]] = {}
# agregar_producto(inventario,"Camisa", 20.0, 50)
# agregar_producto(inventario,"Pantalon", 30.0, 30)
# actualizar_stock(inventario, "Camisa", 10)
# print("el inventario a calcular es ", inventario)
# valor_total = valor_inventario(inventario)
# print(valor_total)

"""
Ejercicio 21. Implementar en Python:

1. Una funci´on contar lineas(in nombre archivo : str) → int que cuenta y devuelva la cantidad de l´ıneas de texto del
archivo dado.

2. Una funci´on existe palabra(in palabra : str, in nombre archivo : str) → bool que dice si una palabra existe en un
archivo de texto o no

3. Una funci´on cantidad apariciones(in nombre archivo : str, in palabra : str) → int que devuelve la cantidad de apariciones de una palabra en un archivo de texto


"""

def contar_lineas(archivo:str):
    archivo = open(archivo,'r')
    a = archivo.readlines()
    res = len(a)
    archivo.close()
    return res

def existe_palabra(palabra:str,nombre_archivo:str)-> bool:
    archivo = open(nombre_archivo,"r")
    lineas = archivo.read()
    palabra_del_texto: str = ""
    for caracter in lineas:
        if caracter != " " and caracter != "\n":
            palabra_del_texto += caracter
            
        else:
            if palabra_del_texto == palabra:
                archivo.close()
                return True
            
            palabra_del_texto = ""

    if palabra_del_texto == palabra:
        archivo.close()
        return True
    
    archivo.close()
    return False
    
    

# print(existe_palabra("esto", "ej20.txt"))

"""
Ejercicio 22. Dado un archivo de texto con comentarios, implementar una funcion
clonar sin comentarios(in nombre archivo : str) que toma un archivo de entrada y genera un nuevo archivo que tiene el
contenido original sin las lıneas comentadas. Para este ejercicio vamos a considerar comentarios como aquellas l´ıneas que tienen
un car´acter ‘#’como primer car´acter de la l´ınea, o si no es el primer car´acter, se cumple que todos los anteriores son espacios.
Ejemplo:
# esto es un comentario
# esto tambien
esto no es un comentario # esto tampoco
"""

def clonar_sin_comentarios(archivo_entrada:str,archivo_salida:str):
    arch_entrada = open(archivo_entrada,"r")
    arch_salida = open(archivo_salida,"w")
    lineas = arch_entrada.readlines()
    for linea in lineas:
        if not ((pertenece(linea,"#")) and (linea[0] == "#")):
            arch_salida.write(linea)

    arch_entrada.close()
    arch_salida.close()

def es_comentario(linea:str)->bool:
    return sacar_espacios(linea)[0] == "#"

def sacar_espacios(linea:str)-> str:
    res = ''
    for letra in linea:
       if letra != ' ':
           res += letra

    return res


#clonar_sin_comentarios("ej22.txt","contar_lineas.txt")
"""
Ejercicio 23. Dado un archivo de texto, implementar una funci´on invertir lineas(in nombre archivo : str), que escribe un
archivo nuevo llamado reverso.txt que tiene las mismas l´ıneas que el original, pero en el orden inverso.
Ejemplo: si el archivo original es
Esta es la primera linea .
Y esta es la segunda .
debe generar:
Y esta es la segunda .
Esta es la primera linea .
"""

def invertir_lineas(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    reverso = open("reverso.txt","w")
    pila = Pila()
    for linea in lineas:
        pila.put(linea)

    while not pila.empty():
        reverso.write(pila.get())


# invertir_lineas("ej23.txt")

"""
Ejercicio 24. Dado un archivo de texto y una frase, implementar una funci´on
agregar frase al final(in nombre archivo : str, in frase : str), que la agregue al final del archivo original (sin hacer una
copia).

"""

def agregar_frase_al_final(nombre_archivo:str, frase:str):
    archivo = open(nombre_archivo,"r")
    copiar_frase = []
    lineas = archivo.readlines()
    for linea in lineas:
        copiar_frase.append(linea) 

    copiar_frase.append(frase)
    archivo.close()
    archivo = open(nombre_archivo,"w")
    
    for linea in copiar_frase:
        archivo.write(linea)

    archivo.close()
    print(copiar_frase)

# agregar_frase_al_final("ej24.txt","esta es mi frase agregada")

"""
Ejercicio 25. Dado un archivo de texto y una frase, implementar una funci´on
agregar frase al principio(in nombre archivo : str, in frase : str), que agregue la frase al comienzo del archivo original
(similar al ejercicio anterior, sin hacer una copia del archivo).

"""

def agregar_frase_al_principio(nombre_archivo:str, frase:str):
    archivo = open(nombre_archivo,"r")
    cola = Cola()
    lineas = archivo.readlines()
    cola.put(frase)
    cola.put("\n") #Agregamos un salto de linea

    for linea in lineas:
        cola.put(linea) 

    archivo.close()
    archivo = open(nombre_archivo,"w")
    
    while not cola.empty():
        archivo.write(cola.get())

    archivo.close()

agregar_frase_al_principio("ej25.txt","otra frase agregada")