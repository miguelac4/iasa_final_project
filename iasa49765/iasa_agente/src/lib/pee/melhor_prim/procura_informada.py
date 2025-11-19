from abc import ABC
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
"""
Também conhecidos como algoritmos de procura heurística, utilizam informação adicional (heurísticas) para encontrar 
soluções de forma mais eficiente.
"""
# Classe base para procuras informadas
class ProcuraInformada(ProcuraMelhorPrim, ABC):

    # Define a heurística no avaliador e prossegue com a procura
    def procurar(self, problema, heuristica): 
        # Alterar heuristica do avaliador
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)
