from abc import ABC
from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade

"""
Procura Melhor-Primeiro (Best-First Search)
		
        Usa uma função de avaliação f(n) para decidir a ordem de exploração dos nós.
		f(n) ≥ 0: quanto menor for f(n), mais promissor é o nó.
		A fronteira de exploração está ordenada por f(n) (por ordem crescente).
		Todas usam uma fila de prioridade (a fronteira) ordenada por f(n), mas cada uma tem um comportamento diferente consoante a função que se escolhe.
		
        f(n) pode ser:
			g(n): custo acumulado (Procura de Custo Uniforme).
			h(n): estimativa até ao objetivo (Procura Sôfrega).
			g(n) + h(n): custo acumulado + estimativa (Procura A*).

"""


class ProcuraMelhorPrim(ProcuraGrafo, ABC):

    def __init__(self, avaliador):
        self._avaliador = avaliador
        super().__init__(FronteiraPrioridade(avaliador)) # Inicia a fronteira prioridade com o avaliador

    def _manter(self, no):
        estado = no.estado

        # Manter se não houver ainda esse estado explorado
        if estado not in self._explorados:
            return True

        # Se já existe, verifica se o novo nó tem menor custo (melhor caminho)
        return no.custo < self._explorados[estado].custo