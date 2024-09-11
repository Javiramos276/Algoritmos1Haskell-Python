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

