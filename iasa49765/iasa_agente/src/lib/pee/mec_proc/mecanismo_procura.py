from abc import ABC

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

"""
Procura em Espaço de Estados:

	Problemas de planeamento:
		.Problemas cuja solução consiste numa sequência de acções a realizar e de situações a percorrer para, 
        partindo de uma situação inicial, atingir um objectivo.

	Arvore de procura:
		.Uma estrutura em árvore, organizada em nós, que mantém informação relativa a cada transição de estado 
        explorada
		.Relaciona cada nó com o seu antecessor e mantendo informação do estado correspondente ao nó e do operador 
        que originou a transição de estado respectiva gerando esse novo estado.
		.Na arvore de procura podem existir nos com os mesmo estado pois o nó pode vir de diferentes caminhos.
		.No antecessor servem quando antigirmos o objetivo e queremos recuperar a sequecia (solução).
		.Custo de cada nó serve para escolher os caminhos com menor custo, arranjar a melhor forma de solucionar
		.Profundidade avalia o caminho por numero de passos enquanto cada passo pode obter um custo diferente.

    Procura numa árvore de procura:
	    .O agente utiliza algoritmos de procura para explorar a árvore e encontrar um caminho desde o estado 
        inicial até ao estado objetivo.

Estas primeiras duas procuras dadas em aula fazem parte do grande grupo das Procuras sem Informação (Uninformed 
Search), em que o agente não possui informação adicional sobre a definição do problema.
"""

# Esta classe será responsavél pelo esqueleto para qualquer algoritmo de procura mais tarde implementado.
class MecanismoProcura(ABC):
    def __init__(self, fronteira):
        self._fronteira = fronteira

    
    def _iniciar_memoria(self):
        self._fronteira.iniciar()

    def _memorizar(self, no):
        #ultizando a fronteira inserir um no
        self._fronteira.inserir(no)

    def procurar(self, problema):

        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        
        while not self._fronteira.vazia:
            no = self._fronteira.remover() # Remover o próximo nó da fronteira
            if problema.objectivo(no.estado): # Se o estado atual for "objetivo", terminamos e devolvemos a solução
                return Solucao(no)
            # Expandir nó atual gerando sucessores
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)
                
        return None
        

    # Irá pegar no nó atual e gerar todos os nós sucessores
    def _expandir(self, problema, no):
        sucessores = [] # Lista para guardar sucessores vazia
        estado = no.estado # Variavel auxiliar explicativa para receber o estado do nó a ser expandido
        
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado) # Aplicar operador ao estado
            if estado_suc is not None:
                # Informaçoes para criar o nó sucessor
                # Somar o custo da transição no estado para o estado sucessor
                custo = no.custo + operador.custo(estado, estado_suc) 
                # Criar nó sucessor
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor) # Justar nó sucessor à lista de nós sucessores
        
        return sucessores # Retorna uma lista de nós sucessores
    
    @property
    def nos_processados(self):
        # Total de nós criados durante o processo
        return No.nos_criados

    @property
    def nos_mem(self):
        # Número máximo de nós em memória
        return No.nos_max_mem
