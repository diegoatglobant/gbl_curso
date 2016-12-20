# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'Diego Linayo'



import os

path_to_walk = '/home/diego/Documents/txt/';



def arbol(path ):

    # Contadores para poder tabular segun directorio
    total_archivos = 0
    total_directorios = 0

    # Los archivos ordenados alfabeticamente
    files = sorted(
        (os.path.join(path, filename) for filename in os.listdir(path)),
        key=lambda s: s.lower()
    )

    #print map(lambda item: item+"\n", files)
    for item in files:
        if os.path.isdir(item):
            total_directorios += 1
            print('\x1b[6;30;42m %s \x1b[0m') %item
            arbol(item)
        else:
            total_archivos += 1
            print item

    print "Total Archivos %d total Dirs %d" % (total_archivos, total_directorios)


if __name__ == "__main__":
    arbol(path_to_walk)


