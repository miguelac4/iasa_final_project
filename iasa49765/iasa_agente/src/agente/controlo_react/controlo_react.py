"""
Controlo do agente a partir de um control reactivo, como implementado na primeira parte da cadeira.

Programa-se um agente reactivo com os conceitos base Reaccao e Comportamento, a nossa biblioteca 
ecr disponibiliza-os.

A função do controlo no contexto do ciclo de controle do agente será associar o método processar a um controlo

Representa o módulo de controlo na arquitetura do agente, sendo responsável por gerir a ativação dos 
comportamentos com base nas perceções do ambiente.

O controlo atua  entre a perceção do meio envolvente e a execução de ações, ativando os comportamentos registados 
e recolhendo as ações que resultam dessas ativações.

Esta estrutura permite ao agente reagir de forma automática e dinâmica ao ambiente, garantindo uma resposta 
rápida a estímulos detetados.
"""
class ControloReact():
    
    def __init__(self, comportamento):
        self.__comportamento = comportamento

    # Recebe uma percepcao e retorna a ativação do comportamento passando a accão
    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)