from .comport_comp import ComportComp

# Na lista acção a primeira vai ser a mais prioritaria
class Hierarquia(ComportComp):
    
    # Verifica se existem acções e retorna o primeiro elemento da lista de acções.
    def seleccionar_accao(self, accoes):
        if accoes:
            return accoes[0]