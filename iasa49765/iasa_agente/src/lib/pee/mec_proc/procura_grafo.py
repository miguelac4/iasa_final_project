from abc import ABC, abstractmethod
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Diferente da procura em arvore a procura em grafo não pode acontecer ciclos, utilizando a fronteira de explorados evitamos esses ciclos.

A ideia principal é manter um dicionário "self._explorados" onde ficam registados os estados já visitados, associados 
ao nó correspondente.

"""


class ProcuraGrafo(MecanismoProcura, ABC):

    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {} # Iremos ter um dicionário de nós explorados (sempre que é memorizado um nó é colocado no dicionário)

    def _memorizar(self, no): # Define se um nó é para manter ou não
        if self._manter(no):
            super()._memorizar(no)
            self._explorados[no.estado] = no
            
    @abstractmethod
    def _manter(self, no):
        pass