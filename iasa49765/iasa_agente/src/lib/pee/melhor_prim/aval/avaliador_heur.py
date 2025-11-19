from pee.melhor_prim.aval.avaliador import Avaliador
"""

Avaliador que usa heurística para calcular a prioridade de um nó.
Serve de base para os avaliadores sofregos e A*.

"""

class AvaliadorHeur(Avaliador):
    def __init__(self):
        self.__heuristica = None

    # A heurística pode ser atribuída depois via property.
    @property 
    def heuristica(self):
        return self.__heuristica

    @heuristica.setter
    def heuristica(self, value):
        self.__heuristica = value