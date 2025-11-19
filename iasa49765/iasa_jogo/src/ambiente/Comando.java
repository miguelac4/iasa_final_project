package ambiente;

/**
 *  Esta interface representa um comando que pode ser executado pelo agente no ambiente.
 *  Um comando pode ser uma ação direta do agente no ambiente, como mover-se ou interagir com objetos.
 */

public interface Comando {

    void mostrar();
}

//pequena nota: interfaces me Java já assumem que os seus métodos são public e abstract