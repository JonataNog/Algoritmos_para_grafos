class HeapMax:

    def __init__(self):
        '''Inicia a estrutura heap máxima'''
        self.nos = 0
        self.heap = []

    def adiciona_nos(self, u):
        '''Adiciona um nó na árvore heap máxima'''
        self.heap.append(u)
        self.nos += 1
        filho = self.nos
        while True:
            if filho == 1:
                break
            pai = filho // 2
            if self.heap[pai-1] >= self.heap[filho-1]:
                break
            else:
                self.heap[pai-1], self.heap[filho-1] = self.heap[filho-1], self.heap[pai-1]
                filho = pai

    def remove_no(self):
        '''Remove o nó raiz da árvore heap'''
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        pai = 1
        while True:
            filho = 2 * pai
            if filho > self.nos:
                break
            if filho + 1 <= self.nos:
                if self.heap[filho] > self.heap[filho-1]:
                    filho += 1
            if self.heap[pai-1] >= self.heap[filho-1]:
                break
            else:
                self.heap[filho-1], self.heap[pai-1] = self.heap[pai-1], self.heap[filho-1]
                pai = filho
        return x

    def tamanho(self):
        '''Retorna o tamanho da árvore heap'''
        return self.nos

    def maior_elemento(self):
        '''Retorna o maior elemento da árvore caso não seja uma estrutura vazia'''
        if self.nos != 0:
            return self.heap[0]
        return None

    def filho_esquerda(self, i):
        '''Retorna o filho a esquerda de um elemento caso ele exista'''
        if self.nos >= 2*i:
            return self.heap[2*i - 1]
        return None

    def filho_direita(self, i):
        '''Retorna o filho a direita de um elemento caso ele exista'''
        if self.nos >= 2*i + 1:
            return self.heap[2*i]
        return None

    def pai(self, i):
        '''Retorna o pai de um elemento'''
        return self.heap[i // 2-1]

    def mostra_heap(self):
        '''Imprime a árvore heap em formato de lista'''
        print(self.heap)