from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao
"""
Aproximar alvo especializa prioridade e instancia o aproximar direcional.

	O agente vai aproximar o alvo mais proximo, irá ter sensores nas quatro direções, portanto vai ter 4 reacções

	4 instancias de reacções de aproximar alvo (comportamentos internos):
		.Aproximar alvo (direcção = NORTE)
		.Aproximar alvo (direcção = SUL)
		.Aproximar alvo (direcção = ESTE)
		.Aproximar alvo (direcção = OESTE)

	No abstrato estas quatro instâncias são reacções pois necessitam de estimulos (especialização de reacção).

	Cada acção vamos associar uma prioridade que sera a função inversa porporcional à distancia.
"""

class AproximarAlvo(Prioridade):
    def __init__(self):
        # No constructor usamos a superclasse Prioridade para evocarmos um AproximarDir com cada direcção.
        # Lista de reacções AproximarDir para cada direcção (NORTE; SUL; ESTE; OESTE, 
        # estas presentes na biblioteca sae)
        comportamentos = [AproximarDir(direccao) for direccao in Direccao]
        super().__init__(comportamentos)
        
