# Imports absolutos
from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.recolher import Recolher
from sae import Agente

class AgenteReact(Agente):

    def __init__(self):
        #comportamento = Explorar(0.7) # Instanciar um comportamento incial que será explorar
        comportamento = Recolher()
        # O controlo reactivo do agente é baseado nas reações do comportamento
        self.__controlo = ControloReact(comportamento)
        # Chama-se o construtor da superclasse Agente com o controlo anterior como argumento
        super().__init__()

    # Controlo irá processar uma percepcao do agente
    # Executar é um modelo de percepcao com três passos: Percepcionar - Processar - Actuar
    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self._actuar(accao)