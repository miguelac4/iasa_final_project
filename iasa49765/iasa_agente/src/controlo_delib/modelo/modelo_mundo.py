from math import dist
from controlo_delib.modelo.estado_agente import EstadoAgente
from controlo_delib.modelo.operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento

"""
A classe ModeloMundo representa o conhecimento interno que o agente tem sobre o ambiente. É através desta estrutura que o agente 
vai manter um modelo atualizado do que já observou no mundo.

Guarda os seguintes elementos principais:
    - Estado atual do agente "estado"
    - Lista de estados conhecidos "estados"
    - Mapa de elementos percebidos "elementos", onde cada posição está associada a um tipo
    - Lista de operadores de movimento para cada direção possível "operadores"
"""

class ModeloMundo(ModeloPlan): # Modelo do mundo tem de realizar a interface ModeloPlan

    def __init__(self):
         
        self.__alterado = False
        self.__estado = None # Estado atual do agente começa a None
        self.__estados = [] # Lista de estados conhecidos do mundo (inicialmente vazia)
        self.__elementos = {} # Dicionario de elementos

        # Lista de operadores com todas as direções possíveis em OperadorMover
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]

    # Devolve o estado atual do agente
    def obter_estado(self):
        return self.__estado

    # Devolve a lista de estados conhecidos no mundo
    def obter_estados(self):
        return self.__estados

    # Devolve a lista de operadores possíveis (um por direção)
    def obter_operadores(self):
        return self.__operadores

    # Retorna um elemento se ele existir, caso não, retorna None
    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao) # Vai buscar ao dicionário o elemento que está na posição do estado

    def distancia(self, estado):
        # Calcular e devolver um valor float (distancia entre o estado passado e a distancia do estado modelo)
        # A função "dist" calcula a distância num espaço cartesiano, esta aceita tuplos
        return dist(self.__estado.posicao, estado.posicao)
    
    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__alterado = self.__elementos != percepcao.elementos

        if self.__alterado:
            self.__elementos = percepcao.elementos # Atualizar elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes] # Atualizar os estados

    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items(): # items() converte um dicionario numa lista de tuplos
                # Se o elemento for um dos indicados na lista irá mostrar o elemento
                if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                    vista.mostrar_elemento(posicao, elemento)
        # Marcar a posição atual do agente
        vista.marcar_posicao(self.__estado.posicao)

    def __contains__(self, estado):
        return estado in self.__estados

    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    

