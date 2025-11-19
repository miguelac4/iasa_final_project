# Quando obtemos uma solução obtemos o ultimo nó
from pee.mec_proc.passo_solucao import PassoSolucao


class Solucao:
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__passos = [] # iniciado como uma lista vazia

        no = no_final
        # percorrer todos os nós enquanto tiverem nós sucessores
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            # Insert() para inserir os passos pela ordem certa visto que estamos a percorrer do ultimo para 
            # o mais recente
            self.__passos.insert(0, passo)
            # Recuar o nó, para chegar ao nó sem sucessor
            no = no.antecessor

    #<<iterable>> - é uma classe cujos objetos podem ser percorridos um item de cada vez, mecanismo para definir 
    # uma iteração
	# uma classe iteravél tem obrigatoriamente o método def __iter__(self)
    def __iter__(self):
        return iter(self.__passos)

    # retornar a partir do index de forma mais prática (ex: self.passos[2])
    def __getitem__(self, index):
        return self.__passos[index]

    @property
    def dimensao(self):
        # Profundidade do no final por ser incrementada no a no
        return self.__no_final.profundidade
    
    @property
    def custo(self):
        # Custo do nó final por ser acumulado
        return self.__no_final.custo