from mod.estado import Estado
"""

A classe EstadoAgente representa o estado interno do agente no mundo.
Herda da classe abstrata Estado, e serve para identificar a posição atual do agente no ambiente.

"""

class EstadoAgente(Estado):
    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(self.__posicao) # Iniciar atributo privado com a identificação unica (hash) do estado

    # retorna um identificador unico para cada estado
    def id_valor(self):
        return self.__id_valor
    
    @property
    def posicao(self):
        return self.__posicao