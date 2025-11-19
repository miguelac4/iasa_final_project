from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

"""
Engenharia de Software:
    Programação por diferenças (Modelaridade):
	    Utilizámos programação por diferenças porque criámos um mecanismo de procura geral que trata toda a 
        lógica comum. A diferença no comportamento entre profundidade e largura é modularizada nas classes de 
        fronteira, mudando apenas a ordem de inserção dos nós.
	    Com apenas uma linha de codigo implementámos o comportamento do mecanismo de procura em profundidade e com 
        outra linha o comportamento do mecanismo em largura.

Procura em profundidade (Depth-First Search)
    O agente explora primeiro o caminho mais recente e, em seguida, expande todos os nós restantes desse caminho.
	Explora primeiro um caminho até ao fim antes de tentar outras opções.
	Explora primeiro os nós mais recentes.
	
	Fronteira de exploração:
		A fronteira de exploração são os nós de possivel exploração.
		Passos de procura:
			1) Remover primeiro nó da fronteira
			2) Aplico os operadores
			3) Gero todos os sucessores possiveis
			4) Coloco os sucessores gerados na fronteira
	Procura termina: a solução corresponde à sequência de nós (estados e operadores) no ramo da árvore de procura 
    que contém o nó correspondente ao estado objectivo.
"""

class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        super().__init__(FronteiraLIFO()) # Evocar construtor da superclasse passando a instancia LIFO


    # Vamos ignorar o método memorizar(self, no), por enquanto