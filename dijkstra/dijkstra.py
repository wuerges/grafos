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

def spfa(g, source):
    inf = int(1e9)

    # inicializando o custos dos vertices
    cost = [inf] * (g.n+1)
    pred = [0] * (g.n+1)
    
    q = []

    # considerando o custo da fonte como 0
    cost[source] = 0
    pred[source] = source

    # marcando o vertice 1 para ser o primeiro a ser analisado
    heappush(q, (0, source)) 

    while q:
        (_, u) = heappop(q)

        for (w, v) in g.adj[u]:
            if cost[u] + w < cost[v]:
                print("relaxed {}: cost {} => {}".format((u, v), cost[v], cost[u]+w))
                cost[v] = cost[u] + w
                pred[v] = u
                heappush(q, (cost[v], v))
    
    return cost, pred

g = AdjList(7)

edges = [(1, 2, 3), (1, 4, 6), \
         (2, 4, 1), (2, 3, 5), (2, 6, 2), \
         (3, 4, 10), (3, 5, 8), \
         (4, 5, 9), \
         (5, 7, 1), \
         (6, 7, 6) ]

for (u, v, w) in edges:
    g.add_edge(u, v, w)

print(g)

print (spfa(g, 1))
