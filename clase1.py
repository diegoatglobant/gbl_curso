#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Diego Linayo'

from practicas.clase1 import conjuntos


if __name__ == "__main__":
    # Agregar un elemento al Set.
    # Remover un elemento del Set

    # e1 = conjuntos.EmuladorSets()
    # print e1
    # print repr(e1)
    # e1.insertar_item(1)
    # e1.insertar_item(1)
    # e1.insertar_item(2)
    # e1.insertar_item(2)
    # e1.quitar_item(1)
    # print repr(e1)
    # e1.insertar_item(1)
    # e1.insertar_item(2)
    # e1.insertar_item(6)
    # print "E1 " + repr(e1)
    #
    # e2 = conjuntos.EmuladorSets()
    # for elemento in range(0,4):
    #     e2.insertar_item(elemento)
    # print "E2" + repr(e2)
    #
    # #print repr(e1)





    # Diferencia entre un Set y otro Set.
    e1 = conjuntos.EmuladorSets([5,4,3, 8, 9])
    e2 = conjuntos.EmuladorSets([1,4,3])

    diff = conjuntos.diferencias_entre_sets(e1,e2)
    print "Diff: " + repr(diff)



    # Intersección entre un Set y otro Set.
    #print repr(e3)
    interseccion = conjuntos.intersecciones_entre_sets(e1, e2)
    print "Interseccion: " + repr(interseccion)


    # Un método que determine si un Set está incluído en otro Set.
    # print repr(e3)
    validacion = conjuntos.validacion_elementos_entre_sets(list(e1), list(e1))
    print "Esta un set en otro? " +  repr(validacion)
    validacion = conjuntos.validacion_elementos_entre_sets(list(e1), list(e2))
    print "Esta un set en otro? " + repr(validacion)

    # Diferencia simétrica entre un Set y otro Set.


    # ['diego', 8, 'practica', 7,  "este no es en el primero"]

    simetria = conjuntos.diferencia_simetrica(e1, e2)
    print "Simetria: " + repr(simetria)


    # Potencia de Conjuntos

    potencia = conjuntos.conjunto_potencia(e1)
    print repr(potencia)

