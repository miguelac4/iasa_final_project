from abc import ABC, abstractmethod


# Tem um contrato que obriga a existir o metodo planear que recebe o metodo planeamento e uma lista de objetivos.

class Planeador(ABC):

    # Planea para o primeiro objetivo da lista de objetivos
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """"""
