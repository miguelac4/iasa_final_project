package agente;

/**
 *  Engenharia de Software:
 *      - Segue o princípio aberto/fechado (OCP), permitindo a criação de novas ações sem modificar o código existente.
 *      - Mantém a separação de preocupações definindo ações de forma isolada.
 *
 *  Representa uma ação realizada pelo agente.
 *  A ação pode ser simples (executar um comando) ou complexa (envolvendo planeamento e aprendido).
 */

import ambiente.Comando;

public class Accao {

    public Comando comando;

    public Accao(Comando comando){
        this.comando = comando;
    }

    //Será omitido o Set pois no UML temos um readOnly
    public Comando getComando(){
        return comando;
    }

}
