from pee.mec_proc.fronteira import Fronteira
import heapq
"""
Esta classe representa uma fronteira com comportamento de fila de prioridade.
"""
#A FronteiraPrioridade recebe um avaliador no construtor, esse avaliador sera para definir a prioridade de cada no.
class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no) # Atualizar a prioridade do nó calculando essa prioridade utilizando o avaliador respetivo
        heapq.heappush(self._nos, no) # heappush() serve para inserir elementos numa heap (fila de prioridade) mantendo a estrutura ordenada.

    def remover(self):
        return heapq.heappop(self._nos) # heppop() remove da mesma forma ordenada

