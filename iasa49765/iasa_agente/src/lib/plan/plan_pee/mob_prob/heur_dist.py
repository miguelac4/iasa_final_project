import math


class HeurDist():

    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        # Retorna a distancia entre a posicção do estado e a posição do estado final
        return math.dist(self.__estado_final.posicao, estado.posicao)