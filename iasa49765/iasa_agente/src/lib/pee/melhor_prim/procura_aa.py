from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada

"""
É uma combinação entre a Procura de Custo Uniforme e a Procura Sofrega.
Combina o custo acumulado até ao nó, g(n), com a heurística, h(n), formando a função f(n) = g(n) + h(n).

Vantagens: encontra a solução ótima se a heurística for admissível (não sobrestima o custo).
Desvantagens: pode ser lenta ou usar muita memória se o espaço de procura for grande.

"""

class ProcuraAA(ProcuraInformada):

    # Chama o construtor da superclasse com o correto avaliador
    def __init__(self):
        super().__init__(AvaliadorAA())