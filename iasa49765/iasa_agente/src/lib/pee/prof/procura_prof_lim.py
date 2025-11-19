from pee.prof.procura_profundidade import ProcuraProfundidade
"""
Procura em Profundidade Limitada
	Procura em profundidade mas com limite, obriga a procura a ser exaustiva dentro do limite de profundidade.
	Esta se não poder passer uma certa profundidade irá para outro ramo.

	Implementação: antes de expandirmos iremos verificar se a profundidade do nó é menor que a profundidade 
    maxima, caso se verifique, iremos expandir.
"""

class ProcuraProfLim(ProcuraProfundidade):
    def __init__(self, prof_max):
        super().__init__() # Chama o construtor da superclasse procura em profundidade
        self._prof_max = prof_max # Guarda a profundidade máxima
    
    #def procurar(self, problema, prof_max):

    def _expandir(self, problema, no):
        sem_sucessores = []
        # Só iremos expandir se a profundidade do nó for menor que a profundidade maxima
        if no.profundidade < self._prof_max: 
            return super()._expandir(problema, no) # Retorna uma lista de nós
        else:
            # Para não cometer erros temos de retornar uma lista vazia, caso nao seja menor não retorna 
            # mais sucessores
            return sem_sucessores