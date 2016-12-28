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

    def multiply(self, *args):
        print "ll" + str(args)
        return args

    def multiplicar(self, M, N):
        for index,value in enumerate(M):
            self.insertar_item(map(self.multiply, zip(M.getItems()[index], N.getItems()[index])))


if __name__ == "__main__":
    m1 = Matrices([10,20,30] , [1,1,1], [1,1,1])
    m2 = Matrices([4,3,4], [4,4,4], [1,1,1])

    m3 = Matrices()
    m3.suma(m1 , m2)
    print repr(m3)

    producto_escalar = m3.producto_escalar(2)
    print repr(producto_escalar)

    m3.multiplicar(m1,m2)