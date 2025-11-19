from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from plan.plan_pee.mob_prob.heur_dist import HeurDist
from plan.plan_pee.mob_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

"""
A classe PlaneadorPEE é responsável por gerar planos com base num problema de planeamento. 
O objetivo desta classe é transformar um conjunto de estados e operadores num plano concreto que o agente vai seguir para atingir 
um dos seus objetivos. No método planear, o planeador começa por escolher o primeiro objetivo da lista recebida. A seguir, cria 
uma instância do problema (ProblemaPlan) com o estado atual e os operadores disponíveis. Também se cria uma heurística (HeurDist) 
que vai ajudar o algoritmo de procura a decidir quais os melhores caminhos a explorar.
Depois disso, o planeador chama o método procurar do mecanismo de procura (A*), passando o problema e a heurística. Se for 
encontrada uma solução, essa solução é convertida num plano (PlanoPEE) que o agente vai poder usar para se orientar até ao objetivo.
"""

class PlaneadorPEE(Planeador):

    def __init__(self):
        #self.__mec_pee = ProcuraCustoUnif()
        self.__mec_pee = ProcuraAA()
    
    def planear(self, modelo_plan, objectivos):
        objectivo_inicial = objectivos[0]
        estado_final = objectivos[0] # Criamos uma variavel local "estado_final" fica com o primeiro objetivo
        # Criamos uma instancia de problema de planeamento chamada "problema" e passamos o modelo_plan e o primeiro 
        # da lista "objectivos"
        self.problema = ProblemaPlan(modelo_plan, objectivo_inicial)
        self.__heur_dist = HeurDist(objectivo_inicial) # Instanciar a heuristica de distancia
        # Gerar uma solução para o problema utilizando o mecanismo de procura em espaço de estados de custo uniforme
        solucao = self.__mec_pee.procurar(self.problema, self.__heur_dist)
        # Se existir uma Solucão, retorna uma instãncia "Planopee" com essa solucao
        if solucao is not None:
            return PlanoPEE(solucao)