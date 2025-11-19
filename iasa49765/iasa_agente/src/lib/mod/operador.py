from abc import ABC, abstractmethod

"""
Aplicar um operador a um estado e simular a esse estado os efeitos da ação ao operador gerando um novo estado.
"""

class Operador(ABC):
    @abstractmethod
    def aplicar(self, estado):
        """"""

    @abstractmethod
    def custo(self, estado, estado_suc):
        pass