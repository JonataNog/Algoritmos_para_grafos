import grafo

g1 = grafo.Grafo()
g1.ler_arquivo("toy.txt")

print(g1.dijkstra(0))
print(g1.bellman_ford(0))
