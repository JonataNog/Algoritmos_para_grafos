import grafo
import time

arquivo = input("Informe o arquivo: ")
g = grafo.Grafo()
flag = g.ler_arquivo(arquivo)

origem = input("Digite o vertice de origem: ")
origem = int(origem)
destino = input("Digite o vertice de destino: ")
destino = int(destino)

inicio = time.process_time()
if flag == 0:
    print("\n---Busca em largura para caminho minimo---")
    pred, dist, fim = g.busca_largura_caminhos(origem)
elif flag == 1:
    print("\n---Algoritmo de Dijkstra---")
    pred, dist, fim = g.dijkstra(origem)
else:
    print("\n---Algoritmo de Bellman Ford---")
    pred, dist, fim = g.bellman_ford(origem)
custo = dist[destino]
tempo = fim - inicio
caminho = g.rec_caminho(origem, destino, pred)
print("Caminho: ", caminho)
print("Custo: ", custo)
print("Tempo: ", tempo)





