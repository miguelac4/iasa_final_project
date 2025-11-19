from pee.mec_proc.fronteira import Fronteira

#FIFO (First In First Out)
class FronteiraFIFO(Fronteira):
    # Sob a lista de nós append do nó na ultima posição, dai o uso do append
    def inserir(self, no):
        self._nos.append(no)
