# encoding:utf-8

'''
	Otimização por colônia de formigas aplicado ao problema do caixeiro viajante
	Ant Colony Optimization for Traveling Salesman Problem
'''


# classe que representa uma aresta
class Aresta:

	def __init__(self, origem, destino, custo):
		self.origem = origem
		self.destino = destino
		self.custo = custo
		self.feromonio = None

	def obterOrigem(self):
		return self.origem

	def obterDestino(self):
		return self.destino

	def obterCusto(self):
		return self.custo

	def obterFeronomio(self):
		return self.feromonio

	def setFeromonio(self, feromonio):
		self.feromonio = feromonio


# classe que representa um grafo
class Grafo:

	def __init__(self, num_vertices):
		self.num_vertices = num_vertices
		self.arestas = {}
		self.ligacoes = {}

	def adicionarAresta(self, origem, destino, custo):
		aresta = Aresta(origem=origem, destino=destino, custo=custo)
		self.arestas[(origem, destino)] = aresta
		self.ligacoes[origem].append(destino)

	def obterCustoAresta(self, origem, destino):
		return self.arestas[(origem, destino)].obterCusto()

	def obterFeromonioAresta(self, origem, destino):
		return self.arestas[(origem, destino)].obterFeronomio()

	def setFeromonioAresta(self, origem, destino, feromonio):
		self.arestas[(origem, destino)].setFeromonio(feromonio)


# classe do ACO
class ACO:

	def __init__(self, grafo):
		self.grafo = grafo

		custo_guloso = 1
		# inicializa o feromônio de todas as arestas
		for aresta in self.grafo.arestas:
			feromonio = 1.0 / (self.grafo.num_vertices * custo_guloso) 


if __name__ == "__main__":

	# cria um grafo passando o número de vértices
	grafo = Grafo(num_vertices=5)

	# adiciona as arestas
	grafo.adicionarAresta(1, 2, 10)
	grafo.adicionarAresta(2, 1, 10)
	grafo.adicionarAresta(1, 3, 20)
	grafo.adicionarAresta(3, 1, 20)
	grafo.adicionarAresta(2, 3, 30)
	grafo.adicionarAresta(3, 2, 30)

	# cria uma instância de ACO
	aco = ACO(grafo=grafo)