# Um comportamento composto corresponde à combinação de múltiplas reações interligadas. São comportamentos 
# complexos que quando um agente precisa de equilibrar diferentes objetivos, como evitar obstáculos enquanto 
# mantém a trajetória em direção a um destino desejado.

# O que vai estar dentro do comportamento composto irá ser um comportamento composto ou uma reacção simples. 
# (grande versatilidade)

# Comportamentos compostos agregam vários comportamentos.

from .comportamento import Comportamento
from abc import ABC, abstractmethod


class ComportComp(Comportamento, ABC):
    
    # No contrutor é necessario guardar o parametro comportamentos (para saber quais são os comportamentos internos)
    def __init__(self, comportamentos):
        #Lista que pode conter reações simples ou outros comportamentos compostos, permitindo hierarquias 
        #complexas.
        self.__comportamentos = comportamentos

    # Quando o comportamento composto é ativado vão ser ativado todos os comportamentos internos (um de cada vez) e 
    # vão ser guardados todas as acções que cada comportamento irá gerar.
    def activar(self, percepcao):
        # Iniciar uma lista vazia de accoes
        accoes = []
        # Varreamento de todos os comportamentos, ativando-os
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            # O que faz um comportamento não gerar uma accão é o valor de intensidade do estimulo ser 0
            if(accao is not None): 
                accoes.append(accao) # Guardar accoes

            if accoes:

                return self.seleccionar_accao(accoes)
    
    #Irá receber a lista gerada pelo activar() e retornar uma accao selecionada
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """"""