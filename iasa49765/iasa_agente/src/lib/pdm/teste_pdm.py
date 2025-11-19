from modelo.modelo_pdm import ModeloPDM
from pdm import PDM

"""
Modelo do ambiente 7x1 baseado num PDM (Processo de Decisão de Markov).
Este modelo é determinista, ou seja, a transição entre estados é certa (probabilidade 1),
e baseia-se em dois tipos de acções: mover para a esquerda ou mover para a direita.
"""

class ModeloAmbiente7x1(ModeloPDM):
    
    def __init__(self,):
        self.__S = [1, 2, 3, 4, 5, 6, 7] # Conjunto de Estados
        self.__A = ["<", ">"] # Lista para a esquerda e para a direita (caracter menor: "<", caracter maior: ">")
        
        
        

        # Dicionário de transições deterministas T(s, a, s') -> probabilidade [0 ou 1]
        self.__T = { # Definir o domínio da função de transição T como um conjunto cartesiano S × A × S'
            (1, "<", 1): 0,
            (1, ">", 2): 0,
            (2, "<", 1): 1,
            (2, ">", 3): 1,
            (3, "<", 2): 1,
            (3, ">", 4): 1,
            (4, "<", 3): 1,
            (4, ">", 5): 1,
            (5, "<", 4): 1,
            (5, ">", 6): 1,
            (6, "<", 5): 1,
            (6, ">", 7): 1,
            (7, "<", 6): 0,
            (7, ">", 7): 0
        }

        # Dicionário de recompensas R(s, a, s')
        self.__R = { # Definir o domínio da função de recompensa R como um conjunto cartesiano S × A × S'
            (1, '<', 1): 0,
            (1, '>', 2): 0,
            (2, '<', 1): -1, # penalização por chegar ao estado de perda (estado "1")
            (2, '>', 3): 0,
            (3, '<', 2): 0, 
            (3, '>', 4): 0,
            (4, '<', 3): 0, 
            (4, '>', 5): 0,
            (5, '<', 4): 0, 
            (5, '>', 6): 0,
            (6, '<', 5): 0, 
            (6, '>', 7): 1, # recompensa por chegar ao estado de ganho (estado "7")
            (7, '<', 6): 0, 
            (7, '>', 7): 0
        }

    def S(self):
        return self.__S # Retorna o conjunto de todos os estados possíveis no ambiente

    def A(self, s):
        return self.__A if s not in [1, 7] else[] # Retorna a lista de acções possíveis num dado estado s.
        
    def T(self, s, a, sn):
        return self.__T[(s, a , sn)] # Retorna a probabilidade da transição ocorrer, indexando no dicionario T
        
    def R(self, s, a, sn):
        return self.__R[(s, a , sn)] # Retorna a probabilidade da transição ocorrer, indexando no dicionario R
        
    # Retorna a lista de estados sucessores possíveis para o par (s, a), consultando o dicionário transicoes previamente 
    # calculado, caso nao haja sucessor retorna uma lista vazia
    def suc(self, s, a): 

        # Criou-se um atributo privado extra para definir as transições
        # Por cada par (estado, accao) vai se difinir um estado sucessor
        # Ira haver uma entrada se o estado não for o estado terminal
        self.__transicoes = {(s,a): sn for (s, a, sn) in self.__T if s not in [1, 7]}

        sn = self.__transicoes.get((s, a)) # Buscar estado sucessor
        return [sn] if sn else [] 
        
# Dois underscores internos sera o nome do modulo que está a correr, significa se o modulo esta a ser diretamente executado
if __name__ == "__main__": 
    modelo = ModeloAmbiente7x1()# Instanciar o modelo_pdm
    gama = 0.5
    delta_max = 0.1

    pdm = PDM(modelo, gama, delta_max) # Instanciar PDM

    U, pol = pdm.resolver()

    print("Utilidades:", U)
    print("Politicas:", pol)

    
    