# encoding:utf-8

'''
	Otimização por colônia de formigas aplicado ao problema do caixeiro viajante
	Ant Colony Optimization for Traveling Salesman Problem
'''

import random, math


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


# classe que representa um grafo (grafos completos)
class Grafo:

	def __init__(self, num_vertices):
		self.num_vertices = num_vertices # número de vértices do grafo
		self.arestas = {} # dicionário com as arestas
		self.vizinhos = {} # dicionário com todos os vizinhos de cada vértice


	def adicionarAresta(self, origem, destino, custo):
		aresta = Aresta(origem=origem, destino=destino, custo=custo)
		self.arestas[(origem, destino)] = aresta
		if origem not in self.vizinhos:
			self.vizinhos[origem] = [destino]
		else:
			self.vizinhos[origem].append(destino)

	def obterCustoAresta(self, origem, destino):
		return self.arestas[(origem, destino)].obterCusto()

	def obterFeromonioAresta(self, origem, destino):
		return self.arestas[(origem, destino)].obterFeronomio()

	def setFeromonioAresta(self, origem, destino, feromonio):
		self.arestas[(origem, destino)].setFeromonio(feromonio)


# classe que representa uma formiga
class Formiga:

	def __init__(self, cidade):
		self.cidade = cidade

	def obterCidade(self):
		return self.cidade


# classe do ACO
class ACO:

	def __init__(self, grafo, num_formigas, vertice_inicial=1, alfa=1, beta=5, 
						iteracoes=10, evaporacao=0.5):
		self.grafo = grafo
		self.vertice_inicial = vertice_inicial
		self.num_formigas = num_formigas
		self.alfa = alfa # importância do feromônio
		self.beta = beta # importância da informação heurística
		self.iteracoes = iteracoes # quantidade de iterações
		self.evaporacao = evaporacao # taxa de evaporação
		self.formigas = [] # lista de formigas

		# cria as formigas
		for i in range(self.num_formigas):
			# coloca cada formiga aleatoriamente em uma cidade
			self.formigas.append(Formiga(cidade=random.randint(1, self.grafo.num_vertices)))

		# calcula o custo guloso pra usar na inicialização do feromônio
		custo_guloso = 0
		vertice_corrente = self.vertice_inicial
		visitados = [vertice_corrente]
		while True:
			vizinhos = self.grafo.vizinhos[vertice_corrente][:]
			custos, escolhidos = [], {}
			for vizinho in vizinhos:
				if vizinho not in visitados:
					custo = self.grafo.obterCustoAresta(vertice_corrente, vizinho)
					escolhidos[custo] = vizinho
					custos.append(custo)
			if len(visitados) == self.grafo.num_vertices:
				break
			min_custo = min(custos) # pega o menor custo da lista
			custo_guloso += min_custo # adiciona o custo ao total
			vertice_corrente = escolhidos[min_custo] # atualiza o vértice corrente
			visitados.append(vertice_corrente) # marca o vértice corrente como visitado

		# adiciona o custo do último visitado ao custo_guloso
		custo_guloso += self.grafo.obterCustoAresta(visitados[-1], self.vertice_inicial)

		# inicializa o feromônio de todas as arestas
		for chave_aresta in self.grafo.arestas:
			feromonio = 1.0 / (self.grafo.num_vertices * custo_guloso)
			self.grafo.setFeromonioAresta(chave_aresta[0], chave_aresta[1], feromonio)


	def rodar(self):
		
		# lista de listas com as cidades visitadas por cada formiga
		cidades_visitadas = []
		for i in range(self.num_formigas):
			cidades = [self.formigas[i].obterCidade()]
			cidades_visitadas.append(cidades)

		#print(cidades_visitadas)

		for i in range(1, self.grafo.num_vertices):

			for k in range(self.num_formigas):
				# obtém todos os vizinhos que não foram visitados
				cidades_nao_visitadas = list(set(self.grafo.vizinhos[self.formigas[k].obterCidade()]) - set(cidades_visitadas[k]))
				
				# somatório do conjunto de cidades não visitadas pela formiga "k"
				# servirá para utilizar no cálculo da probabilidade
				somatorio = 0.0
				for cidade in cidades_nao_visitadas:
					# calcula o feromônio
					feromonio =  self.grafo.obterFeromonioAresta(self.formigas[k].obterCidade(), cidade)
					# obtém a distância
					distancia = self.grafo.obterCustoAresta(self.formigas[k].obterCidade(), cidade)
					# adiciona no somatório
					somatorio += (math.pow(feromonio, self.alfa) * math.pow(1.0 / distancia, self.beta))

				# probabilidades de escolher um caminho
				probabilidades = {}

				for cidade in cidades_nao_visitadas:
					# calcula o feromônio
					feromonio = self.grafo.obterFeromonioAresta(self.formigas[k].obterCidade(), cidade)
					# obtém a distância
					distancia = self.grafo.obterCustoAresta(self.formigas[k].obterCidade(), cidade)
					# obtém a probabilidade
					probabilidade = (math.pow(feromonio, self.alfa) * math.pow(1.0 / distancia, self.beta)) / somatorio
					# adiciona na lista de probabilidades
					probabilidades[cidade] = probabilidade

				# obtém a cidade escolhida
				cidade_escolhida = min(probabilidades, key=probabilidades.get)
				# adiciona a cidade escolhida a lista de cidades visitadas pela formiga "k"
				cidades_visitadas[k].append(cidade_escolhida)


		#for k in range(self.num_formigas):
		#	print('%d: %s' % (self.formigas[k].obterCidade(), str(cidades_visitadas[k])))


if __name__ == "__main__":

	# cria um grafo passando o número de vértices
	grafo = Grafo(num_vertices=4)

	# adiciona as arestas
	grafo.adicionarAresta(1, 2, 10)
	grafo.adicionarAresta(2, 1, 10)
	grafo.adicionarAresta(1, 3, 50)
	grafo.adicionarAresta(3, 1, 50)
	grafo.adicionarAresta(1, 4, 30)
	grafo.adicionarAresta(4, 1, 30)
	grafo.adicionarAresta(2, 3, 20)
	grafo.adicionarAresta(3, 2, 20)
	grafo.adicionarAresta(2, 4, 10)
	grafo.adicionarAresta(4, 2, 10)
	grafo.adicionarAresta(3, 4, 60)
	grafo.adicionarAresta(4, 3, 60)

	# cria uma instância de ACO
	aco = ACO(grafo=grafo, num_formigas=grafo.num_vertices, alfa=1, beta=5, 
				iteracoes=10, evaporacao=0.5)
	# roda o algoritmo
	aco.rodar()