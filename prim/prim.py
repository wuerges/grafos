from pprint import pformat

class AdjList:
  def __init__(self, n):
    self.adj = [[] for _ in range(n+1)]
    self.n = n

  def add_edge(self, u, v, w):
    self.adj[u].append((w, v))
    self.adj[v].append((w, u))

  def __repr__(self):
    return pformat(self.adj)


from heapq import heappush, heappop

def prim(g):
    total = 0

    # inicializando o conjunto dos visitados como vazio
    vis = [False] * (g.n+1)
    q = []

    # marcando o vertice 1 para ser o primeiro a ser analisado
    heappush(q, (0, 1)) 

    while q:
        (w_u, u) = heappop(q)
        if vis[u]:
            continue
        vis[u] = True
        total += w_u
        print("added {} cost {}".format(u, w_u))

        for (w, v) in g.adj[u]:
            heappush(q, (w, v))
    
    return total, vis

g = AdjList(7)

edges = [(1, 2, 3), (1, 4, 4), \
         (2, 4, 1), (2, 3, 5), (2, 6, 2), \
         (3, 4, 10), (3, 5, 8), \
         (4, 5, 9), \
         (5, 7, 7), \
         (6, 7, 6) ]

for (u, v, w) in edges:
    g.add_edge(u, v, w)

print(g)

print (prim(g))
