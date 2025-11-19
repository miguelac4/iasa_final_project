"""
Comparação Temporal entre Mecanismos
		Uma métrica geral para comparar o tempo de cada mecanismo de procura será o numero de nós. Assim medimos a 
        quantidade temporal a partir da quantidade de nós processados.
		Complexidade temporal: numero de nós processados
		Complexidade espacial: numero de nós em memória

"""

class No:
    """
    Engenharia de software:
		Em python os atributos estáticos são comuns a todas as instâncias, assim usamos atributos estáticos referenciando 
        apenas o nome da classe.
    """
    nos_criados = 0
    nos_eliminados = 0
    nos_max_mem = 0 # Nos maximo em memória

    def __init__(self, estado = None, operador = None, antecessor = None, custo = 0.0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        # Se não houver antecessor a profundidade será 0, o nó criado será o nó raiz
        if antecessor is None:
            self.__profundidade = 0
            # Caso não exista sucessor os contadores serão reiniciados
            No.nos_criados = 0
            No.nos_eliminados = 0

        else:
            self.__profundidade = antecessor.profundidade + 1 

        No.nos_criados += 1 # Incrementar nos criados, pois a cada chamado do construtor é criado um novo nó

        nos_em_mem = No.nos_criados - No.nos_eliminados # Variavel local, nós em memória no atual momento
        No.nos_max_mem = max(No.nos_max_mem, nos_em_mem) # Guarda o maximo numero de nós em memoria
        self.__prioridade = 0

    def __del__(self): # Função Python chamada automáticamente quando o objeto é destruido
        No.nos_eliminados += 1 # Incrementar nos eliminados, pois cada chamada do destrutor destroi um nó

    # __lt__ é um método interno do python chamado automaticamente quando usamos o operador  "<" e define a ordem de 
    # comparação entre objetos
    def __lt__(self, other):
        return self.prioridade < other.prioridade

    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def antecessor(self):
        return self.__antecessor
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, other):
        self.__prioridade = other