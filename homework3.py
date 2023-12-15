class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def set_numarator(self, new):
        self.numarator = new

    def set_numitor(self, new):
        self.numitor = new

    def __str__(self):
        return f'Fractie: {self.numarator} / {self.numitor}'

    def reducere(self):
        x = self.numitor
        y = self.numarator
        while x != 0:
            x, y = y % x, x
        return y

    def __add__(self, other):
        aux = Fractie(0, 0)
        aux.numarator = self.numarator * other.numitor + self.numitor * other.numarator
        aux.numitor = self.numitor * other.numitor
        aux2 = Fractie(aux.numarator, aux.numitor)
        aux.numarator = aux.numarator // aux2.reducere()
        aux.numitor = aux.numitor // aux2.reducere()
        return aux

    def __sub__(self, other):
        aux = Fractie(0, 0)
        aux.numarator = self.numarator * other.numitor - self.numitor * other.numarator
        aux.numitor = self.numitor * other.numitor
        aux2 = Fractie(aux.numarator, aux.numitor)
        aux.numarator = aux.numarator // aux2.reducere()
        aux.numitor = aux.numitor // aux2.reducere()
        return aux

    def inverse(self):
        aux = Fractie(0, 0)
        aux.numarator = self.numitor
        aux.numitor = self.numarator
        aux = aux.reducere()
        return aux


a = Fractie(3, 3)
b = Fractie(4, 3)
c = Fractie(0, 0)
c = a.__add__(b)
print(c)
c = a.__sub__(b)
print(c)
c = b.inverse()
print(b)
