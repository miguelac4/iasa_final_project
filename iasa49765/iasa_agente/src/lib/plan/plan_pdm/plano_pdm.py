class PlanoPDM:
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado): # Para um determinado plano obter accao
        if self.__politica:
            return self.__politica.get(estado) # Se existir politica retorna accao para o estado indicado, caso contrario None

    def mostrar(self, vista):
        if self.__politica:
            # Mostrar Utilidade
            for estado, valor in self.__utilidade.items():
               vista.mostrar_valor_posicao(estado.posicao, valor)
            
            # Mostrar Politica (Em cada posição quero por um vetor da direção da acção na posição)
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)
