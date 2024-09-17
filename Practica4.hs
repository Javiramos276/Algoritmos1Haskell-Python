{-


Ejercicio 1. Implementar la funcion fibonacci:: Integer ->Integer que devuelve el i-esimo numero de Fibonacci.
Recordar que la secuencia de Fibonacci se define como:
fib(n) =
    {
        0 si n = 0
        1 si n = 1
        fib(n − 1) + fib(n − 2) en otro caso
    }
-}

fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)

{-
Ejercicio 2. Implementar una funci´on parteEntera :: Float ->Integer segun la siguiente especificacion:

problema parteEntera (x: R) : Z {
    requiere: { x ≥ 0 }
    asegura: { resultado ≤ x < resultado + 1 }
}

-}

parteEntera :: Float -> Integer
parteEntera n = truncate n

{-
Ejercicio 3. Especificar e implementar la funcion esDivisible :: Integer ->Integer ->Bool que dados dos numeros
naturales determinar si el primero es divisible por el segundo. No est´a permitido utilizar las funciones mod ni div.
-}


esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == y = True
                | x < y = False
                | x > y = esDivisible (x - y) y

{-
Ejercicio 4. Especificar e implementar la funci´on sumaImpares :: Integer ->Integer que dado n ∈ N sume los primeros
n n´umeros impares. Por ejemplo: sumaImpares 3 ❀ 1+3+5 ⇝ 9.
-}

sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n | mod n 2 == 1 = n + sumaImpares(n-1)
sumaImpares n | mod n 2 == 0 = sumaImpares(n-1)

{-
        Ejercicio 5. Implementar la funci´on medioFact :: Integer ->Integer que dado n ∈ N calcula n!! = n (n−2)(n−4)· · · .
        problema medioFact (n: Z) : Z {
        requiere: { n ≥ 0 }
        asegura: { resultado =⌊n−12Y⌋i=0(n − 2i) }}
        Por ejemplo:
        medioFact 10 ❀ 10 ∗ 8 ∗ 6 ∗ 4 ∗ 2 ❀ 3840.
        medioFact 9 ❀ 9 ∗ 7 ∗ 5 ∗ 3 ∗ 1 ❀ 945.
        medioFact 0 ❀ 1.
-}

medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact(n-2)

{-

Ejercicio 6. Implementar la funcion todosDigitosIguales :: Integer ->Bool que determina si todos los dıgitos de un
    numero natural son iguales, es decir:
    problema todosDigitosIguales (n: Z) : B {
    requiere: { n > 0 }
    asegura: { resultado = true ↔ todos los dıgitos de n son iguales }
}

-}

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | ultimoDigito /= anteUltimoDigito = False
                      | otherwise = todosDigitosIguales(div n 10)
    where ultimoDigito = mod n 10
          anteUltimoDigito = mod (div n 10) 10


{-
    Ejercicio 7. Implementar la funcion iesimoDigito :: Integer ->Integer ->Integer que dado un n ∈ Z mayor o igual
    a 0 y un i ∈ Z mayor o igual a 1 menor o igual a la cantidad de d´ıgitos de n, devuelve el i-´esimo d´ıgito de n.
    problema iesimoDigito (n: Z, i: Z) : Z {
    requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
    asegura: { resultado = (n div 10cantDigitos(n)−i
    ) mod 10 }
    }

    problema cantDigitos (n: Z) : N {
    requiere: { n ≥ 0 }
    asegura: { n = 0 → resultado = 1}
    asegura: { n ̸= 0 → (n div 10resultado−1 > 0 ∧ n div 10resultado = 0) }
    }
-}
cantidadDigitos :: Integer -> Integer
cantidadDigitos n | n < 10 = 1
                  | otherwise = cantidadDigitos(div n 10) + 1

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | n < 10 = n
                 | cantidadDigitos n == i = ultimoDigito
                 | otherwise = iesimoDigito (div n 10) i
    where ultimoDigito = mod n 10


{-
Un ejemplo de esto sería lo siguiente, supongamos el siguiente numero: 4568
    -> cantidad de digitos ¿4 == 2? No, continua la recursion con el numero 456. ¿3 == 2 ? No, continua con 45. ¿2 == 2? Si, retorna entonces el ultimo numero de n
    4568  2 
    456   2
    45    2  
-}

