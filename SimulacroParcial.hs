module SimulacroParcial where


{- Solucion ejercicio 1 -}
invertir :: (String,String) -> (String,String)
invertir (a,b) = (b,a)

invertirLista :: [(String,String)] -> [(String,String)]
invertirLista [] = []
invertirLista [x] = [invertir x]
invertirLista (x:xs) = invertir x: invertirLista xs

pertenece :: (String,String) -> [(String,String)] -> Bool
pertenece (z,v) [] = False
pertenece (z,v) (x:xs)| (z,v) == x = True
                      | otherwise = pertenece (z,v) xs

eliminarRepetidos :: [(String,String)] -> [(String,String)]
-- Esta funcion elimina todos los elementos repetidos de tuplas en la listas y tambien los invertidos.
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | pertenece x xs || pertenece x (invertirLista xs) = eliminarRepetidos xs
                         | otherwise = x: eliminarRepetidos xs

relacionesValidas :: [(String,String)]-> Bool
relacionesValidas (x:xs) | (x:xs) == eliminarRepetidos (x:xs) = True
                         | otherwise = False


{- Solucion ejercicio 2 -}

personas :: [(String,String)] -> [String]
personas [x] = [fst x, snd x]
personas (x:xs) = quitarNombresRepetidos ([fst x,snd x] ++ personas xs)

perteneceNombres :: [String] -> [String] -> Bool
perteneceNombres a [] = False
perteneceNombres a (x:xs)| a == [x] = True
                         | otherwise = perteneceNombres a xs

quitarNombresRepetidos :: [String] -> [String]
quitarNombresRepetidos [] = []
quitarNombresRepetidos [x] = [x]
quitarNombresRepetidos (x:xs)| perteneceNombres [x] xs = quitarNombresRepetidos xs
                             | otherwise = x:quitarNombresRepetidos xs

{- Solucion ejercicio 3 -}

amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((a,b):xs)
  | persona == a = b : amigosDe persona xs
  | persona == b = a : amigosDe persona xs
  | otherwise = amigosDe persona xs

{- Solucion ejercicio 4 -}

cantidadDeAmigos :: String -> [(String,String)] -> Integer
cantidadDeAmigos nombre [] = 0
cantidadDeAmigos nombre [(a,b)] | nombre == a || nombre == b = 1
                                | otherwise = 0
cantidadDeAmigos nombre ((a,b):xs)| nombre == a || nombre == b  = 1 + cantidadDeAmigos nombre xs
                                  | otherwise = cantidadDeAmigos nombre xs

perteneceNombre :: String -> [(String,String)] -> Bool
perteneceNombre x [] = False
perteneceNombre x (y:ys)| x == fst y = True
                        | otherwise = perteneceNombre x ys

darNombreYAmigos :: String -> [(String,String)] -> [(String,Integer)]
darNombreYAmigos nombre [] = [(nombre,0)]
darNombreYAmigos nombre [(a,b)] = [(nombre,cantidadDeAmigos nombre [(a,b)])]
darNombreYAmigos nombre (x:xs)| perteneceNombre nombre (x:xs) = [(nombre,cantidadDeAmigos nombre (x:xs))]
                              | otherwise = (nombre,cantidadDeAmigos nombre (x:xs)):darNombreYAmigos 

-- personaConMasAmigos :: [(String,String)] -> String
-- personaConMasAmigos ((a,b):xs) | cantidadDeAmigos a ((a,b):xs) > cantidadDeAmigos b ((a,b):xs) = personaConMasAmigos xs
--                                | otherwise = 


