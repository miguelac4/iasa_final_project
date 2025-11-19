from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
A procura por custo uniforme escolhe sempre o nó com menor custo acumulado desde o estado inicial.
É útil quando queremos garantir que encontramos o caminho mais barato até ao objetivo.

Usa uma fila de prioridade onde os nós são organizados pelo custo. No código, usamos a FronteiraPrioridade com um AvaliadorCustoUnif 
que dá a prioridade igual ao custo do nó.

"""

# Procura de custo uniforme, usa o avaliador de custo
class ProcuraCustoUnif(ProcuraMelhorPrim):
    def __init__(self):
        # Inicia a procura com o avaliador de custo uniforme
        super().__init__(AvaliadorCustoUnif())
