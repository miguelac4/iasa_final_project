"""
Modelo de Transição T(s, a, s') e Modelo de Recompensa R(s, a, s')
	- São a base do ambiente.
	- Permitem perceber:
		.Para onde se pode ir ao executar uma acção a no estado s (probabilisticamente).
		.O que se ganha ao fazer essa transição.
	- São utilizados no cálculo do valor esperado de uma acção.

 Fator de Desconto y
	- Aplica-se às recompensas futuras.
	- Recompensas distantes valem menos, incentivando decisões com foco no curto/médio prazo.
	- Fundamental no cálculo da utilidade de um estado.

Valor Esperado (Combina T, R e y)
	- Este valor representa o valor total esperado ao tomar uma acção a no estado s.
	- Base da Equação de Bellman.
	- Serve para escolher a melhor acção.

Utilidade U(s)
	- Mede o valor de estar num estado, tendo em conta recompensas futuras.
	- É calculada recursivamente com base nos valores esperados de todas as acções possíveis.
	- Depende diretamente de T, R e y.

Utilidade Óptima U*(s)
	- Máximo valor possível num estado assumindo seguimento de π*.
	- Serve para validar ou melhorar a política actual.
	- Depende de T, R, γ.
"""

class MecUtil:
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    """
    Calcula a utilidade de cada estado usando Iteração de Valor.
    A utilidade U(s) representa o valor de estar num estado, tendo em conta as recompensas futuras esperadas.
    Calculada recursivamente a partir do valor esperado das acções, depende de T, R e gama.
    """
    def utilidade(self): # Calcula e devolve a utilidade de todos os estados.
        U = {s: 0.0 for s in self.__modelo.S()} # Inicializar U(s) = 0, ∀s ∈ S

        Uant = U.copy() 

        while True:
            Uant = U.copy()  # Guardar utilidade anterior para cálculo de erro
            #(.copy() faz uma cópia superficial do dicionário (nível único), necessária para comparação entre iterações)
            delta = 0  # Erro máximo nesta iteração

            # Para cada estado do modelo
            for s in self.__modelo.S():
                # Calcular a melhor utilidade possível para as acções disponíveis
                U[s] = max([self.util_accao(s, a, Uant) 
                                        for a in self.__modelo.A(s)],
                                        default=0.0) 
                # O max de uma lista vazia dava uma excessao, com o default retorna esse valor do default.
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= self.__delta_max:
                break
        return U
                
                
        
    """
    Calcula a utilidade esperada da acção `a` no estado `s`, com base na função de utilidade `U`.
    Este método implementa a equação para o valor esperado de uma acção:
        U_acção(s, a) = ∑ T(s, a, s') * [R(s, a, s') + y * U(s')]
    
            T(s, a, s') é a probabilidade de passar do estado s para s' ao executar a acção a.
            R(s, a, s') é a recompensa imediata associada à transição.
            y (gama) é o fator de desconto, que reduz o peso das recompensas futuras.
            U(s') é a utilidade do estado seguinte s'.
    O valor devolvido representa o valor total esperado da acção a no estado s e será usado para escolher a melhor acção no 
    cálculo da utilidade de cada estado.
    """
    def util_accao(self, s, a, U): # Devolve a utilidade esperada da acção `a` no estado `s`, com base na utilidade `U`
        T = self.__modelo.T
        R = self.__modelo.R
        gama = self.__gama
        suc = self.__modelo.suc

        return sum(T(s, a, sn) * (R(s, a, sn) +  gama * U[sn]) for sn in suc(s, a))
            
