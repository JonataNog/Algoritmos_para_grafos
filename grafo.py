class Grafo:

    def __init__(self, num_vert=0, num_arestas=0, lista_adj=None, mat_adj=None):
        self.num_vert = num_vert
        self.num_arestas = num_arestas
        if lista_adj is None:
            self.lista_adj = [[] for i in range(num_vert)]
        else:
            self.lista_adj = lista_adj
        if mat_adj is None:
            self.mat_adj = [[0 for j in range(num_vert)] for i in range(num_vert)]
        else:
            self.mat_adj = mat_adj

    def add_aresta(self, u, v, w=1):
        '''Adiciona aresta de u a v com peso w'''
        self.num_arestas += 1
        if u < self.num_vert and v < self.num_vert:
            self.lista_adj[u].append((v, w))
            self.mat_adj[u][v] = w
        else:
            print("Aresta invalida!")

    def remove_aresta(self, u, v):
        '''Remove aresta de u a v, se houver'''
        if u < self.num_vert and v < self.num_vert:
            if self.mat_adj[u][v] != 0:
                self.num_arestas -= 1
                self.mat_adj[u][v] = 0
                for (v2, w2) in self.lista_adj[u]:
                    if v2 == v:
                        self.lista_adj[u].remove((v2, w2))
                        break
            else:
                print("Aresta inexistente!")
        else:
            print("Aresta invalida!")

    def grau(self, u):
        '''Retorna o grau do vertice u'''
        return len(self.lista_adj[u])

    def adjacente(self, u, v):
        '''Determina se v é adjacente a u'''
        if self.mat_adj[u][v] != 0:
            return True
        else:
            return False

    def adjacentes_peso(self, u):
        '''Retorna a lista dos vertices adjacentes a u no formato (v, w)'''
        return self.lista_adj[u]

    def adjacentes(self, u):
        """Retorna a lista dos vertices adjacentes a u"""
        adj = []
        for i in range(len(self.lista_adj[u])):
            (v, w) = self.lista_adj[u][i]
            adj.append(v)
        return adj

    def densidade(self):
        '''Retorna a densidade do grafo'''
        return self.num_arestas / (self.num_vert * (self.num_vert - 1))

    def subgrafo(self, g2):
        '''Determina se g2 e subgrafo de self'''
        if g2.num_vert > self.num_vert:
            return False
        for i in range(len(g2.mat_adj)):
            for j in range(len(g2.mat_adj[i])):
                if g2.mat_adj[i][j] != 0 and self.mat_adj[i][j] == 0:
                    return False
        return True

    def ler_arquivo(self, nome_arq):
        '''Le arquivo de grafo no formato dimacs
            Flag recebe valor 0 para um grafo não ponderado, flag recebe 1 para grafo com pesos positivos
            e flag recebe 2 para grafos com pesos negativos'''
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            str = arq.readline()
            str = str.split(" ")
            self.num_vert = int(str[0])
            cont_arestas = int(str[1])
            # Inicializacao das estruturas de dados
            self.lista_adj = [[] for i in range(self.num_vert)]
            self.mat_adj = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)]
            flag = 1
            # Le cada aresta do arquivo
            for i in range(0, cont_arestas):
                str = arq.readline()
                str = str.split(" ")
                u = int(str[0])  # Vertice origem
                v = int(str[1])  # Vertice destino
                w = int(str[2])  # Peso da aresta
                if w < 0:
                    flag = 2
                self.add_aresta(u, v, w)
            return flag
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")

    def busca_largura(self, s):
        '''Retorna a ordem de descoberta dos vertices pela busca em largura a partir de s'''
        desc = [0 for v in range(self.num_vert)]
        Q = [s]
        R = [s]
        desc[s] = 1
        while Q:
            u = Q.pop(0)
            for (v, w) in self.lista_adj[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
        return R

    def busca_profundidade(self, s):
        '''Retorna a ordem de descoberta dos vertices pela busca em profundidade a partir de s'''
        desc = [0 for v in range(self.num_vert)]
        S = [s]
        R = [s]
        desc[s] = 1
        while S:
            u = S[-1]
            desempilhar = True
            for (v, w) in self.lista_adj[u]:
                if desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    break
            if desempilhar:
                S.pop(-1)
        return R

    def conexo(self, s):
        '''Retorna Ture se o grafo e conexo e False caso contrario baseado na busca em largura'''
        desc = [0 for v in range(self.num_vert)]
        Q = [s]
        R = [s]
        desc[s] = 1
        while Q:
            u = Q.pop(0)
            for (v, w) in self.lista_adj[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
        for i in range(len(desc)):
            if desc[i] == 0:
                return False
        return True

    def ciclo(self, s):
        '''Retorna Ture se o grafo tem ciclo e False caso contrario baseado na busca em largura'''
        desc = [0 for v in range(self.num_vert)]
        for s in range(self.num_vert):
            if desc[s] == 0:
                Q = [s]
                R = [s]
                desc[s] = 1
                while Q:
                    u = Q.pop(0)
                    for (v, w) in self.lista_adj[u]:
                        if desc[v] == 0:
                            Q.append(v)
                            R.append(v)
                            desc[v] = 1
                        else:
                            return True
        return False

    def dijkstra(self, s):
        dist = [float("inf") for v in range(self.num_vert)]
        pred = [None for v in range(self.num_vert)]
        dist[s] = 0
        Q = []
        for i in range(self.num_vert):
            Q.append(i)

        while Q:
            u = menor_dist(dist, Q)
            Q.remove(u)
            for (v, w) in self.lista_adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
        return pred

    def bellman_ford(self, s):
        dist = [float("inf") for v in range(self.num_vert)]
        pred = [None for v in range(self.num_vert)]
        dist[s] = 0
        for i in range(self.num_vert-1):
            trocou = False
            for (u, w) in self.lista_adj[i]:
                if dist[u] > dist[i] + w:
                    dist[u] = dist[i] + w
                    pred[u] = i
                    trocou = True
            if trocou == False:
                break
        return pred

    def rec_caminho(s, t, pred):
        C = [t]
        aux = t
        while aux != s:
            aux = pred[aux]
            C.insert(0,aux)
        return C

def menor_dist(dist, Q):
    menorD = float("inf")
    menorV = None
    for i in range(len(Q)):
        aux = Q[i]
        if dist[aux] < menorD:
            menorD = dist[aux]
            menorV = aux
    return menorV

