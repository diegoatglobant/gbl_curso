# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'Diego Linayo'

import os

def arbol(path , nivel= 0 ):

    # Contadores para poder tabular segun directorio
    total_archivos = 0
    total_directorios = 0

    # Los archivos ordenados alfabeticamente
    files = sorted(
        (os.path.join(path, filename) for filename in os.listdir(path)),
        key=lambda s: s.lower()
    )
    if nivel is not 0:
        nivel_tab = "|" + "\t" * nivel + "|--- "
    else:
        nivel_tab = "\t" * nivel + "|--- "


    for item in files:
        if os.path.isdir(item):
            total_directorios += 1
            #print nivel_tab +  ('\x1b[6;30;42m %s \x1b[0m') % os.path.basename(item) + "- " + item + "Nivel " + str(nivel)
            print nivel_tab +  ('\x1b[6;30;42m %s \x1b[0m') % os.path.basename(item)
            #print "\t" +  "Total Archivos %d total Dirs %d" % (total_archivos, total_directorios)
            arbol(item, nivel + 1)
        else:
            total_archivos += 1
            print nivel_tab + ""+ os.path.basename(item)



if __name__ == "__main__":
    path_to_walk = '/home/diego/Documents/txt/';
    arbol(path_to_walk)


