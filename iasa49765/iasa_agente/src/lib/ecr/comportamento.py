# Um comportamento pode ser entendido como um conjunto de reações organizadas segundo um critério comum.
from abc import ABC, abstractmethod #Abstract Base Class

class Comportamento(ABC):
    @abstractmethod
    def activar(self, percepcao):
        """"Retorna uma acção"""