import qualified Control.Applicative as 0
-- Ejercicio 1. a) Implentar la funcion parcial f :: Integer -> Integer definida por extension de la siguiente manera:

funcionf :: Integer -> Integer
funcionf 1 = 8
funcionf 4 = 131
funcionf 16 = 16

-- b) Analogamente, especificar e implementar la función parcial g :: Integer ->Integer

funciong :: Integer -> Integer
funciong 8 = 16
funciong 16 = 4
funciong 131 = 1

-- c) A partir de las funciones definidas en los item 1 y 2, implementar las funciones parciales h = f ◦ g y k = g ◦ f

funcionh :: Integer -> Integer
funcionh n = funcionf(funciong n)

funcionk :: Integer -> Integer
funcionk n = funciong(funcionf n)

-- Ejercicio 2. ⋆ Especificar e implementar las siguientes funciones, incluyendo su signatura

-- a) absoluto: calcula el valor absoluto de un numero entero

absoluto :: Integer -> Integer
absoluto n | n < 0 = (-1)*n
           | otherwise = n

-- b) maximoabsoluto: devuelve el maximo entre el valor absoluto de dos numeros enteros.

maximoabsoluto :: Integer -> Integer -> Integer
maximoabsoluto a b | absoluto a > absoluto b = a
                   | absoluto a < absoluto b = b
                   | otherwise = a

-- c) maximo3: devuelve el maximo entre tres numeros enteros.

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c | (a>b) && (b>c) = a
              | (b>c) = b
              | otherwise = c

-- d) algunoEs0: dados dos numeros racionales, decide si alguno de los dos es igual a 0 (hacerlo dos veces, una usando pattern matching y otra no).

algunoEs0 :: Float -> Float -> Bool
algunoEs0 a b = a == 0 || b == 0

-- Usando pattern Matching

algunoEs0pm :: Float -> Float -> Bool
algunoEs0pm 0 _ = True
algunoEs0pm _ 0 = True
algunoEs0pm _ _ = False

-- e) ambosSon0: dados dos numeros racionales, decide si ambos son iguales a 0 (hacerlo dos veces, una usando pattern matching y otra no).

ambosSon0 :: Float -> Float -> Bool
ambosSon0 a b = (a == 0) && (b == 0)

-- Usando pattern Matching

ambosSon0pm :: Float -> Float -> Bool
ambosSon0pm 0 0 = True
ambosSon0pm _ _ = False

-- f) mismoIntervalo: dados dos numeros reales, indica si estan relacionados considerando la relacion de equivalencia en R
-- cuyas clases de equivalencia son: (−∞, 3],(3, 7] y (7, ∞), o dicho de otra forma, si pertenecen al mismo intervalo.

{-

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo a b | a == b = True
                   | a >= b 
-}

-- g) sumaDistintos: que dados tres numeros enteros calcule la suma sin sumar repetidos (si los hubiera)

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c | (a == b) && (b == c) = 0
                    | (a == b) = c
                    | (b == c) = a
                    | otherwise = a+b+c

-- h) esMultiploDe: dados dos numeros naturales, decidir si el primero es multiplo del segundo

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b = mod b a == 0 


-- i) digitoUnidades: dado un numero entero, extrae su dıgito de las unidades
-- esto vendria a ser que si tengo el numero 73 el digito que tengo que devolver es 3

digitoUnidades :: Integer -> Integer
digitoUnidades a = mod a 10


-- j) digitoDecenas: dado un numero entero mayor a 9, extrae su dıgito de las decenas.
-- Esto sería que si tengo un numero por ejemplo 390 me devuelva 9

digitoDecenas :: Integer -> Integer
digitoDecenas a = div(mod a 100) 10

{-

Ejercicio 3. Implementar una funcion estanRelacionados :: Integer -> Integer -> Bool
problema estanRelacionados (a:Z, b:Z) : Bool {
    requiere: {a ̸= 0 ∧ b ̸= 0}
    asegura: {(res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para alg´un k ∈ Z con k ̸= 0)}
}
Por ejemplo:
estanRelacionados 8 2 ⇝ True porque existe un k = −4 tal que 82 + 8 × 2 × (−4) = 0.
estanRelacionados 7 3 ⇝ False porque no existe un k entero tal que 72 + 7 × 3 × k = 0.

-}

{- Resolución:

Si trabajo un poco con la expresión puedo hacer lo siguiente: a^2+a*b*k = 0, o dicho de otra manera,
a^2 = -a*b*k donde aca puedo dividir por a ya que por hipótesis sabemos que a /= 0, entonces
a= -k*b o lo que es equivalente a decir que el resto entre a y b será 0 ya que existe algun multiplo que los
relaciona. En definitiva, estoy resolviendo lo mismo que en el ejercicios 2f con la funcion esMultiploDe 

-}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = mod b a == 0

