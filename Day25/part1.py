import sys
import networkx as nx
import matplotlib.pyplot as plt

g = {}
for line in sys.stdin:
    src,*dests = line.strip().split()
    if src[:-1] not in g: g[src[:-1]] = set()
    g[src[:-1]].update(dests)
    for dest in dests:
        if dest not in g: g[dest] = set()
        g[dest].add(src[:-1])

# G = nx.Graph()
# for u,vs in g.items():
#     for v in vs:
#         if u > v:
#             G.add_edge(u,v)
# nx.draw(G, with_labels = True)
# plt.show()

edges = [('bgl','vfx'), ('bqq','rxt'), ('btp','qxr')]
for u,v in edges:
    g[u].remove(v)
    g[v].remove(u)

S = set([min(g)])
frontier = set([min(g)])
while frontier:
    u = frontier.pop()
    S.add(u)
    for v in g[u]:
        if v in S: continue
        frontier.add(v)
print(len(S) * (len(g) - len(S)))