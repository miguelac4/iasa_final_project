from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
# Avaliador da procura A* (A Star Search).
# Nesta procura já existe dependencia do custo, a prioridade do nó é calculada com base no custo acumulado + heurística, 
# este algoritmo é mais equilibrado porque tenta encontrar caminhos bons e curtos.
"""

class AvaliadorAA(AvaliadorHeur):
    def prioridade(self, no):
        return no.custo + self.heuristica.h(no.estado)
