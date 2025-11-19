from agente.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao

"""	
Aproximar Direcção especializa Reacção.
O aproximar direcional é uma reaccção que associa o estimulo alvo a uma resposta mover, depende de uma direção.
"""
class AproximarDir(Reaccao):
    # No constructor usamos a superclasse Reaccao para evocarmos um EstimuloAlvo com uma certa direcção 
    # e uma RespostaMover com essa mesma direcção.
    def __init__(self, direccao):
        super().__init__(
            EstimuloAlvo(direccao),
            RespostaMover(direccao)
        )