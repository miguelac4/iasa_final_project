from ecr.resposta import Resposta
from sae.agente.accao import Accao

"""
A resposta mover obriga a ter uma acção naquela certa direcção.
"""

class RespostaMover(Resposta):

    def __init__(self, direccao):
        super().__init__(Accao(direccao)) # É intanciada uma acção numa dada direcção