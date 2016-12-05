class EmuladorSets:

    def __init__(self):
        self._sets = []

    def __init__(self, *args):
        self._sets = []
        for item in args:
            #print type(item)
            if isinstance(item, list):
                #print "entra aca"
                for i in item:
                    self.insertar_item(i)
            #else:
            #print "entra aca 2"
            #self.insertar_item(item)

    def __repr__(self):
        return str(self._sets)

    def insertar_item(self, item):
        if item not in self._sets:
                self._sets.append(item)

    def quitar_item(self, item):
        if item in self._sets:
            self._sets.remove(item)

    # Sin esto no se puede Iterar
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
    set_intersecciones = EmuladorSets()
    for i in set1:
        if i in set2:
            set_intersecciones.insertar_item(i)
            # print "Elemento %s" % str(i)
    for i in set2:
        if i in set1:
            set_intersecciones.insertar_item(i)
            # print "Elemento %s" % str(i)

    return set_intersecciones

def validacion_elementos_entre_sets(set1, set2):
    validacion = False
    if len(set1) == len(set2):
        #print "Tienen la misma dimension"
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
            # print "Elemento %s" % str(i)
    for i in set2:
        if i not in set1:
            simetria.insertar_item(i)
            # print "Elemento %s" % str(i)

    return simetria

def producto_cartesiano(set1, set2):
    pc = EmuladorSets()
    for e1 in set1:
        for e2 in set2:
            tmp_par = e1, e2
            pc.insertar_item(tmp_par)
    return pc


def conjunto_potencia(set1):
    potencia = EmuladorSets()
    potencia.insertar_item(None)
    for e1 in set1:
        potencia.insertar_item(e1)


    return potencia

