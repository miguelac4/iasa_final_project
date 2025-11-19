from ecr.estimulo import Estimulo


class EstimuloObst(Estimulo):
    def __init__(self, direccao, intensidade = 1):
        self.__direccao = direccao
        self.__intensidade = intensidade

    def detectar(self, percepcao):
        # avalia se existe um contacto com o obstaculo e caso seja verdade retorna a intensidade 
        # guardada no construtor
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0 