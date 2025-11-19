from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.explorar.explorar_mem import ExplorarMem
from ecr.hierarquia import Hierarquia


class Recolher(Hierarquia):
        def __init__(self):
                # Comportamento composto com hierarquia de subcomportamentos 
                # (AproximarAlvo > EvitarObst > Explorar)
                #super().__init__([AproximarAlvo(), EvitarObst(), Explorar(0.7)])
                super().__init__([AproximarAlvo(), EvitarObst(), ExplorarMem(), Explorar(0.7)])