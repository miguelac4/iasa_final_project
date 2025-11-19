from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador

# @dataclass - é uma forma de definer estrutura e dados, possivel no python
# O python automaticamente gera os contrutores necessários e as suas propriedades
@dataclass
class PassoSolucao:
    estado : Estado
    operador : Operador
