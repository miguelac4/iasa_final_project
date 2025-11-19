from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax

        # Criamos um dicionário auxiliar que mapeia (estado, acção) para o estado sucessor, se existir.
        # Usado para facilitar o cálculo das transições e dos estados sucessores.
        self.__transicoes = {}
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn = a.aplicar(s) # Simular a acção
                if sn:
                    self.__transicoes[(s, a)] = sn

    def obter_estado(self):
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        return self.__modelo_plan.obter_estados()

    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    def S(self):
        return self.obter_estados()

    def A(self, s):
        # Retornar os operadores à excessão da situação do estado terminal, caso contrario retorna uma lista vazia
        return self.obter_operadores() if s not in self.__objectivos else []

    # Função de transição: verifica se existe uma transição válida de (s, a) para sn.
    def T(self, s, a, sn):
        # Verificar no dicionario de transicoes se existe alguma transicao 
        snt = self.__transicoes.get((s,a))
        # Se existir uma transicao retorna 1 caso contrario retorna 0
        return 1 if snt else 0
        #return 1 if snt == sn else 0 # No nosso caso nao seria necessario 

    def R(self, s, a, sn):
        #Retorna a recompensa maxima se um estado for objetivo, caso contrario retorna 0
        return self.__rmax if sn in self.__objectivos else 0

    def suc(self, s, a):
        # Se hover sucessor retornamos uma lista com o sucessor, caso contrario retornamos uma lista vazia
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []
