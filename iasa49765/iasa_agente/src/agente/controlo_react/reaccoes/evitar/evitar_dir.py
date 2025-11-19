from agente.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst
from agente.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from ecr.reaccao import Reaccao

"""
Evitar Direcção especializa Reacção.
No construtor da classe EvitarDir estamos a associar uma instância de EstimuloObst, que serve para detetar
obstáculos numa dada direcção, com uma instância do RespostaEvitar
Esta associação permite ao agente reagir automaticamente quando deteta um obstáculo nessa direcção
"""


class EvitarDir(Reaccao):
        # Associar uma instancia de estimulo obstaculo na direcção que é indicada a uma intancia de resposta evitar
        def __init__(self, direccao):
                estimulo = EstimuloObst(direccao)
                resposta = RespostaEvitar()
                super().__init__(estimulo, resposta)