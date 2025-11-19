from pee.mec_proc.fronteira import Fronteira


#LIFO (Last In First Out)
class FronteiraLIFO(Fronteira):
    # Sob a lista de nós insert(0 nó)
    def inserir(self, no):
        self._nos.insert(0, no)