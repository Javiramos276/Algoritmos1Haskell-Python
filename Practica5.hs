{-
Ejercicio 1. Definir las siguientes funciones sobre listas:
. longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos
-}

longitud :: [t] -> Integer
longitud [] = 0
longitud l = 1 + longitud(tail l)

{-
2. ultimo :: [t] -> t seg´un la siguiente especificaci´on:
problema ultimo (s: seq⟨T ⟩) : T {
requiere: { |s| > 0 }
asegura: { resultado = s[|s| − 1] }
}
-}

ultimo :: [t] -> t
ultimo [l] = l
ultimo l = ultimo (tail(l)) 

{-
3. principio :: [t] -> [t] seg´un la siguiente especificaci´on:
problema principio (s: seq⟨T ⟩) : seq⟨T ⟩ {
requiere: { |s| > 0 }
asegura: { resultado = subseq(s, 0, |s| − 1) }
}
-}

principio :: [t] -> [t]
principio [] = []
principio (x:xs) = ultimo (x:xs)


{-5. quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparici´on de x en
la lista xs (de haberla).

-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == head (y:ys) = quitar x ys
                | otherwise = ys

{-
Resolucion hecha por los profes
-}

quitarProfes :: (Eq t) => t -> [t] -> [t]
quitarProfes x [] = []
quitarProfes x xs | x == head xs = tail xs
                  | otherwise = [head xs] ++ quitarProfes x (tail xs)

quitarProfes2 :: (Eq t) => t -> [t] -> [t]
quitarProfes2 n [] = []
quitarProfes2 n (x:xs) | n == x = xs
                       | otherwise = x:(quitarProfes2 n xs)

{-

3. maximo :: [Integer] -> Integer seg´un la siguiente especificaci´on:
problema maximo (s: seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
}

-}

maximo :: [Integer] -> Integer 
maximo (x:xs) | xs == [] = x
              | x >= head xs = maximo (x:(tail xs))
              | otherwise = maximo xs 



{-

Ejercicio 17 fibonacci
-}

-- esFibonacci :: Integer -> Bool
-- esFibonacci 0 = True
-- esFibonacci 1 = True
-- esFibonacci n | n == esFibonacciAux n 1  = True
--               | n > esFibonacciAux n 1 = False
--               | otherwise = esFibonacci n

-- fibAux :: Integer -> Integer
-- fibAux 0 = 0
-- fibAux 1 = 1
-- fibAux b  = fibAux(b-1) + fibAux(b-2)

{-
Aca voy a tener que usar esta funcion auxiliar para poder hacer una iteracion a la fibAux, es decir,
el parametro m aca deberia aumentar de a 1 para hacer la iteracion en fibAux
-}

-- esFibonacciAux :: Integer -> Integer -> Integer
-- esFibonacciAux n m | n < fibAux m = esFibonacciAux n m+1
--                    | n == fibAux m = n
--                    | otherwise = 

{-
ordenar
-}

minimo :: [Int] -> Int
minimo (x:xs) | xs == [] = x
              | x <= head xs = minimo (x:(tail xs))
              | otherwise = minimo xs 

ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar x = (minimo x) : (ordenar (quitar (minimo x) x))
