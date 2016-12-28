#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Diego Linayo'

from practicas.clase1 import EmuladorSets,Matrices


def pruebas_conjuntos():
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


def pruebas_matrices():
    m1 = Matrices([10,20,30] , [1,1,1], [1,1,1])
    m2 = Matrices([4,3,4], [4,4,4], [1,1,1])

    m3 = Matrices()
    m3.suma(m1 , m2)
    print repr(m3)

    producto_escalar = m3.producto_escalar(2)
    print repr(producto_escalar)

    result = m3.multiplicar(m1,m2)
    print repr(result)

    transpuesta = m1.matriz_transpuesta()
    print repr(transpuesta)

    #print "Imprimir en forma de Matriz"
    print m1


if __name__ == "__main__":

    opcion = raw_input("Ingresa 1 para Conjuntos y 2 Para Matrices: ")

    if opcion == 1:
        pruebas_conjuntos()
    else:
        pruebas_matrices()


