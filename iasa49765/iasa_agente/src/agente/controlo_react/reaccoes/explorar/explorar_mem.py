from ecr.resposta import Resposta
from sae.agente import percepcao
from sae.agente.avancar import Avancar


"""
A classe ExplorarMem representa um comportamento de exploração com memória.
"""

class ExplorarMem():
    # No construtor, criamos uma memória (lista) onde vamos guardar as perceções até a um certo limite 
    # (dim_max_mem). Se passar esse limite, apaga-se a mais antiga.
    def __init__(self, dim_max_mem = 100):
        self.__dim_max_mem = dim_max_mem
        self.__memoria = []

        self.__resposta = Resposta(Avancar())

    # verificamos se a perceção atual já está na memória. 
    def activar(self, percepcao):
        situacao = percepcao

        # Se a percepção não estiver na memoria adiciona-a
        if situacao not in self.__memoria:
            self.__memoria.append(situacao)

            # condição de eliminar memoria mais antiga caso fique cheia
            if len(self.__memoria) > self.__dim_max_mem:
                self.__memoria.pop(0)

            return self.__resposta.activar(percepcao)
        