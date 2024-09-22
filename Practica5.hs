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
principio [_] = []
principio (x:xs) = x : principio xs

{-
4. reverso :: [t] -> [t] seg´un la siguiente especificaci´on:
problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
}
-}

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = ultimo (x:xs) : reverso (principio(x:xs))

{-
Ejercicio 2. Definir las siguientes funciones sobre listas:
1. pertenece :: (Eq t) => t -> [t] -> Bool seg´un la siguiente especificaci´on:
problema pertenece (e: T, s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ e ∈ s }
}
-}

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) | x == y = True
                   | otherwise = pertenece x ys

{-
2. todosIguales :: (Eq t) => [t] -> Bool, que dada una lista devuelve verdadero s´ı y solamente s´ı todos sus elementos son iguales
-}

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:xs) | x == head xs = todosIguales (tail xs)
                    | otherwise = False

{-
3. todosDistintos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema todosDistintos (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
}
-}

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [_] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos (head xs:tail xs)

{-
4. hayRepetidos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema hayRepetidos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
}
-}

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [_] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos (head xs:tail xs)

{-5. quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparici´on de x en
la lista xs (de haberla).
-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x (y:ys) | x == y = ys
                | otherwise = y:quitar x ys

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
6. quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado es igual a s pero sin el elemento e. }
}

-}

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys) | pertenece x (y:ys) = quitarTodos x (quitar x (y:ys))
                     | otherwise = y:ys

{-
7. eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una ´unica aparici´on de cada elemento, eliminando
las repeticiones adicionales.
-}

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = eliminarRepetidos xs  
                         | otherwise = x : eliminarRepetidos xs --aca no estoy obedeciendo el orden... no creo que importe porque no especifica nada el problema

{-
8. mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero s´ı y solamente s´ı
ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:
problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ todo elemento de s pertenece r y viceversa}
}
-}

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos [] _ = False
mismosElementos (x:xs) (y:ys) | pertenece (head conjuntoA) conjuntoB = mismosElementos (tail conjuntoA) conjuntoB
                              | otherwise = False
    where conjuntoA = eliminarRepetidos (x:xs)  
          conjuntoB = eliminarRepetidos (y:ys)

{-
Ejercicio 3. Definir las siguientes funciones sobre listas de enteros:
1. sumatoria :: [Integer] -> Integer seg´un la siguiente especificaci´on:
problema sumatoria (s: seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { resultado =
P|s|−1
i=0 s[i] }
}
-}

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria l = head l + sumatoria (tail l) 

sumatoria2 :: [Integer] -> Integer
sumatoria2 [] = 0
sumatoria2 (x:xs) = x + sumatoria xs 

{-
2. productoria :: [Integer] -> Integer seg´un la siguiente especificaci´on:
problema productoria (s: seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { resultado =
Q|s|−1
i=0 s[i] }
}
-}

productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

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
4. sumarN :: Integer -> [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { T rue }
asegura: {|resultado| = |s| ∧ cada posici´on de resultado contiene el valor que hay en esa posici´on en s sumado
n }
}
-}

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (n+x): sumarN n xs


{-
5. sumarElPrimero :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[0], s) }
}
Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]
-}

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

{-
6. sumarElUltimo :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[|s| − 1], s) }
}
-}

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

{-
7. pares :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { T rue }
asegura: {resultado s´olo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
}
Por ejemplo pares [1,2,3,5,8,2] da [2,8,2]
-}

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x: pares(xs)
             | otherwise = pares (quitar x (x:xs))

{-
8. multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un n´umero n y una lista xs, devuelve una lista
con los elementos de xs m´ultiplos de n.
-}

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN x (y:ys) | mod y x == 0 = y: multiplosDeN x ys
                      | otherwise = multiplosDeN x (quitar y (y:ys))

{-
9. ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
c´omo pueden usar la funcion maximo para que ayude a generar la lista ordenada necesaria.
-}



{-
ordenar
-}

-- minimo :: [Int] -> Int
-- minimo (x:xs) | xs == [] = x
--               | x <= head xs = minimo (x:(tail xs))
--               | otherwise = minimo xs 

-- ordenar :: [Int] -> [Int]
-- ordenar [] = []
-- ordenar x = (minimo x) : (ordenar (quitar (minimo x) x))
