from ecr.resposta import Resposta
from sae.agente.rodar import Rodar


class RespostaEvitar(Resposta):
    # Assim que um agente apanhar um obstaculo o agente ira alterar a direcção
        
    def activar(self, percepcao, intensidade):
        dir_agente = percepcao.direccao
        if percepcao.contacto_obst(dir_agente):
            dir_resposta = dir_agente.rodar()
            self._accao = Rodar(dir_resposta)
            return super().activar(percepcao, intensidade)