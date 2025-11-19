from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento
"""
Estimulo alvo tem associado uma direcção.
Realiza a interface estimulo, ou seja obriga o contrato detectar.
"""

class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama = 0.9):
        self.__direccao = direccao
        self.__gama = gama
        
    # A percepcao pode ser indexada numa direcção, a percepcao trás as 4 direcções
    def detectar(self, percepcao):
        # interessa-nos o elemento e distancia a partir da estrutura de dados percepcao
        elemento, distancia, _ = percepcao[self.__direccao] # "_" siginifica que não vamos usar essa parte do tuplo
        # á medida que a distancia aumenta a intensidade diminui exponecialmente, se existir alvo 
        # (gama pertence  a [0, 1[)
        intensidade = self.__gama ** distancia if elemento == Elemento.ALVO else 0
        return intensidade