class EmuladorSets:

    def __init__(self, *args):
        self._sets = []
        map(lambda i:self.insertar_item(i), [item for item in args if isinstance(item, list)])

    def __repr__(self):
        return str(self._sets)

    def insertar_item(self, item):
        if item not in self._sets:
                self._sets.append(item)

    def quitar_item(self, item):
        if item in self._sets:
            self._sets.remove(item)

    def __iter__(self):
        return iter(self._sets)


    def __len__(self):
        return len(self._sets)

    def __str__(self):
        return "En esta practica emulamos las colecciones Sets."


    def diferencias_entre_sets(set1, set2):
        diff = EmuladorSets()
        for e1 in set1:
            if e1 not in set2:
                for e2 in set2:
                    if e1 != e2:
                        diff.insertar_item(e1)

        return diff


    def intersecciones_entre_sets(set1, set2):
       return [i for i in set1 if i in set2]



    def comparar_inclusion_entre_sets(set1, set2):
        validacion = False
        if len(set1) == len(set2):
            for e1 in set1:
                for e2 in set2:
                    if e1 == e2:
                        validacion = True
                        break
                    else:
                        validacion = False
                    pass


        else:
            print "Inconsistencia entre Sets"

        return validacion


    def diferencia_simetrica(set1, set2):
        simetria = EmuladorSets()
        for i in set1:
            if i not in set2:
                simetria.insertar_item(i)
        for i in set2:
            if i not in set1:
                simetria.insertar_item(i)

        return simetria

    def producto_cartesiano(set1, set2):
        return ( (c1,c2) for c1 in set1 for c2 in set2)


    def conjunto_potencia(set1):
        potencia = EmuladorSets()
        potencia.insertar_item(None)
        for e1 in set1:
            potencia.insertar_item(e1)


        return potencia

