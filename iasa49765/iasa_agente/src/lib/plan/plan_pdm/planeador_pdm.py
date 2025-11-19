from pdm.pdm import PDM
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM

"""
Qual é o efeito das alterações feitas no agente deliberativo com processos de Marcov?
    O agente passa a decidir com base em utilidades esperadas e recompensas futuras, em vez de seguir apenas o caminho mais curto 
    até ao objetivo.
"""

class PlaneadorPDM:
    def __init__(self, gama = 0.95, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objectivos):
        modelo = ModeloPDMPlan(modelo_plan, objectivos)
        pdm = PDM(modelo, self.__gama, self.__delta_max)
        U, pol = pdm.resolver()
        return PlanoPDM(U, pol)

