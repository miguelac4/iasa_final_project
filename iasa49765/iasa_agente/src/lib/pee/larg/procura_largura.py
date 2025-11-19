from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Engenharia de Software:
    Programação por diferenças (Modelaridade):
	    Utilizámos programação por diferenças porque criámos um mecanismo de procura geral que trata toda a 
        lógica comum. A diferença no comportamento entre profundidade e largura é modularizada nas classes de 
        fronteira, mudando apenas a ordem de inserção dos nós.
	    Com apenas uma linha de codigo implementámos o comportamento do mecanismo de procura em profundidade e com 
        outra linha o comportamento do mecanismo em largura.

Procura em largura (Breadth-First Search)
	Explora os nós por camadas, nível a nível.
    Só depois do agente explorar todos os nós da camada atual é que passa para a exploração da proxima camada.
	Explorar primeiro os nós mais antigos.

	Fronteira de exploração:
		Passos de procura:
			Iguais ao da procura em profundidade embora nesta os sucessores são colocados no fim.
"""

class ProcuraLargura(MecanismoProcura):
    def __init__(self):
        super().__init__(FronteiraFIFO()) # Evocar construtor da superclasse passando a instancia FIFO

    # Por enquanto vamos ignorar o ProcuraGrafo e herdar diretamente de MecanismoProcura