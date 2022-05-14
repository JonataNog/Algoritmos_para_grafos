import grafo

g1 = grafo.Grafo()
g1.ler_arquivo("toy.txt")

predD_g1 = g1.dijkstra(0)
