from contagem.modelo.estado_contagem import EstadoContagem
from contagem.modelo.operador_incremento import OperadorIncremento
from mod.problema import Problema


class ProblemaContagem(Problema):

    # lista "incrementos" para sabermos quais são os operadores
    # quando antigimos o valor final chegamos à solução
    def __init__(self, valor_inicial, valor_final, incrementos):
        # invocar constutor da super classe recebe um estado inicial (EstadoContagem) com parametro valor_inicial 
        # e uma lista de operadores (uma lista feita com base num gerador)
        super().__init__(EstadoContagem(valor_inicial),
                         [OperadorIncremento(incremento)
                          for incremento in incrementos])
        self.__valor_final = valor_final # Guarda o valor final como atributo privado

    # Verifica se um estado é objetivo
    def objectivo(self, estado):
        # É objetivo se o valor do estado for maior ou igual ao valor final (valor do problema)
        return estado.id_valor() >= self.__valor_final