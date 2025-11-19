from abc import ABC, abstractmethod

"""
Estado: Um estado é um paço para a resolução de um problema.

Espaço de estados: Conjunto de todos os tipos de estados e transições para a resolução de um problema 
(tipicamente nunca se representa em memória por poder ser infinito).

Dentro de estado temos estados sucessores usamos estes ate atingir um objetivo.

"""

class Estado(ABC):
    @abstractmethod
    def id_valor(self):
       """"""

    def __hash__(self):
        return self.id_valor()

    def __eq__(self, other):
        # Só vamos considerar 2 objetos iguais com o mesmo hash se o outro objeto tambem for um estado
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()
        # O else por omissão será None que neste caso  (boleano) irá dar False