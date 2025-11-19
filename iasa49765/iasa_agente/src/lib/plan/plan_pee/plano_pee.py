from plan.plano import Plano

"""
A classe PlanoPEE serve para representar um plano que é gerado depois de ser feita uma procura (como o AA).
Esse plano é basicamente uma lista de passos que o agente deve seguir para chegar ao objetivo.
Cada passo do plano tem um estado e um operador, e os passos estão ordenados. Quando o agente precisa de agir, o plano vê se 
o estado atual é o esperado e, se for, devolve o operador certo para seguir o caminho.
Também tem um método para mostrar graficamente o plano (com setas nas direções) e dá a dimensão do plano, ou seja, quantos 
passos foram definidos desde o início.
"""

class PlanoPEE(Plano):
    
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao] # converter a solucao numa sequencia de passos
        self.__dimensao = len(self.__passos)
        
        
    def obter_accao(self, estado):
        
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador
        
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
            
    @property
    def dimensao(self):
        return self.__dimensao
