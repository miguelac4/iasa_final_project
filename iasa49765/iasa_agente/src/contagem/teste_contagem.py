# Testes para verificar o python path
#import sys
#print(sys.path)

# Nos modulos executaveis só sao admitidos imports absolutos
from contagem.modelo.problema_contagem import ProblemaContagem
from pee.larg.procura_largura import ProcuraLargura # Descomentar para usar Largura
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.prof.procura_profundidade import ProcuraProfundidade # Descomentar para usar Profundidade
from pee.prof.procura_prof_lim import ProcuraProfLim # Descomentar para usar ProfundidadeLimite
from pee.prof.procura_prof_iter import ProcuraProfIter # Descomentar para usar ProfundidadeIterativa

# Parametros do Problema
VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2, -1]

# Definição do Problema
problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

# Escolher mecanismo de procura
# mec_proc = ProcuraProfundidade() # Descomentar para usar Profundidade
# mec_proc = ProcuraLargura() # Descomentar para usar Largura
# mec_proc = ProcuraProfLim(5) # Descomentar para usar ProfundidadeLimite
# mec_proc = ProcuraProfIter() # Descomentar para usar ProfundidadeIterativa
mec_proc = ProcuraCustoUnif() # Descomentar para usar CustoUniforme

# solucao = mec_proc.procurar(problema)
# Foi criado uma nova solução para conseguirmos usar a ProcuraProfLim (este tem mais dois parametros inc_prof, 
# limite_prof)
solucao = mec_proc.procurar(problema, 1 ,10) 

# Mostrar Solução
if solucao:
    passos = [passo.operador.incremento for passo in solucao]
    estados = [passo.estado.valor for passo in solucao]

    print(f"Solução:  {passos}")
    print(f"Dimensão:  {solucao.dimensao}")
    print(f"Custo: {solucao.custo}")
    print("Nós Processados: ", mec_proc.nos_processados)
    print("Máximo de nós em memória: ", mec_proc.nos_mem)
    print("Número de estados não Repetidos: ", len(mec_proc._explorados))
    for passo in solucao:
        # print(passo.estado.valor)
        # print("-----------")
        # print(passo.operador.incremento)
        print("/////////////////")
else:
    print("Solução não encontrada") # Log se não houver solução