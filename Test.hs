-- Ejemplos con Test 
import Test.HUnit
import Practica5

run = runTestTT testsFibo
run2 = runTestTT testsacarBlancosRepetidos

testsFibo = test [
    "Casobase 1 : fib 0" ~: fib 0 ~?= 0,
    "Casobase 2 : fib 1" ~: fib 1 ~?= 1,
    "Casorecursivo 1 : fib 2" ~: fib 2 ~?= 1   
    ]

testsacarBlancosRepetidos = test [
    "Casobase 1 : SBR " ~: sacarBlancosRepetidos [' '] ~?= [' '],
    "Casobase 2 : SBR 2 elementos" ~: sacarBlancosRepetidos [' ',' '] ~?= [' '],
    "Casobase 3 : SBR +2 elementos" ~: sacarBlancosRepetidos [' ','h','o','l','a'] ~?= [' ','h','o','l','a'],
    "Casobase 4 : SBR con palabras + espacios" ~: sacarBlancosRepetidos [' ',' ','h','o','l','a'] ~?= [' ','h','o','l','a'],
    "Casobase 5 : SBR con espacio al final y al principio" ~: sacarBlancosRepetidos [' ',' ','h','o','l','a',' ',' '] ~?= [' ','h','o','l','a',' ']   
    ]
