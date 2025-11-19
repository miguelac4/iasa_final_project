from contagem.modelo.estado_contagem import EstadoContagem
from mod.operador import Operador

# Representa um operador de incremento no problema
class OperadorIncremento(Operador):

    def __init__(self, incremento):
        self.incremento = incremento # Guarda o valor do incremento que este operador vai aplicar

    # retorna uma nova instancia de EstadoContagem(estado_antecessor incrementado pelo incremento do operador)
    def aplicar(self, estado):
        return EstadoContagem(estado.valor + self.incremento) # Cria um novo estado com o valor incrementado

    # Calcula o custo da transição entre estados
    def custo(self, estado, estado_suc):
        # O custo será o quadrado do incremento (**) independentemente do estado e do estado sucessor
        return self.incremento ** 2 