from .comport_comp import ComportComp
class Prioridade(ComportComp):
    
    # Da lista de acçoes escolher a que tem maior prioridade
    def seleccionar_accao(self, accoes):
        if accoes:
            #função lamda (anonima) definir uma função que não tem nome só argumentos para aquele momento
            return max(accoes, key=lambda accao: accao.prioridade) #max permite-nos dizer qual é a chave de avaliação (função que devolve um valor)
