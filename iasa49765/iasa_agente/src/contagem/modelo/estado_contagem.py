from mod.estado import Estado


class EstadoContagem(Estado):
    def __init__(self, valor):
        self.valor = valor # guarda o valor num atributo publico (valor)

    def id_valor(self):
        return self.valor # retorna o identificador unico da instancia de estado