{-
Ejercicio 10. Especificar, implementar y dar el tipo de las siguientes funciones (s´ımil Ejercicio 4 Pr´actica 2 de Algebra 1).

a) f1(n) = sum desde i=0 hasta n 2^i , n ∈ N0.
-}

sumatoria1 :: Integer -> Integer -> Integer
sumatoria1 i 0 = 1
sumatoria1 i n = 2^n + sumatoria1 i (n-1)

{-
b) f2(n, q) = sum desde i = 0 hasta n q^i , n ∈ N y q ∈ R
-}

sumatoria2 :: Integer -> Integer -> Float -> Float
sumatoria2 i 0 q = 1
sumatoria2 i n q = q^n + sumatoria2 i (n-1) q 

{-
c) f3(n, q) = sum desde i = 1 hasta 2n q^i , n ∈ N y q ∈ R
-}

-- sumatoria3 ::  Integer -> Float -> Float
-- sumatoria3 1 _  = 1
-- sumatoria3 _ q = 2*q
-- sumatoria3 n q = q^(n) + sumatoria2 (n+1) q 

{-
d) f4(n, q) = sum desde i = n hasta 2n q^i , n ∈ N y q ∈ R
-}

sumatoria4 :: Integer -> Float -> Float
sumatoria4 0 q = 1
sumatoria4 n q = q^(n)+ sumatoria4 (n+1) q

{-
Ejercicio 11. a) Especificar e implementar una funci´on eAprox :: Integer ->Float que aproxime el valor del n´umero e
a partir de la siguiente sumatoria:

sum i=0 hasta n de 1/i!

-}

nfactorial :: Integer -> Integer
nfactorial n | n == 0 = 1
             | otherwise = n*nfactorial(n-1)


eAprox :: Integer -> Float
eAprox 1 = 2 --Esto esta bien? O sea si da la funcion pero es raro definirlo asi...
eAprox n = 1 / fromIntegral (nfactorial n) + eAprox(n-1)
-- Aca fromIntegral lo que hace es cambiarme el tipo de la funcion de Integer a Float porque asi lo requiere la funcion "/"

{-
b) Definir la constante e :: Float como la aproximaci´on de e a partir de los primeros 10 t´erminos de la serie anterior.
¡Atenci´on! A veces ciertas funciones esperan un Float y nosotros tenemos un Int. Para estos casos podemos utilizar la
funci´on fromIntegral :: Int ->Float definida en el Preludio de Haskell.

-}

e :: Float
e = eAprox 10

{-
Ejercicio 12. Para n ∈ N se define la sucesi´on:
Lo cual resulta en la siguiente definicion recursiva: a1 = 2, an = 2 + 1
an−1
. Utilizando esta sucesi´on, especificar e implementar
una funci´on raizDe2Aprox :: Integer ->Float que dado n ∈ N devuelva la aproximaci´on de √
2 definida por √
2 ≈ an−1.
Por ejemplo:
raizDe2Aprox 1 ⇝ 1
raizDe2Aprox 2 ⇝ 1,5
raizDe2Aprox 3 ⇝ 1,4
-}

sucesionRecursiva :: Integer -> Float
sucesionRecursiva 1 = 2
sucesionRecursiva n = 2 + 1 / sucesionRecursiva(n-1)

raizDe2Aprox :: Integer -> Float 
raizDe2Aprox n = sucesionRecursiva (n) - 1

{-
Ejercicio 13. Especificar e implementar la siguiente funci´on:

f(n,m) = es una doble sumatoria i^j

-}

-- Esto sería la sumatoria interna
sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna n j = n^j + sumatoriaInterna n (j-1)

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaDoble (n-1) m + sumatoriaInterna n m

{-
Ejercicio 14. Especificar e implementar una funci´on sumaPotencias :: Integer ->Integer ->Integer ->Integer que
dados tres naturales q, n, m sume todas las potencias de la forma q
a+b
con 1 ≤ a ≤ n y 1 ≤ b ≤ m.
-}

sumaPotenciasAux :: Integer -> Integer -> Integer -> Integer 
sumaPotenciasAux q 1 m = q^(1+m)
sumaPotenciasAux q n m = q^(n+m) + sumaPotenciasAux q (n-1) m 

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n 1 = q^(1+n)
sumaPotencias q n m = q^(n+m) + sumaPotencias q n (m-1) + sumaPotenciasAux q n m