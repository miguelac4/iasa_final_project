from controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo


"""

Tipos de Agente:
	- Presente
		.Agentes reactivos sem estado (ausência de memória)
		.Tipo de comportamento possível: Reagir
	- Passado - Presente
		.Agentes reactivos com estado (memória de recordação do passado)
		.Tipo de comportamento possível: Repetir / Evitar
	- Passado - Presente - Futuro
		.Agentes deliberativos (memória de representação e simulação do futuro)
		.É criado uma simulação interna, em memoria, sobre o futuro para o poder anticipar
		. Agentes deliberativos (memória de representação e simulação do futuro)

Arquitetura Deliberativa
	.A memória é o principal, em contrario com a arquitetura reativa, esta contem um papel mais importante no comportamento do agente.
	.Numa arquitectura deliberativa o comportamento é gerado com base em processos de planeamento suportados por representações 
    internas do ambiente.

    Deliberação (RACIOCÍNIO SOBRE FINS): Produz objetivos
	Planeamento (RACIOCÍNIO SOBRE MEIOS): Irá produzir sequencias de ação (planos).

Reconsideração: reconsiderar as opções atuais do sistema.

Processor de tomada de decisão/acção:
	- Observar o mundo
	- Actualizar o modelo do mundo
	- Se Reconsiderar
		- Deliberar
		- Planear
	- Executar plano de acção
"""

class ControloDelib():
    
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo() # Instanciar Modelo do Mundo
        self.__mec_delib = MecDelib(self.__modelo_mundo) # Instanciar o mecanismo deliberativo com o atributo modelo do mundo
        # Adicional 2 atributos privados (objetivos e plano igual a None)
        self.__objectivos = None
        self.__plano = None

    def processar(self, percepcao):
        # 1. Assimilar perceção
        self.__assimilar(percepcao)

        # 2. Verifica se for para reconsiderar
        if self.__reconsiderar():
            # 3. Caso sim, delibera e planeia
            self.__deliberar()
            self.__planear()

        # 4. Executa a acção
        return self.__executar()


    # Atualizar o modelo do mundo com a percepcao
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)  # Atualiza o modelo do mundo com a nova perceção

    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or not self.__plano # Reconsidera se o mundo mudou ou se não existe plano

    def __deliberar(self):
        self.__objectivos = self.__mec_delib.deliberar() # Usa o mecanismo deliberativo para gerar os objetivos com base no estado atual

    def __planear(self):
        if self.__objectivos: # Se houver objetivos definidos, usa o planeador para gerar um plano
            
            # self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
            # Acrescentou-se [0] no self.__objectivos para que apenas seja usado o primeiro objetivo da lista para planear.
            # Assim o agente planeia para um unico alvo de cada vez
            self.__plano = self.__planeador.planear(self.__modelo_mundo, [self.__objectivos[0]])

        else:
            self.__plano = None # Se não houver objetivos o plano tem de ser definido como None


    def __executar(self):
        if self.__plano:
            # Obter o operador do plano que corresponde ao estado actual do agente
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao
            else:
                self.__plano = None
        else:
            return None
        
    # Iremos usar o mostrar do modelo do mundo
    def mostrar(self, vista):
        vista.limpar() # Limpar a vista
        self.__modelo_mundo.mostrar(vista) # Pedir ao modelo do mundo para se mostrar
        # Se existir plano
        if self.__plano:
            self.__plano.mostrar(vista) # Mostrar o plano
        # Se existirem objetivos
        if self.__plano:
            # Para cada objetivo dos objetivos marcamos a posicao com a posicao do objetivo
            for objectivo in self.__objectivos:
                vista.marcar_posicao(objectivo.posicao)