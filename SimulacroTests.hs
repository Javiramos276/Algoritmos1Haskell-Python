import Test.HUnit
import SimulacroParcial

run = runTestTT tests

tests = test [
    "Caso 1: Tupla sin repetir" ~: relacionesValidas [("ana","pedro"),("javi","pepe")] ~?= True,
    "Caso 2: Tupla repetida" ~: relacionesValidas [("ana","pedro"),("ana","pedro")] ~?= False,
    "Caso 3: Tupla invertida" ~: relacionesValidas [("ana","pedro"),("pedro","ana")] ~?= False,
    "Caso 4: Tupla multiple" ~: relacionesValidas [("ana","pedro"),("javi","pepito"),("juancito","donpepe")] ~?= True
    ]