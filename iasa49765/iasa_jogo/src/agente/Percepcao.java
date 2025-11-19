package agente;

import ambiente.Evento;

/**
 *  Engenharia de Software:
 *      - Encapsula os dados do ambiente.
 *      - Permite implementação flexível para diferentes tipos de percepção.
 *
 *  Nesta classe "Percepcao" representamos uma precepção do ambiente
 */
public class Percepcao {

    public Evento evento;

    public Percepcao(Evento evento){
        this.evento = evento;
    }

    //Será omitido o Set pois no UML temos um readOnly
    public Evento getEvento(){
        return evento;
    }
}
