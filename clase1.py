#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Diego Linayo'

from practicas.clase1 import EmuladorSets,Matrices


if __name__ == "__main__":
    # Agregar un elemento al Set.

    e1 = EmuladorSets()
    e1.insertar_item("a")
    e1.insertar_item("b")
    e1.insertar_item("c")
    e1.insertar_item("d")

    e2 = EmuladorSets()
    e2.insertar_item("d")
    e2.insertar_item("e")
    e2.insertar_item("f")
    e2.insertar_item("g")


    e3 = EmuladorSets(['a','b'])

    # Diferencia entre un Set y otro Set.
    diff = EmuladorSets.diferencias_entre_sets(e1,e2)
    print "Diff: " + repr(diff)


    # Intersección entre un Set y otro Set.
    interseccion = EmuladorSets.intersecciones_entre_sets(e1, e2)
    print "Interseccion: " + repr(interseccion)



    # Un método que determine si un Set está incluído en otro Set.
    validacion = EmuladorSets.comparar_inclusion_entre_sets(e1, e1)
    print "Esta un set en otro? " +  repr(validacion)

    validacion = EmuladorSets.comparar_inclusion_entre_sets(e2, e3)
    print "Esta un set en otro? " + repr(validacion)



    # Diferencia simétrica entre un Set y otro Set.
    simetria = EmuladorSets.diferencia_simetrica(e1, e2)
    print "Diff Simetrica: " + repr(simetria)

    #Producto cartesiano entre un Set y otro Set.
    producto_cartesiano = EmuladorSets.producto_cartesiano(e1,e2)
    print "Producto Cartesiano: " + str(list(producto_cartesiano))

    # Potencia de Conjuntos
    #potencias = conjuntos.conjunto_potencia()


