
{-
2023 Segundo Cuatrimestre

¡Vamos Campeones!
En exactas se está jugando un torneo de fútbol y la facultad le pidió a los alumnos de IP programar algunas
funcionalidades en Haskell, Los datos con los que contamos para esto son los nombres de los equipos que participan
del torneo, los nombres de los arqueros titulares de cada uno de dichos equipos, y la cantidad de goles recibidos
por esos arqueros. Los nombres de los equipos y sus respectivos arqueros serán modelados mediante tuplas de tipo
(String, String), donde la primera componente representa el nombre del equipo, y la segunda representa el nombre
del arquero titular de dicho equipo.
En los problemas en los cuales se reciben como parámetros secuencias arquerosPorEquipo y goles, cada posición de
la lista goles representará la cantidad de goles recibidos por el arquero del equipo que se encuentra en esa misma
posicion de arquerosPorEquipo. Por ejemplo, si la lista arquerosPorEquipo es [("Sacachispas", "Neyder Aragon"),
("Fenix", "Nahuel Galardi")] y la lista de goleses [3, 5], eso indicaría que Neyder Aragon recibió 3 goles, y
Nahuel Galardi 5.

Se pueden usar las siguientes funciones del preludio:
	- Listas: head, tail, last, init, length, elem, ++
	- Tuplas: fst, snd
	- Operaciones Lógicas: &&, ||, not
	- Constructores de listas: (x:xs), []
	- Constructores de tuplas: (x, y)


1) Atajaron Suplentes
problema atajaronSuplentes (arquerosPorEquipo: seq<String X String>, goles: seq<Z>, totalGolesTorneo: Z): Z {
	requiere: {equiposValidos(arquerosPorEquipo)
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {La suma de todos los elementos de goles es menor o igual a totalGolesTorneo}
	asegura: {
	res es la cantidad de goles recibidos en el torneo por arqueros que no son titulares en sus equipos.
	}
}


2) Equipos Válidos
problema equiposValidos (arquerosPorEquipo: seq<String X String>): Bool {
	requiere: {True}
	asegura: {
	(res = True) <=> arquerosPorEquipo no contiene nombres de clubes repetidos, ni arqueros repetidos, ni jugadores con nombre del club
	}
}


3) Porcentaje de goles
problema porcentajeDeGoles (arquero: String, arquerosPorEquipo: seq<String X String>, goles: seq<Z>): R {
	requiere: {La segunda componente de algún elemento de arquerosPorEquipo es arquero}
	requiere: {equiposValidos(arquerosPorEquipo)}
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {Hay al menos un elemento de goles mayores estricto a 0}
	asegura: {
	res es el porcentaje de goles que recibió arquero sobre el total de goles recibidos por arqueros titulares
	}
}

Para resolver este ejercicio pueden utilizar la siguiente función que devuelve como float la división entre dos
numeros de tipo Int.

division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b


4) Valla Menos Vencida
problema vallaMenosVencida (arquerosPorEquipo: seq<String X String>, goles: seq<Z>): String {
	requiere: {equiposValidos(arquerosPorEquipo)}
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {|goles| > 0}
	asegura: {
	res es alguno de los arqueros de arquerosPorEquipo que menor goles recibió de acuerdo a goles
	}
}

-}

-- Solucion ejercicio 1
{-

1) Atajaron Suplentes
problema atajaronSuplentes (arquerosPorEquipo: seq<String X String>, goles: seq<Z>, totalGolesTorneo: Z): Z {
	requiere: {equiposValidos(arquerosPorEquipo)
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {La suma de todos los elementos de goles es menor o igual a totalGolesTorneo}
	asegura: {
	res es la cantidad de goles recibidos en el torneo por arqueros que no son titulares en sus equipos.
	}
}
-}

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

atajaronSuplentes :: [(String,String)] -> [Integer] -> Integer -> Integer
atajaronSuplentes [] [0] 0 = 0 -- Caso base 1, que no haya equipo, no hay goles no hay nada
atajaronSuplentes [x] [y] totalgoles = totalgoles - y
atajaronSuplentes (x:xs) (y:ys) totalgoles = golesASuplentes
    where golesASuplentes = totalgoles - sumatoria (y:ys)


