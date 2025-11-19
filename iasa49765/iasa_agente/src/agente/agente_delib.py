from sae import Agente
from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE

"""
Um agente deliberativo, ao contrário de um agente reativo, não reage logo aos estímulos, em vez disso, analisa o que está à 
volta, escolhe os objetivos e planeia como os atingir, só depois de ter um plano é que decide o que fazer.

Este tipo de agente usa memória e mantém uma ideia do que já viu no mundo.
Isso permite-lhe pensar à frente, ou seja, imaginar o que pode acontecer no futuro.
Enquanto os agentes reativos respondem logo, os deliberativos escolhem o caminho mais inteligente.

"""

class AgenteDelib(Agente):
    
    def __init__(self):
        planeador = PlaneadorPEE() # Criamos uma instância do planeador PEE
        self.__controlo = ControloDelib(planeador)
        super().__init__() # Chamar o construtor da superclasse Agente

    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao) # O controlo deliberativo processa essa perceção
        self.__controlo.mostrar(self.vista) # Para mostrar caminho na janela extra
        self._actuar(accao)
