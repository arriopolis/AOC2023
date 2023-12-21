import sys
import networkx as nx
import matplotlib.pyplot as plt

mods = {}
for line in sys.stdin:
    src,dests = line.strip().split(' -> ')
    if src[0] in '&%':
        mode = src[0]
        src = src[1:]
    else: mode = ''
    mods[src] = (mode, dests.split(', '))

G = nx.DiGraph()
for src, (mode, dests) in mods.items():
    for dest in dests:
        G.add_edge(src, dest)
node_colors = [
    'g' if mod == 'broadcaster' else
    'k' if mod not in mods else
    'b' if mods[mod][0] == '&' else 'r'
    for mod in G.nodes()
]
nx.draw(G, with_labels = True, node_color = node_colors)
plt.show()