class Matrices:

    def __init__(self, *args):
        self._items = []
        map(lambda i:self.insertar_item(i), [item for item in args if isinstance(item, list)])

    def insertar_item(self, item):
        self._items.append(item)

    def getItems(self):
        return self._items

    def __repr__(self):
        return str(self._items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, key):
        return self._items[key]


    def suma(self, M, N):
        for index,value in enumerate(M):
            self.insertar_item(map(sum, zip(M.getItems()[index], N.getItems()[index])))

    def producto_escalar(self, escalar):
        result = []
        for index,value in enumerate(self.getItems()):
            result.append(map(lambda x: x*escalar, self.getItems()[index]) )

        return result


    def multiplicar(self, m1, m2):
		return Matrices(list(sum(a*b for a,b in zip(m1_filas,m2_columnas)) for m2_columnas in zip(*m2.getItems()) for m1_filas in m1.getItems()))


if __name__ == "__main__":
    m1 = Matrices([10,20,30] , [1,1,1], [1,1,1])
    m2 = Matrices([4,3,4], [4,4,4], [1,1,1])

    m3 = Matrices()
    m3.suma(m1 , m2)
    print repr(m3)

    producto_escalar = m3.producto_escalar(2)
    print repr(producto_escalar)

    result = m3.multiplicar(m1,m2)
    print repr(result)