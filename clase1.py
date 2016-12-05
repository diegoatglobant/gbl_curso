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
    e3 = conjuntos.EmuladorSets([1,2,3])
    e4 = conjuntos.EmuladorSets([1,4,3])
    #print repr(e3)
    interseccion = conjuntos.intersecciones_entre_sets(e3, e4)
    print "Interseccion: " + repr(interseccion)


    # Un método que determine si un Set está incluído en otro Set.
    e5 = conjuntos.EmuladorSets([9, 3, "diego", 5, 8])
    e6 = conjuntos.EmuladorSets([5, 9, 3, "diego", 8])
    # print repr(e3)
    validacion = conjuntos.validacion_elementos_entre_sets(e5, e6)
    print "Esta un set en otro? " +  repr(validacion)

    # Diferencia simétrica entre un Set y otro Set.

    e7 = conjuntos.EmuladorSets([9, 3, "diego", 5, 8])
    e8 = conjuntos.EmuladorSets([5, 9, 3, "practica", 7, "este no es en el primero"])

    # ['diego', 8, 'practica', 7,  "este no es en el primero"]

    simetria = conjuntos.diferencia_simetrica(e7, e8)
    print "Simetria: " + repr(simetria)


    # Producto cartesiano entre un Set y otro Set.

    e10 = conjuntos.EmuladorSets([1,2,3])
    potencia = conjuntos.conjunto_potencia(e10)
    print repr(potencia)

