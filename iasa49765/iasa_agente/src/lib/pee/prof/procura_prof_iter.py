from pee.prof.procura_prof_lim import ProcuraProfLim

"""
Procura em Profundidade Iterativa
    Realiza várias procuras em profundidade limitada, aumentando o limite de profundidade progressivamente.
    Ira alargando a profundidade até encontrar a solução.
"""

class ProcuraProfIter(ProcuraProfLim):

    def __init__(self, prof_max_inicial = 10):
        super().__init__(prof_max_inicial)

    def procurar(self, problema, inc_prof, limite_prof):
        # Os ranges em python são exclusivos, daí o uso do +1
        for profundidade in range(0, limite_prof + 1, inc_prof):
            self._prof_max = profundidade # Alterar profundidade maxima para profundidade
            solucao = super().procurar(problema) # Procurar solução com esta profundidade máxima
            if solucao:
                return solucao # Se encontrar solução, devolve
            