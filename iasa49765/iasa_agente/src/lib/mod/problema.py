from abc import ABC, abstractmethod

"""
Problema: Qual é o estado inicial, quais os operadores que se podem utilizar e qual será o objetivo.

Para encontrar/solucionar problemas:
	- espaço de estados
	- uma função sucessora (com acções e custos)
	- um estado inicial e um objetivo

A solução será uma sequencia de ações que passam o estado inicial para estado objetivo.

Raciocinio Automático:
	Refere-se à capacidade de um sistema computacional resolver de forma automática um problema com 
    base numa representação de conhecimento
	
	Este processo envolve dois tipos de actividades:
		- Explorar Opções
		- Avaliar Opções

Representação Interna do Mundo é baseada em duas representações: representacção do estado (configuração da 
situação) e representação do operador (representação a acção) estes produzem transições de estados.

"""

class Problema(ABC):
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @abstractmethod
    def objectivo(self, estado):
        pass

    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    @property
    def operadores(self):
        return self.__operadores