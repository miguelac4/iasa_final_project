from sae.ambiente.elemento import Elemento

"""
A classe MecDelib representa o mecanismo deliberativo do agente. É responsável por analisar o estado atual do mundo 
(guardado no ModeloMundo) e decidir quais são os objetivos relevantes que o agente deve seguir.

Raciocinio Pratico:
	- É um raciocinio orientado para a ação, ou seja, quais as consequencias da acção para chegar aos pretendidos objetivos 
    (O que fazer para chegar aos objetivos).
	- Elementos de Suporte:
		.Representação dos objectivos a atingir
		.Representação das acções realizáveis
		.Representação do mundo (ambiente)

Este mecanismo é usado na fase de deliberação dentro do ControloDelib. É uma forma de o agente tomar decisões informadas, com base no 
que já percebeu do mundo, em vez de reagir de forma cega.
"""

class MecDelib():

    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        # Gera todos os objetivos possíveis
        objectivos = self.__gerar_objectivos()

        # Se existirem objetivos, selecionamos os que interessam
        if objectivos:
            return self.__seleccionar_objectivos(objectivos)

    def __gerar_objectivos(self):
        # Guardar os estados que são objetivos (com alvo)
        objectivos = []

        # Vamos percorrer todos os estados conhecidos do mundo
        for estado in self.__modelo_mundo.obter_estados():
            # Se nesse estado estiver um elemento do tipo ALVO
            if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO:
                objectivos.append(estado)

        return objectivos
       

    # Ordenar a lista de objetivos com um criterio de distancia ao agente (para ter os alvos mais proximos do agente primeiro)
    def __seleccionar_objectivos(self, objectivos):

        # objectivos.sort(key=self.__modelo_mundo.distancia)
        # Adicionamos o reverse = True para inverter a ordem criado pelo parametro distancia, nesta ultima versão o agente procura
        # primeiro os alvos mais longe.
        objectivos.sort(key=self.__modelo_mundo.distancia, reverse = True)
        return objectivos
    
        # NOTA: não sera possivel retornar a função "sort" diretamente pois esta altera a ordem da lista e retorna none