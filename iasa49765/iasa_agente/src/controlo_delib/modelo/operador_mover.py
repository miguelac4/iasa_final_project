from math import cos, sin
import math

from controlo_delib.modelo.estado_agente import EstadoAgente
from sae.agente.accao import Accao
"""
A classe OperadorMover representa uma ação de movimento que o agente pode executar no mundo, numa determinada direção.

Este operador é utilizado no planeador para gerar os possíveis estados sucessores a partir de um estado atual, simulando 
o que aconteceria se o agente se movesse naquela direção.
"""

class OperadorMover:
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Accao(direccao)

    def aplicar(self, estado):
        nova_posicao = self.__translacao(estado.posicao, self.accao.passo, self.ang)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo: # Instrução "in" é suportada pelo método "__contains__" do modelo_mundo
            return novo_estado

    # Custo significa quanto custa ao operador para produzir o estado sucessor
    def custo(self, estado, estado_suc):
        return max(1, math.dist(estado.posicao, estado_suc.posicao)) # Calcula a distância entre os estados, mas garante que o custo mínimo é 1

    def __translacao(self, posicao, distancia, angulo):
        x, y = posicao # Posição é um tuplo mas o Python faz a separação automatica
        dx = dx = round(distancia * cos(angulo)) # Arredondamento da distancia * cosseno do angulo
        dy = round(-distancia * sin(angulo)) # Arredondamento da distancia * seno do angulo
        nova_posicao = (x + dx, y + dy)
        return nova_posicao

    @property
    def ang(self):
        return self.__ang

    @property
    def accao(self):
        return self.__accao
