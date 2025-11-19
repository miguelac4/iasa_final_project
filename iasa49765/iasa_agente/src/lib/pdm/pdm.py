from .mec_util import MecUtil
from pdm.modelo.modelo_pdm import ModeloPDM
"""
Processos de decisão sequencial
    Nos processos de decisão sequencial, as decisões do agente vão influenciar não só o que acontece no momento, mas também 
    o que pode acontecer mais à frente. Quando o agente executa uma acção, nem sempre se sabe com certeza qual vai ser o resultado 
    (não existe concretamente determinismo, ou seja, a acção pode levar a diferentes estados com probabilidades diferentes).

    Estas situações formam o que se chama um espaço de estados não-determinista, em que a transição de um estado para outro depende 
    da acção escolhida e da sua probabilidade de sucesso.

Propriedade de Markov
    Para este novo modelo irá ser necessário a aplicação da matemática.

    A Propriedade de Markov diz-nos que, num processo estocástico (isto é, um processo com incerteza), o que vai acontecer a seguir 
    depende apenas do estado actual e não do caminho que foi feito para lá chegar. 

    Um Processo de Decisão de Markov (PDM) é uma forma de representar ambientes onde as acções podem ter resultados incertos. Este 
    modelo descreve o mundo com:	
        - Conjunto de Accoes
        - Conjunto de Estados
        - Função de Transição T(s, a, s') -> [0, 1]
            s : S "conjunto de estados"
            a : A(s)  "conjunto de ações"
            s' : "estado seguinte"
        - Recompensa Esperada por fazer a Transição
        - Tempo Discreto

A medida de desempenho serve para avaliar quão boa é a sequência de decisões de um agente. Em vez de olhar só para o resultado 
imediato, esta medida considera o efeito acumulado das decisões ao longo do tempo, através das recompensas recebidas em cada 
transição de estado. No fundo, permite perceber se o agente está a ganhar ou a perder com as suas escolhas.

Num processo de decisão, o agente não deve apenas reagir ao momento, mas sim avaliar qual das ações possíveis trará maior recompensa, 
de todas as possiveis.

Utilidade
    A utilidade de um estado representa o valor que pode ser obtido a partir desse estado ao longo de uma sequência de evolução 
    de estado.
    Uma forma possivel para o calculo dessa Utilidade será a soma dessas todas recompensas.

Recompensa Descontada no Tempo
    Em problemas de decisão sequencial, a recompensa que o agente recebe pode ser descontada ao longo do tempo. as recompensas futuras 
    valem menos do que recompensas imediatas, porque quanto mais distante no tempo maior a incerteza ou menor o impacto. 
    O desconto é controlado por um fator gama, entre 0 e 1. 
        - Se mais próximo de 1, mais importância damos ao futuro
        - Se mais próximo de 0, valorizamos mais as recompensas imediatas.

"""

class PDM:
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo # Guardar o modelo como atributo privado
        self.__mec_util = MecUtil(modelo, gama, delta_max) # Instanciar o mecanismo de utilidade com os parâmetros fornecidos
        # self.__gama = gama
        # self.__delta_max = delta_max
        
    """
    Política π(s)
            - Estratégia que define qual acção tomar em cada estado.
            - Pode ser:
                .Determinista → uma única acção por estado.
                .Estocástica → distribuição de probabilidades sobre as acções.
            - Define que acções são consideradas no cálculo da utilidade com política U^π(s).
            - Baseia-se no valor esperado das acções.

        Política Óptima π*(s)
            - Escolhe a acção com maior valor esperado
            - A acção que maximiza a utilidade maxima
            - Uma vez conhecida, é usada para calcular a utilidade óptima.
            - Cria um ciclo com a utilidade, pois ambas se dependem.
    """
    def politica(self, U):
        S = self.__modelo.S
        A = self.__modelo.A
        util_accao = self.__mec_util.util_accao
        pol = {s: max(A(s), key=lambda a: util_accao(s, a, U)) for s in S() if A(s)} # Lambda serve como adaptador
        # Esta função Lambda é usada para calcular dinamicamente o valor associado a cada acção
        
        return pol
        
    def resolver(self): 
        U = self.__mec_util.utilidade() # Calcular utilidade ótima dos estados

        pol = self.politica(U) # Calcular a política ótima com base nessa utilidade
        
        return U, pol