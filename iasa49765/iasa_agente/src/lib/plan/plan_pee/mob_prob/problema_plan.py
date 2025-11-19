from mod.problema import Problema


class ProblemaPlan(Problema):

    def __init__(self, modelo_plan, estado_final):
        # Evoca o construtor da superclasse (classe problema) dentro da evocação do construtor da super classe: modelo_planeamento.obter_estado
        # segundo parametro da evocação da superclasse sera sob parametro obter_operadores
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final # Guarda estado final num atributo privado estado final

    def objectivo(self, estado):
        return estado == self.__estado_final # retornar verdade se o estado passado for igual ao estado final