from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

"""
Evitar Obstaculo especializa hierarquia.
"""


class EvitarObst(Hierarquia):
        
        def __init__(self):
            # No constructor usamos a superclasse Hierarquia para evocarmos um EvitarDir com cada direcção.
            # Lista de reacções EvitarDir para cada direcção (NORTE; SUL; ESTE; OESTE, 
            # estas presentes na biblioteca sae)
            comportamentos = [EvitarDir(direccao) for direccao in Direccao]
            super().__init__(comportamentos)