from pprint import pprint, pformat

class Muf:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    def __repr__(self):
        return pformat((self.root, self.rank))

    # ultra lento no python, cuidado!
    def find_rec(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def find(self, x):
        todo = []
        while self.root[x] != x:
            todo.append(x)
            x = self.root[x]
        for t in todo:
            self.root[t] = x
        return x        


    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.root[xroot] = yroot
            self.rank[yroot] += self.rank[xroot]
        else:
            self.root[yroot] = xroot
            self.rank[xroot] += self.rank[yroot]

print("criada Muf vazia, com 5 conjuntos")
m = Muf(5)
pprint(m)

print("unidos conjuntos #0 e #1")
m.union(0, 1)
pprint(m)

print("unidos conjuntos #1 e #2")
m.union(1, 2)
pprint(m)

print("unidos conjuntos #3 e #4")
m.union(3, 4)
pprint(m)

print("unidos conjuntos #2 e #3")
m.union(2, 3)
pprint(m)
