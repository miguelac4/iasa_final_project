from agente.agente_delib import AgenteDelib
from agente.agente_react import AgenteReact
from agente.agente_delib_pdm import AgenteDelibPDM
from sae import Simulador

#Executar Simulador da SAE
# Simulador = Simulador(1, AgenteReact())
# Simulador = Simulador(4, AgenteDelib(), vista_modelo=True)
Simulador = Simulador(4, AgenteDelibPDM(), vista_modelo=True)
Simulador.executar()