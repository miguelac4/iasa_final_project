#NOTAS GERAIS:
#   O objetivo do Sistema Prospetor de Recolha de Alvos é desenvolver um sistema capaz de identificar e evitar alvos 
#   de forma eficiente, permitindo que o agente se desvie de obstáculos com precisão.

#   É necessário programar a lógica interna do sistema para que ele consiga identificar corretamente os estímulos do 
#   ambiente e associá-los às respostas adequadas que deve gerar.

#   A perceção do agente é modelada através da classe Percepção, que num sistema reativo representa a capacidade do 
#   agente de recolher informações do meio envolvente.

# A associação entre um estímulo e uma resposta chama-se reação. Esta reação funciona como um mecanismo interno do 
#  agente, estabelecendo uma relação entre a deteção do estímulo e a ação a ser tomada como resposta.

# Import Notes
#   Imports absolutos para que tudo seja reocalizavel, estão dependestes do python path ou do path corrente
#   Imports relativos começam com ponto (1 ponto = pasta local, 2 pontos = pasta acima, etc), estes não podem ser 
#       utilizados em modulos executaveis.

from .comportamento import Comportamento # Import relativo
# Como as interfaces no python são abstratas será necessário herdar
class Reaccao(Comportamento):

    def __init__(self, estimulo, resposta):
        ##-------------self.__estimulo = estimulo
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao):
        # Primeiro o estímulo é detetado com base na perceção recebida.
        # O método detectar() do estímulo vai analisar essa perceção e devolver uma intensidade.
        #-------------intensidade = self.__estimulo.detectar(percepcao)
        intensidade = self.__estimulo.detectar(percepcao)
        # Se a intensidade for maior que zero, significa que o estímulo foi o suficiente
        # para haver uma resposta.
        if(intensidade > 0):
            # A resposta é ativada, passando a perceção e a intensidade como parâmetros.
            accao = self.__resposta.activar(percepcao, intensidade)
            return accao #Retorna uma Acção
        #Não será necessario retornar none porque em python por omissão todos os métodos retornam None
            
        