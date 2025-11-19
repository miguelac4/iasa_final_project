from abc import ABC, abstractmethod
"""
Uma heurística é uma função que estima o custo desde o estado atual até ao objetivo. Fornece orientação sobre qual direção 
explorar, atribuindo prioridades aos possíveis estados.
A qualidade da heurística influencia a rapidez com que os algoritmos encontram a solução. Uma boa heurística pode reduzir 
significativamente o espaço de procura.
É usada em algoritmos de procura informada, como a procura sofrega ou A*, para ajudar a decidir quais os nós mais 
# promissores a expandir primeiro.
"""

class Heuristica(ABC):

    @abstractmethod
    def h(self, estado):
        pass