package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;
/**
 * Esta classe representa um exemplo de um sistema autonomo inteligente.
 * A jogo.personagem interage com o ambiente e age com base nas perceções recebidas.
 * Esta classe herda a classe Agente.
 */

public class Personagem extends Agente {

    public Personagem(AmbienteJogo ambiente){
        super(ambiente, new ControloPersonagem());
    }

}