-- Ejercicio 4. ⋆ Especificar e implementar las siguientes funciones utilizando tuplas para representar pares, ternas de numeros.

-- a) prodInt: calcula el producto interno entre dos tuplas R × R.

prodInt :: (Integer, Integer) -> (Integer, Integer) ->  Integer
prodInt (a,b) (c,d) = a * c + b * d

-- b) todoMenor: dadas dos tuplas R×R, decide si es cierto que cada coordenada de la primera tupla es menor a la coordenada
-- correspondiente de la segunda tupla.

todoMenor :: (Integer,Integer) -> (Integer,Integer) -> Bool
todoMenor (a,b) (c,d) = (a < c) && (b < d) 

-- c) distanciaPuntos: calcula la distancia entre dos puntos de R2
{-
    Para calcular la distancia entre dos puntos teniamos que calcular sqr((x2-x1)^2 + (y2-y1)^2 )
-}

distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (x1,y1) (x2,y2) = sqrt((x2-x1)^2 + (y2-y1)^2)


-- d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.

sumaTerna :: (Float,Float,Float) -> Float
sumaTerna (a,b,c) = a+b+c

{-
    e) sumarSoloMultiplos: dada una terna de n´umeros enteros y un natural, calcula la suma de los elementos de la terna que
    son m´ultiplos del n´umero natural. Por ejemplo:
    sumarSoloMultiplos (10,-8,-5) 2 ⇝ 2
    sumarSoloMultiplos (66,21,4) 5 ⇝ 0
    sumarSoloMultiplos (-30,2,12) 3 ⇝ -18
-}

sumarSoloMultiplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) d | (mod a d == 0) && (mod b d == 0) && (mod c d == 0) = a+b+c
                             | (mod b d == 0) && (mod c d == 0) = b+c
                             | (mod c d == 0) = c
                             | otherwise = 0

-- f) posPrimerPar: dada una terna de enteros, devuelve la posici´on del primer n´umero par si es que hay alguno, y devuelve 4 si son todos impares
posPrimerPar :: (Integer,Integer,Integer) -> Integer
posPrimerPar (a,b,c) | mod a 2 == 0 = 0
                     | mod b 2 == 0 = 1
                     | mod c 2 == 0 = 2
                     | otherwise = 4

-- g) crearPar :: a ->b ->(a, b): crea un par a partir de sus dos componentes dadas por separado (debe funcionar para elementos de cualquier tipo).

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

--h) invertir :: (a, b) -> (b, a): invierte los elementos del par pasado como par´ametro (debe funcionar para elementos de cualquier tipo).

invertir :: (a, b) -> (b, a)
invertir (a,b) = (b, a)

-- i) Reescribir los ejercicios prodInt, todoMenor y distanciaPuntos usando el siguiente renombre de tipos: type Punto2D= (Float, Float)
-- Este no entiendo bien que significa

{-
    Ejercicio 5. Implementar la funcion todosMenores :: (Integer, Integer, Integer) ->Bool
    problema todosMenores (t : Z × Z × Z) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
    }
    problema f (n: Z) : Z {
    requiere: {True}
    asegura: {(n ≤ 7 → res = n^2) ∧ (n > 7 → res = 2n − 1)}
    }
    problema g (n: Z) : Z {
    requiere: {True}
    asegura: {Si n es un numero par, entonces res = n/2, en caso contrario, res = 3n + 1}
    }

-}

f :: Integer -> Integer
f n | n<=7 = n^2
    | otherwise = 2*n - 1

g :: Integer -> Integer
g n | (mod n 2) == 0 = div n 2
    | otherwise = 3*n + 1

todosMenores :: (Integer,Integer,Integer) -> Bool
todosMenores (a,b,c) = (f a > g a) && (f b > g b) && (f c > g c)

{-
    Ejercicio 6. Usando los siguientes tipos:
    type Anio = Integer
    type EsBisiesto = Bool
    Programar una funcion bisiesto :: Anio -> EsBisiesto segun la siguiente especificacion:
    problema bisiesto (año: Z) : Bool {
    requiere: {True}
    asegura: {res =  false ↔ año no es multiplo de 4, o año es multiplo de 100 pero no de 400}
    }
    Por ejemplo:
    bisiesto 1901 ⇝ False, bisiesto 1904 ⇝ True,
    bisiesto 1900 ⇝ False, bisiesto 2000 ⇝ True.

-}

