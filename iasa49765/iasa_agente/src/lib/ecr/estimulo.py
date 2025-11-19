#Uma interface é do tipo abstrado (define mas não implementa) não tem nenhum atributo concreto.
#Como Estimulo é uma interface não tem atributos

#Notas UML: os tipos no modelo não se definem em python
from abc import ABC, abstractmethod #Abstract Base Class

#O estímulo representa qualquer evento detetável no ambiente que possa influenciar o comportamento do agente. 
#A classe 	responsável pela deteção do estímulo deverá determinar a intensidade, permitindo que o agente avalie 
#a sua relevância.

# no(_) -> visivel
# _     -> protegido
# __    -> privado

class Estimulo(ABC):
    @abstractmethod #Definir que é um método abstrato, como é um método abstrato não se mete nenhum executavel
    def detectar(self, percepcao): 
        """"Detectar estímulo numa percepcão""" #Para não dar erro mete-se um Tot(?) String
        