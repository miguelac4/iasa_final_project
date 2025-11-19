from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from pee.melhor_prim.procura_informada import ProcuraInformada

"""
Expandir o nó que aparenta estar mais próximo do objetivo.

Vantagens: é rápido quando a heurística é boa.
Desvantagens: pode ser incompleto e não encontrar a solução ótima, pois não tem em conta o custo desde o nó inicial.
"""

class ProcuraSofrega(ProcuraInformada):
    
    # Chama o construtor da superclasse com o correto avaliador
    def __init__(self):
        super().__init__(AvaliadorSof())
        