-- Solucion ejercicio 2 --
{-
2) Equipos Válidos
problema equiposValidos (arquerosPorEquipo: seq<String X String>): Bool {
	requiere: {True}
	asegura: {
	(res = True) <=> arquerosPorEquipo no contiene nombres de clubes repetidos, ni arqueros repetidos, ni jugadores con nombre del club
	}
}
-}

perteneceArqueros :: (Eq t) => t -> [(t,t)] -> Bool
perteneceArqueros nombre [] = False
perteneceArqueros nombre (x:xs)| nombre == snd x = True  
                               | otherwise = perteneceArqueros nombre xs

perteneceClubes :: (Eq t) => t -> [(t,t)] -> Bool
perteneceClubes nombre [] = False
perteneceClubes nombre (x:xs)| nombre == fst x = True  
                             | otherwise = perteneceClubes nombre xs

seRepitenClubes :: [(String,String)] -> Bool
seRepitenClubes [] = False
seRepitenClubes [x] = False 
seRepitenClubes ((a,b):xs)| perteneceClubes a xs = True --seRepitenClubes(head xs:tail xs)
                          | otherwise = seRepitenClubes (head xs:tail xs)

seRepitenArqueros :: [(String,String)] -> Bool
seRepitenArqueros [] = False
seRepitenArqueros [(a,b)] = False
seRepitenArqueros ((a,b):xs) | perteneceArqueros b xs = True
                             | otherwise = seRepitenArqueros (head xs:tail xs)

equipoYNombreIguales :: [(String,String)] -> Bool
equipoYNombreIguales [] = False
equipoYNombreIguales [x]| fst x == snd x = True
                        | otherwise = False
equipoYNombreIguales (x:xs)| fst (head xs) == snd (head xs) = True
                           | otherwise = equipoYNombreIguales xs


equiposValidos :: [(String,String)] -> Bool
equiposValidos [] = True
equiposValidos [x] | equipoYNombreIguales [x] = False
                   | otherwise = True
equiposValidos (x:xs) | seRepitenClubes (x:xs) = False
                      | equipoYNombreIguales (x:xs) = False
                      | seRepitenArqueros (x:xs) = False
                      | otherwise = True

-- Solucion ej 3 --
{-
3) Porcentaje de goles
problema porcentajeDeGoles (arquero: String, arquerosPorEquipo: seq<String X String>, goles: seq<Z>): R {
	requiere: {La segunda componente de algún elemento de arquerosPorEquipo es arquero}
	requiere: {equiposValidos(arquerosPorEquipo)}
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {Hay al menos un elemento de goles mayores estricto a 0}
	asegura: {
	res es el porcentaje de goles que recibió arquero sobre el total de goles recibidos por arqueros titulares
	}
}
-}

division :: Integer -> Integer -> Float
division a b = fromIntegral a / fromIntegral b

               
hallarGolesConvertidos :: String -> [(String,String)] -> [Integer] -> Integer
hallarGolesConvertidos arquero [] [0] = 0
hallarGolesConvertidos arquero [x] [y] | perteneceArqueros arquero [x] = y
                                       | otherwise = 0
hallarGolesConvertidos arquero (x:xs) (y:ys)| arquero == snd x = y  
                                            | otherwise = hallarGolesConvertidos arquero xs ys

porcentajeDeGoles :: String -> [(String,String)] -> [Integer] -> Float
porcentajeDeGoles arquero [x] goles| perteneceArqueros arquero [x] && goles == [0] = 0
                                   | perteneceArqueros arquero [x] = 100
                                   | otherwise = 0
porcentajeDeGoles arquero (x:xs) (y:ys) = division (golesConvertidosAlArquero * 100) golesTotales
    where golesTotales = sumatoria (y:ys)
          golesConvertidosAlArquero = hallarGolesConvertidos arquero (x:xs) (y:ys)


{-
4) Valla Menos Vencida
problema vallaMenosVencida (arquerosPorEquipo: seq<String X String>, goles: seq<Z>): String {
	requiere: {equiposValidos(arquerosPorEquipo)}
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {|goles| > 0}
	asegura: {
	res es alguno de los arqueros de arquerosPorEquipo que menor goles recibió de acuerdo a goles
	}
}
-}

