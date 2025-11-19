from abc import ABC, abstractmethod

"""
Define o comportamento esperado para qualquer modelo de decisão de Markov (PDM)
"""
class ModeloPDM(ABC):
    
    @abstractmethod
    def S(self):
        """
        Devolve a lista de todos os estados possíveis no mundo.
        """

    @abstractmethod
    def A(self, s):
        """
        Dado um estado s, devolve a lista de operadores (ações) possíveis nesse estado.
        """

    # Função de transição:
    @abstractmethod
    def T(self, s, a, sn):
        """
        Devolve a probabilidade de passar do estado s para o estado sn, ao aplicar a ação a.
        """

    # Função de recompensa:
    @abstractmethod
    def R(self, s, a, sn):
        """
        Devolve a recompensa esperada ao passar de s para sn, usando a ação a.

        """

    @abstractmethod
    def suc(self, s, a):
        """
        Dado um estado s e uma ação a, devolve os estados sucessores possíveis.
        """