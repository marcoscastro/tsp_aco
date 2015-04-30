# Otimização por Colônia de Formigas - Problema do Caixeiro Viajante
Otimização por Colônia de Formigas (Ant Colony Optimization - ACO) aplicado ao problema do caixeiro viajante (Traveling Salesman Problem - TSP).

O projeto contém apenas um arquivo de código chamado "tsp_aco.py". Foi implementado em Python, funciona nas versões do Python 2.x e 3.x.

Esse código utiliza a heurística Colônia de Formigas para resolver o problema do Caixeiro Viajante que é um problema onde não se conhece um algoritmo polinomial que obtenha a solução ótima.

O uso de heurísticas é de suma importância para atacar esses problemas. A heurística não garante uma solução ótima, mas, se tiver bem implementada e com parâmetros bem ajustados, garante uma boa solução.

A pasta "referências" contém as referências que foram utilizadas como base para a implementação.

O arquivo "grafo.png" é a matriz de distâncias que foi utilizada para testar a implementação.

![alt tag](https://github.com/marcoscastro/tsp_aco/blob/master/grafo.png)

Um dos menores caminhos para esse grafo é:

7 -> 3 -> 2 -> 5 -> 1 -> 8 -> 4 -> 6 | custo: 140

Alguns parâmetros podem ser ajustados tais como o "alfa" que é a importância do feromônio, "beta" que é a importância heurística, quantidade de iterações e a taxa de evaporação do feromônio. É aconselhável consultar as referências para um melhor entendimento da heurística.

Inicialmente, a quantidade de feromônio depositada nas arestas leva em conta o custo de uma construção gulosa. O artigo descreve bem isso.

Quaisquer dúvidas, entre em contato :)