{-
    la frase 
    "falso ↔  año no es multiplo de 4, o año es multiplo de 100 pero no de 400"
    Es equivalente a decir:
    "verdadero ↔ año es multiplo de 4, o año es multiplo de 400 pero no de 100"

    Todos los años bisiestos son divisibles entre 4.
    Aquellos años que son divisibles entre 4, pero no entre 100, son bisiestos.
    Los años que son divisibles entre 100, pero no entre 400, no son bisiestos.
    Sin embargo, los años divisibles entre 100 y entre 400 sí que son bisiestos.
-}

{-
bisiesto :: Integer -> Bool
bisiesto anio | (mod anio 4) == 0 && (mod anio 100) == 0 -- Si el año es divisible por 4 entonces en principio tiene potencial de ser un año bisiesto
              | (mod anio 4) == 0 
              | (mod anio 400) 

-}

{-
        Ejercicio 7. a) Implementar una funcion:
        distanciaManhattan:: (Float, Float, Float) ->(Float, Float, Float) ->Float
        problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
        requiere: {True}
        asegura: {res = P2 i=0 |pi − qi|}
        }
        Por ejemplo:
        distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
        distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8

-}

distanciaManhattan :: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (a,b,c) (d,e,f) = abs(a-d) + abs(b-e) + abs(c-f)

--b) Reimplementarla teniendo en cuenta el siguiente tipo: type Coordenada3d = (Float, Float, Float) Esto no se bien que significa todavia

{-
    Ejercicio 8. Implementar una funcion comparar :: Integer ->Integer ->Integer
    problema comparar (a:Z, b:Z) : Z {
    requiere: {True}
    asegura: {(res = 1 ↔ sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
    asegura: {(res = −1 ↔ sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
    asegura: {(res = 0 ↔ sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
    }
    problema sumaUltimosDosDigitos (x: Z) : Z {
    requiere: {True}
    asegura: {res = (|x| mod 10) + (⌊(|x|/10)⌋ mod 10)}
    }
    Por ejemplo:
    comparar 45 312 ⇝ -1 porque 45 ≺ 312 y 4 + 5 > 1 + 2.
    comparar 2312 7 ⇝ 1 porque 2312 ≺ 7 y 1 + 2 < 0 + 7.
    comparar 45 172 ⇝ 0 porque no vale 45 ≺ 172 ni tampoco 172 ≺ 45

-}

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = abs x `mod`  10 +  (abs x `div` 10) `mod` 10 

comparar :: Integer -> Integer -> Integer 
comparar a b | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
             | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
             | sumaUltimosDosDigitos(a) == sumaUltimosDosDigitos(b) = 0

-- Ejercicio 9. A partir de las siguientes implementaciones en Haskell, describir en lenguaje natural que hacen y especificarlas.

{-
    a) f1 :: Float -> Float
    f1 n | n == 0 = 1
    | otherwise = 0

    La funcion f1 toma un parametro Flotante y devuelve como resultado otro flotante.
    Su función es que si n es igual a 0 entonces el resultado de la funcion es 1, para otro caso el resultado será 0.
    Basicamente f1 es una funcion partida que vale f(0)=1 y f(n) = 0 para cualquier n /= 0
-}

{-

b) f2 :: Float -> Float
    f2 n | n == 1 = 15
         | n == -1 = -15

    La funcion f2 toma como parametro de entrada un flotante y devuelve un flotante como parametro de salida.
    Para f(1)= 15 y f(-1) = -15 para otro caso no hay especificaciones dadas.
-}

{-
c) f3 :: Float -> Float
    f3 n | n <= 9 = 7
         | n >= 3 = 5

    La funcion f3 toma como parametro de entrada un flotante y devuelve un flotante como parametro de salida.
    Para valores menores que 3 la funcion retornara 5, para valores entre 3 y 9 retornara 7 y para valores mayores que 9 retornara 7
    Esto se debe a que la condicion en la que entra primero es la primera que aparece leyendo de arriba hacia abajo y de izquierda a derecha.

-}

{-
    d) f4 :: Float -> Float -> Float
    f4 x y = ( x + y )/2

    La funcion f4 toma dos parametros de entrada, ambos flotantes y retorna como parametro de salida otro flotante.
    Especificamente la funcion retorna la suma de los parametros de entrada divido 2
-}

{-
    e) f5 :: ( Float , Float ) -> Float
        f5 (x , y ) = ( x + y )/2

    La funcion f5 toma como parametro de entrada una tupla de numeros flotantes y retorna como resultado un flotante.
    Especificamente, toma cada elemento de la tupla, los suma y divide el resultado por 2.
-}

{-
    f) f6 :: Float -> Int -> Bool
        f6 a b = truncate a == b

    La funcion f6 toma como parametro de entrada un Flotante y un Entero y devuelve como resultado un Booleano.
    La funcion verifica lógicamente si el entero mas cercano al parametro a es igual al parametro b. En caso de que 
    sea verdadero retorna True, caso contrario False  
-}