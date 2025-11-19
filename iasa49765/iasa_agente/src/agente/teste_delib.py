from controlo_delib.controlo_delib import ControloDelib
from controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.estado_agente import EstadoAgente
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.ambiente.ambiente import Ambiente
from sae.agente.transdutor import Transdutor # Dispositivo do agente que tens o sensores e atuadores
from sae.defamb import DEF_AMB
from sae import Elemento, Direccao

from agente.agente_delib import AgenteDelib
from agente.agente_react import AgenteReact
from sae import Simulador

"""
Para desenvolvermos estes testes implementamos asserts (instrução do python que garante uma condição, caso nao se 
verifique dará um excessão)
"""

def teste_modelo_mundo(percepcao):
    modelo_mundo = ModeloMundo() # Criar instancia do Modelo do Mundo

    modelo_mundo.actualizar(percepcao) # Atualizar modelo do mundo
    assert modelo_mundo.alterado == True # Verifica se o modelo reconheceu alterações após a perceção

    estado = modelo_mundo.obter_estado()
    assert estado.posicao == (0, 0) # Verifica se a posição do agente foi corretamente registada no modelo

    estados = modelo_mundo.obter_estados()
    #print(len(estados))
    assert len(estados) == 671 # Confirmar que o modelo detetou todas as posições válidas do ambiente
    # ("671" depende do ambiente definido, neste caso o Ambiente Numero 4)

    operadores = modelo_mundo.obter_operadores()
    assert len(operadores) == 4 # Confirmar que foram criados operadores para as 4 direções possíveis

    estado = EstadoAgente((28, 9))
    elemento = modelo_mundo.obter_elemento(estado)
    assert elemento == Elemento.ALVO # Verifica se o modelo sabe que na posição escolhida existe um alvo

    return modelo_mundo

def teste_mec_delib(modelo_mundo):
    mec_delib = MecDelib(modelo_mundo)

    objectivos = mec_delib.deliberar()
    assert len(objectivos) == 3 # Verifica se o mecanismo foi capaz de identificar 3 alvos como objetivos válidos

    return mec_delib, objectivos

def teste_planeador_pee(modelo_mundo, objectivos):
    planeador = PlaneadorPEE()
    plano = planeador.planear(modelo_mundo, objectivos)
    assert plano.dimensao == 37
    
    return planeador

def teste_controlo_delib(planeador, percepcao):
    controlo = ControloDelib(planeador)
    
    accao = controlo.processar(percepcao)
    assert accao.direccao == Direccao.SUL

# Activação do Teste
if __name__ == "__main__": # "__name__" nome do modulo interno
    num_amb = 4
    ambiente = Ambiente(DEF_AMB[num_amb]) # Instancia ambiente
    # Para obter percepcao precisamos de uma instancia de Transdutor
    transdutor = Transdutor() 
    transdutor.iniciar(ambiente)
    percepcao = transdutor.percepcionar()

    # Teste do modelo do mundo
    modelo_mundo = teste_modelo_mundo(percepcao)

    # Teste do mecanismo deliberativo
    mec_delib, objectivos = teste_mec_delib(modelo_mundo)

    #Teste do planeador
    planeador = teste_planeador_pee(modelo_mundo, objectivos)

    # Teste do Controlo Deliberativo
    teste_controlo_delib(planeador, percepcao)

    print("\nTeste concluido com sucesso\n")

    Simulador = Simulador(4, AgenteDelib(), vista_modelo=True)
    Simulador.executar()