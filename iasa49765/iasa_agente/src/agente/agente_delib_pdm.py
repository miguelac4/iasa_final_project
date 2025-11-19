from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Agente


"""
Agente Deliberativo com Planeamento baseado em Modelos PDM (Processos de Decisão Markov).

Este agente utiliza um modelo PDM para decidir as ações a tomar, baseando-se não apenas nos objetivos mas também nas recompensas 
esperadas e na incerteza do ambiente.

Funciona em 3 etapas:
  - Observa o mundo e atualiza o modelo interno.
  - Reconsidera se deve planear de novo.
  - Planeia com base num modelo PDM e executa a melhor ação segundo a política gerada.
"""

class AgenteDelibPDM(Agente):

    def __init__(self):
        planeador = PlaneadorPDM()  # Planeador que resolve pdm
        self.__controlo = ControloDelib(planeador)  # Reutiliza o mesmo controlo deliberativo
        super().__init__()

    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)
