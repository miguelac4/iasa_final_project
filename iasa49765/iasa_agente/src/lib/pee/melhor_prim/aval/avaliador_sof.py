from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
Avaliador da Procura Sofrega (Greedy Search).
# Nesta procura a prioridade do nó é dada apenas pela heurística, ou seja, quanto mais perto do objetivo melhor, mão tendo em 
# conta o custo já percorrido.
"""

class AvaliadorSof(AvaliadorHeur):
    def prioridade(self, no):
        return self.heuristica.h(no.estado)
