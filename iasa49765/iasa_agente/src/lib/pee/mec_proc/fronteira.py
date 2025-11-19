from abc import ABC, abstractmethod

# A fronteira é uma lista onde guardamos os nós que estão abertos para expansão
class Fronteira(ABC):
    def __init__(self):
        self.iniciar()


    def iniciar(self):
        self._nos = []
    
    @abstractmethod
    def inserir(self, no):
        """"""

    def remover(self):
        # Eliminar o primeiro elemento da lista
        return self._nos.pop(0)

    @property
    def vazia(self):
        # Retorna um booleano que afirma se a lista está vazia ou não
        return len(self._nos) == 0