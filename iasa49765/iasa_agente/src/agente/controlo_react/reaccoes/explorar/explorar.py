from sae import Direccao, Avancar, Rodar
import random

# Import absoluto por estarmos a usar uma biblioteca (um package completo)
from ecr.comportamento import Comportamento

"""
O explorar não necessita de estimulo.
O explorer move se com movimentos aleatorios, existem dois tipos de movimentos (avançar e recuar).
"""

class Explorar(Comportamento):
    def __init__(self, prob_rotacao):
        # removeu-se o "super().__init__()" porque como é uma interface não fará sentido ativar 
        # o contrutor da superclasse
        self.__prob_rotacao = prob_rotacao # Probabilidade responsavel para selecionar accao do agente

    # Neste método iremos atribuir que accao realizar dependendo do valor da prob_rotacao do contrutor, as
    # probabilidades são 60% para rodar e 40% para avançar, assim realizamos um explorar com movimentos aleatorios.
    def activar(self, percepcao):
        """ #REALIZADO DE OUTRA FORMA NA AULA 
        #(acredito que o código que realizei diferente do realizado pelo professor seja mais simplificado)
        #sem "else:" a entropia aumenta (unica diferença que acho pretinente no meu codigo)
        randomValue = random.uniform(0, 1) # usei random.uniform para definir o intervalo random
        if randomValue < self.__prob_rotacao:
            # Criar uma lista com o enumerado de Direcções e com o random escolhe de forma random uma 
            # direcção dessa lista
            return Rodar(random.choice(list(Direccao))) # Retorna a acção "Rodar" com uma direcção random
        return Avancar() # Retorna a acção "Avançar"
        """
        # Toda a documentação deste código foi realizada no codigo acima 
        valor_aleatorio = random.random()
        accao = None
        if valor_aleatorio < self.__prob_rotacao:
            direccoes = list(Direccao)
            direccao_aleat = random.choice(direccoes)
            accao = Rodar(direccao_aleat)
        else:
            accao = Avancar()
        return accao
        