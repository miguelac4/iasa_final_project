#Este modulo necessita da classe accao.py (dentro da classe sae)
#Notas sobre a classe Accao
#   Quando um agente deparase com múltiplas reações possíveis, é necessario a seleção da ação. 
#   (Permite ao agente decider a 	resposta com base nas informações recolhidas e dos estímulos detetados)

#   A arquitetura de reação baseia-se na associação direta entre estímulo e resposta. Assim, quando o agente 
#   perceciona o 	ambiente, ele identifica um estímulo e avalia a sua intensidade. Caso essa intensidade 
#   seja superior a um determinado 	limiar, o estímulo é validado e desencadeia uma resposta, que por sua vez 
#   ativa uma ação apropriada.

#   A arquitetura de reação funciona como um reflexo automático do agente, quando ele percebe um estímulo, 
#   avalia quão forte ou relevante esse estímulo é. Se tiver alguma intensidade, isso desencadeia uma 
#   resposta, que por sua vez faz com que o agente tome uma ação.

"""
	Representa uma resposta da reação/comportamento, gera a acção e as condições de gerar ação e verificarem
		Condições:
			- tem de existir uma precepção
			- ter uma intensidade vinda de um estimulo

	Seleção da acção
		#Hierarquia
		Hierarquia: Os comportamentos estão organizados numa lista de hierarquia fixa.
		#Prioridade
		Prioridade: As respostas são seleccionadas de acordo com uma prioridade associada que varia ao longo da execução, cada resposta (acção) tem uma prioridade associada que pode mudar com o tempo, acçao não sera fixa.
		Combinação: As respostas são combinadas numa única resposta por composição, implica uma codificação vetorial e usa a soma vetorial.

	Classes como Hierarquia.py e Prioridade.py ambas têm um mecanismo de selecionar a acção.
"""

class Resposta:
    def __init__(self, accao = None):
        self._accao = accao

    # Neste método se existir uma precepcao a prioridade da acção associada à resposta é atualizada com o 
    # valor de intensidade.
    def activar(self, percepcao, intensidade=0):
        if percepcao is not None:
            self._accao.prioridade = intensidade

        return self._accao #Retorna uma Acção