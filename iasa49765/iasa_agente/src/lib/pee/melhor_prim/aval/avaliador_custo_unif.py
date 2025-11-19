# Avaliador para a procura de custo uniforme
from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):
    def prioridade(self, no):
        # A prioridade será o custo acumulado do nó
        return no.custo
